#!/usr/bin/env python3
"""
Claude Code Monthly Report Generator

Generates executive-ready reports comparing:
- Current metrics vs. baseline
- Current metrics vs. last month
- Trends over time

Usage:
    python generate_report.py                          # Generate current month report
    python generate_report.py --compare baseline.json  # Compare to baseline
    python generate_report.py --format html            # Output format
    python generate_report.py --send-email             # Email report to stakeholders
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class MetricDelta:
    """Change in a metric"""
    name: str
    current: float
    previous: float
    delta: float
    delta_percent: float
    is_improvement: bool
    category: str


class ReportGenerator:
    """Generates comparison reports from collected metrics"""

    def __init__(
        self,
        current_metrics_path: str,
        baseline_metrics_path: Optional[str] = None,
        previous_metrics_path: Optional[str] = None,
    ):
        self.current = self._load_metrics(current_metrics_path)
        self.baseline = self._load_metrics(baseline_metrics_path) if baseline_metrics_path else None
        self.previous = self._load_metrics(previous_metrics_path) if previous_metrics_path else None

    def _load_metrics(self, path: str) -> dict:
        """Load metrics from JSON file"""
        with open(path) as f:
            return json.load(f)

    def generate_report(self, format: str = "markdown") -> str:
        """Generate the report in specified format"""
        if format == "markdown":
            return self._generate_markdown()
        elif format == "html":
            return self._generate_html()
        elif format == "json":
            return self._generate_json()
        else:
            raise ValueError(f"Unknown format: {format}")

    def _calculate_deltas(self, compare_to: dict) -> list[MetricDelta]:
        """Calculate deltas between current and comparison metrics"""
        deltas = []

        # Define which metrics should decrease for improvement
        lower_is_better = {
            "pr_cycle_time_hours",
            "avg_review_iterations",
            "bug_count",
            "bug_reopen_rate",
            "pii_exposure_events",
        }

        categories = [
            ("productivity", self.current.get("productivity", {}), compare_to.get("productivity", {})),
            ("quality", self.current.get("quality", {}), compare_to.get("quality", {})),
            ("knowledge", self.current.get("knowledge", {}), compare_to.get("knowledge", {})),
            ("compliance", self.current.get("compliance", {}), compare_to.get("compliance", {})),
            ("adoption", self.current.get("adoption", {}), compare_to.get("adoption", {})),
        ]

        for category, current_cat, prev_cat in categories:
            for key, current_val in current_cat.items():
                if not isinstance(current_val, (int, float)) or current_val is None:
                    continue

                prev_val = prev_cat.get(key, 0) or 0
                if prev_val == 0:
                    continue

                delta = current_val - prev_val
                delta_pct = (delta / prev_val) * 100 if prev_val else 0

                # Determine if change is improvement
                if key in lower_is_better:
                    is_improvement = delta < 0
                else:
                    is_improvement = delta > 0

                deltas.append(MetricDelta(
                    name=key,
                    current=current_val,
                    previous=prev_val,
                    delta=round(delta, 2),
                    delta_percent=round(delta_pct, 1),
                    is_improvement=is_improvement,
                    category=category,
                ))

        return deltas

    def _generate_markdown(self) -> str:
        """Generate markdown report"""
        report_date = datetime.now().strftime("%B %Y")
        collected_at = self.current.get("collected_at", "Unknown")[:10]

        # Calculate deltas
        vs_baseline = self._calculate_deltas(self.baseline) if self.baseline else []
        vs_previous = self._calculate_deltas(self.previous) if self.previous else []

        # Build report
        lines = [
            f"# Claude Code Metrics Report - {report_date}",
            "",
            f"**Generated:** {collected_at}",
            f"**Period:** {self.current.get('period_start', 'N/A')[:10]} to {self.current.get('period_end', 'N/A')[:10]}",
            "",
            "---",
            "",
            "## Executive Summary",
            "",
        ]

        # Headline metrics
        prod = self.current.get("productivity", {})
        qual = self.current.get("quality", {})
        know = self.current.get("knowledge", {})
        adopt = self.current.get("adoption", {})

        lines.extend([
            "### Key Metrics",
            "",
            "| Metric | Current | vs Baseline |",
            "|--------|---------|-------------|",
        ])

        # Add key metrics with deltas
        key_metrics = [
            ("PR Cycle Time", f"{prod.get('pr_cycle_time_hours', 0)}h", "productivity", "pr_cycle_time_hours"),
            ("Active Developers", f"{prod.get('active_developers', 0)}/{prod.get('total_developers', 0)}", None, None),
            ("Security Blocks", str(qual.get("security_blocks_caught", 0)), "quality", "security_blocks_caught"),
            ("Patterns Created", str(know.get("patterns_count", 0)), "knowledge", "patterns_count"),
            ("Adoption Rate", f"{adopt.get('adoption_percentage', 0)}%", "adoption", "adoption_percentage"),
        ]

        for label, current_val, category, key in key_metrics:
            delta_str = "-"
            if category and key and vs_baseline:
                for d in vs_baseline:
                    if d.category == category and d.name == key:
                        arrow = "↓" if d.delta < 0 else "↑"
                        color = "🟢" if d.is_improvement else "🔴"
                        delta_str = f"{color} {arrow}{abs(d.delta_percent)}%"
                        break
            lines.append(f"| {label} | {current_val} | {delta_str} |")

        lines.extend([
            "",
            "---",
            "",
            "## Detailed Metrics",
            "",
        ])

        # Productivity section
        lines.extend([
            "### Productivity",
            "",
            "| Metric | Value | Change |",
            "|--------|-------|--------|",
        ])

        for key, label in [
            ("pr_cycle_time_hours", "PR Cycle Time (hours)"),
            ("prs_per_dev_per_week", "PRs/Dev/Week"),
            ("commits_per_dev_per_week", "Commits/Dev/Week"),
            ("avg_review_iterations", "Avg Review Iterations"),
        ]:
            val = prod.get(key, 0)
            delta_str = self._get_delta_str(vs_baseline, "productivity", key)
            lines.append(f"| {label} | {val:.1f} | {delta_str} |")

        # Quality section
        lines.extend([
            "",
            "### Quality",
            "",
            "| Metric | Value | Change |",
            "|--------|-------|--------|",
        ])

        for key, label in [
            ("security_blocks_caught", "Security Blocks"),
            ("pii_patterns_detected", "PII Patterns Detected"),
            ("bug_count", "Bug Count"),
            ("bug_reopen_rate", "Bug Reopen Rate (%)"),
        ]:
            val = qual.get(key, 0)
            delta_str = self._get_delta_str(vs_baseline, "quality", key)
            lines.append(f"| {label} | {val} | {delta_str} |")

        # Knowledge section
        lines.extend([
            "",
            "### Knowledge Flywheel",
            "",
            "| Metric | Value | Change |",
            "|--------|-------|--------|",
        ])

        for key, label in [
            ("learnings_count", "Learnings Captured"),
            ("patterns_count", "Patterns Created"),
            ("failures_documented", "Failures Documented"),
            ("pattern_references", "Pattern References"),
            ("avg_reuse_per_pattern", "Avg Reuse/Pattern"),
        ]:
            val = know.get(key, 0)
            delta_str = self._get_delta_str(vs_baseline, "knowledge", key)
            lines.append(f"| {label} | {val} | {delta_str} |")

        # Compliance section
        comp = self.current.get("compliance", {})
        lines.extend([
            "",
            "### Compliance",
            "",
            "| Metric | Value | Status |",
            "|--------|-------|--------|",
        ])

        pii_events = comp.get("pii_exposure_events", 0)
        pii_status = "✅ Clean" if pii_events == 0 else f"🔴 {pii_events} events"
        lines.append(f"| PII Exposure Events | {pii_events} | {pii_status} |")
        lines.append(f"| Secrets Blocked | {comp.get('secrets_blocked', 0)} | ✅ Prevented |")
        lines.append(f"| Dangerous Files Blocked | {comp.get('dangerous_files_blocked', 0)} | ✅ Prevented |")

        # ROI estimate
        lines.extend([
            "",
            "---",
            "",
            "## ROI Estimate",
            "",
        ])

        active_devs = prod.get("active_developers", 0)
        hours_saved_per_dev = 4  # Configurable assumption
        hourly_rate = 75  # Configurable

        monthly_hours = active_devs * hours_saved_per_dev * 4
        monthly_value = monthly_hours * hourly_rate

        lines.extend([
            f"**Assumptions:**",
            f"- Active developers: {active_devs}",
            f"- Hours saved per dev per week: {hours_saved_per_dev}",
            f"- Average hourly rate: ${hourly_rate}",
            "",
            f"**Estimated Monthly Value:** ${monthly_value:,.0f}",
            f"- Hours saved: {monthly_hours} hours/month",
            "",
        ])

        # Recommendations
        lines.extend([
            "---",
            "",
            "## Recommendations",
            "",
        ])

        recommendations = []

        # Check adoption
        if adopt.get("adoption_percentage", 0) < 80:
            recommendations.append("- 📈 **Increase Adoption**: Schedule training sessions for non-active developers")

        # Check flywheel
        if know.get("learnings_count", 0) < 10:
            recommendations.append("- 📚 **Activate Flywheel**: Remind team to use `/learn` after discoveries")

        if know.get("patterns_count", 0) > 0 and know.get("avg_reuse_per_pattern", 0) < 2:
            recommendations.append("- 🔄 **Promote Patterns**: Share existing patterns in standups")

        # Check compliance
        if comp.get("pii_exposure_events", 0) > 0:
            recommendations.append("- 🚨 **Address PII Events**: Review and remediate PII exposure incidents")

        if not recommendations:
            recommendations.append("- ✅ All metrics healthy - continue current practices")

        lines.extend(recommendations)

        lines.extend([
            "",
            "---",
            "",
            f"*Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        ])

        return "\n".join(lines)

    def _get_delta_str(self, deltas: list[MetricDelta], category: str, key: str) -> str:
        """Get formatted delta string for a metric"""
        if not deltas:
            return "-"

        for d in deltas:
            if d.category == category and d.name == key:
                arrow = "↓" if d.delta < 0 else "↑"
                sign = "+" if d.delta > 0 else ""
                emoji = "🟢" if d.is_improvement else ("🔴" if not d.is_improvement and abs(d.delta_percent) > 10 else "⚪")
                return f"{emoji} {sign}{d.delta_percent}%"

        return "-"

    def _generate_html(self) -> str:
        """Generate HTML report with styling"""
        markdown_content = self._generate_markdown()

        # Simple HTML wrapper with styling
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Claude Code Metrics Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            background: #f5f5f5;
        }}
        .report {{
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #1a1a1a; border-bottom: 2px solid #4f46e5; padding-bottom: 0.5rem; }}
        h2 {{ color: #374151; margin-top: 2rem; }}
        h3 {{ color: #4b5563; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e5e7eb;
        }}
        th {{ background: #f9fafb; font-weight: 600; }}
        tr:hover {{ background: #f9fafb; }}
        code {{ background: #f3f4f6; padding: 0.2rem 0.4rem; border-radius: 4px; }}
        hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }}
        .metric-good {{ color: #059669; }}
        .metric-bad {{ color: #dc2626; }}
    </style>
</head>
<body>
    <div class="report">
        <pre style="white-space: pre-wrap; font-family: inherit;">{markdown_content}</pre>
    </div>
</body>
</html>"""
        return html

    def _generate_json(self) -> str:
        """Generate JSON report"""
        vs_baseline = self._calculate_deltas(self.baseline) if self.baseline else []

        report = {
            "generated_at": datetime.now().isoformat(),
            "current_metrics": self.current,
            "baseline_comparison": [
                {
                    "metric": d.name,
                    "category": d.category,
                    "current": d.current,
                    "baseline": d.previous,
                    "delta": d.delta,
                    "delta_percent": d.delta_percent,
                    "is_improvement": d.is_improvement,
                }
                for d in vs_baseline
            ] if vs_baseline else None,
        }

        return json.dumps(report, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Generate Claude Code metrics report")
    parser.add_argument("current", nargs="?", default="metrics_current.json",
                        help="Path to current metrics JSON")
    parser.add_argument("--baseline", type=str, help="Path to baseline metrics JSON")
    parser.add_argument("--previous", type=str, help="Path to previous month metrics JSON")
    parser.add_argument("--format", choices=["markdown", "html", "json"], default="markdown")
    parser.add_argument("--output", type=str, help="Output file path")

    args = parser.parse_args()

    # Check if current metrics file exists
    if not Path(args.current).exists():
        print(f"Error: Current metrics file not found: {args.current}")
        print("\nTo generate metrics first, run:")
        print("  python collect_metrics.py --save metrics_current.json")
        return 1

    generator = ReportGenerator(
        current_metrics_path=args.current,
        baseline_metrics_path=args.baseline,
        previous_metrics_path=args.previous,
    )

    report = generator.generate_report(format=args.format)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)

    return 0


if __name__ == "__main__":
    exit(main())
