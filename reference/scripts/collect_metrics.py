#!/usr/bin/env python3
"""
Claude Code Metrics Collection Script

Collects adoption, productivity, quality, and knowledge metrics from:
- Git repositories
- GitHub API
- .claude/ directories
- Pre-commit hook logs
- JIRA/Linear (optional)

Usage:
    python collect_metrics.py                    # Collect current metrics
    python collect_metrics.py --baseline         # Collect baseline (pre-Claude)
    python collect_metrics.py --months=3         # Specify time range
    python collect_metrics.py --output=json      # Output format (json, csv, markdown)
"""

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
import urllib.request
import urllib.error


@dataclass
class ProductivityMetrics:
    """Productivity-related metrics"""
    pr_cycle_time_hours: float
    prs_per_dev_per_week: float
    avg_review_iterations: float
    commits_per_dev_per_week: float
    active_developers: int
    total_developers: int


@dataclass
class QualityMetrics:
    """Quality-related metrics"""
    bug_count: int
    bug_reopen_rate: float
    security_blocks_caught: int
    pii_patterns_detected: int
    test_coverage_avg: Optional[float]


@dataclass
class KnowledgeMetrics:
    """Knowledge flywheel metrics"""
    learnings_count: int
    patterns_count: int
    failures_documented: int
    pattern_references: int
    avg_reuse_per_pattern: float


@dataclass
class ComplianceMetrics:
    """Compliance and security metrics"""
    secrets_blocked: int
    pii_exposure_events: int
    dangerous_files_blocked: int
    security_antipatterns_warned: int


@dataclass
class AdoptionMetrics:
    """Claude Code adoption metrics"""
    projects_with_claude: int
    total_projects: int
    adoption_percentage: float
    starter_kit_usage: int


@dataclass
class AllMetrics:
    """Combined metrics report"""
    collected_at: str
    period_start: str
    period_end: str
    is_baseline: bool
    productivity: ProductivityMetrics
    quality: QualityMetrics
    knowledge: KnowledgeMetrics
    compliance: ComplianceMetrics
    adoption: AdoptionMetrics


class MetricsCollector:
    """Collects metrics from various sources"""

    def __init__(
        self,
        repo_paths: list[str],
        github_token: Optional[str] = None,
        github_org: Optional[str] = None,
        hook_log_path: Optional[str] = None,
        months: int = 1
    ):
        self.repo_paths = repo_paths
        self.github_token = github_token or os.environ.get("GITHUB_TOKEN")
        self.github_org = github_org or os.environ.get("GITHUB_ORG")
        self.hook_log_path = hook_log_path or os.path.expanduser("~/.claude-metrics/blocks.log")
        self.months = months
        self.since_date = datetime.now() - timedelta(days=30 * months)

    def collect_all(self, is_baseline: bool = False) -> AllMetrics:
        """Collect all metrics"""
        return AllMetrics(
            collected_at=datetime.now().isoformat(),
            period_start=self.since_date.isoformat(),
            period_end=datetime.now().isoformat(),
            is_baseline=is_baseline,
            productivity=self.collect_productivity(),
            quality=self.collect_quality(),
            knowledge=self.collect_knowledge(),
            compliance=self.collect_compliance(),
            adoption=self.collect_adoption(),
        )

    def collect_productivity(self) -> ProductivityMetrics:
        """Collect productivity metrics from Git and GitHub"""
        pr_cycle_time = self._get_pr_cycle_time()
        prs_merged = self._get_prs_merged()
        active_devs = self._get_active_developers()
        total_devs = self._get_total_developers()
        commits = self._get_commit_count()
        weeks = max(1, self.months * 4)

        return ProductivityMetrics(
            pr_cycle_time_hours=pr_cycle_time,
            prs_per_dev_per_week=prs_merged / max(1, active_devs) / weeks if active_devs else 0,
            avg_review_iterations=self._get_review_iterations(),
            commits_per_dev_per_week=commits / max(1, active_devs) / weeks if active_devs else 0,
            active_developers=active_devs,
            total_developers=total_devs,
        )

    def collect_quality(self) -> QualityMetrics:
        """Collect quality metrics"""
        hook_data = self._parse_hook_logs()

        return QualityMetrics(
            bug_count=self._get_bug_count(),
            bug_reopen_rate=self._get_bug_reopen_rate(),
            security_blocks_caught=hook_data.get("secrets", 0),
            pii_patterns_detected=hook_data.get("pii", 0),
            test_coverage_avg=self._get_test_coverage(),
        )

    def collect_knowledge(self) -> KnowledgeMetrics:
        """Collect knowledge flywheel metrics"""
        learnings = 0
        patterns = 0
        failures = 0
        references = 0

        for repo_path in self.repo_paths:
            claude_dir = Path(repo_path) / ".claude"
            if claude_dir.exists():
                learnings += self._count_files(claude_dir / "learnings")
                patterns += self._count_files(claude_dir / "patterns", exclude=[".gitkeep", "TEMPLATE.md"])
                failures += self._count_files(claude_dir / "failures", exclude=[".gitkeep", "TEMPLATE.md"])
                references += self._count_pattern_references(repo_path)

        avg_reuse = references / max(1, patterns) if patterns else 0

        return KnowledgeMetrics(
            learnings_count=learnings,
            patterns_count=patterns,
            failures_documented=failures,
            pattern_references=references,
            avg_reuse_per_pattern=round(avg_reuse, 2),
        )

    def collect_compliance(self) -> ComplianceMetrics:
        """Collect compliance metrics from hook logs"""
        hook_data = self._parse_hook_logs()

        return ComplianceMetrics(
            secrets_blocked=hook_data.get("secrets", 0),
            pii_exposure_events=hook_data.get("pii_exposed", 0),
            dangerous_files_blocked=hook_data.get("dangerous_files", 0),
            security_antipatterns_warned=hook_data.get("antipatterns", 0),
        )

    def collect_adoption(self) -> AdoptionMetrics:
        """Collect adoption metrics"""
        projects_with_claude = 0
        starter_kit_usage = 0

        for repo_path in self.repo_paths:
            claude_dir = Path(repo_path) / ".claude"
            if claude_dir.exists():
                projects_with_claude += 1
                # Check for starter kit markers
                if (claude_dir / "CLAUDE.md").exists():
                    starter_kit_usage += 1

        total = len(self.repo_paths)
        percentage = (projects_with_claude / total * 100) if total else 0

        return AdoptionMetrics(
            projects_with_claude=projects_with_claude,
            total_projects=total,
            adoption_percentage=round(percentage, 1),
            starter_kit_usage=starter_kit_usage,
        )

    # =========================================================================
    # Helper Methods - Git
    # =========================================================================

    def _get_active_developers(self) -> int:
        """Count developers with commits in the period"""
        developers = set()
        since = self.since_date.strftime("%Y-%m-%d")

        for repo_path in self.repo_paths:
            try:
                result = subprocess.run(
                    ["git", "log", f"--since={since}", "--format=%ae"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    developers.update(result.stdout.strip().split("\n"))
            except Exception:
                pass

        # Remove empty strings
        developers.discard("")
        return len(developers)

    def _get_total_developers(self) -> int:
        """Get total developers (from env or count all-time)"""
        total = os.environ.get("TOTAL_DEVELOPERS")
        if total:
            return int(total)

        # Fall back to counting all-time contributors
        developers = set()
        for repo_path in self.repo_paths:
            try:
                result = subprocess.run(
                    ["git", "log", "--format=%ae"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    developers.update(result.stdout.strip().split("\n"))
            except Exception:
                pass

        developers.discard("")
        return len(developers)

    def _get_commit_count(self) -> int:
        """Count commits in the period"""
        total = 0
        since = self.since_date.strftime("%Y-%m-%d")

        for repo_path in self.repo_paths:
            try:
                result = subprocess.run(
                    ["git", "rev-list", "--count", f"--since={since}", "HEAD"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    total += int(result.stdout.strip())
            except Exception:
                pass

        return total

    # =========================================================================
    # Helper Methods - GitHub API
    # =========================================================================

    def _github_request(self, endpoint: str) -> Optional[dict]:
        """Make GitHub API request"""
        if not self.github_token:
            return None

        url = f"https://api.github.com{endpoint}"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode())
        except urllib.error.URLError:
            return None

    def _get_pr_cycle_time(self) -> float:
        """Get average PR cycle time in hours"""
        if not self.github_token or not self.github_org:
            return 0.0

        total_hours = 0
        pr_count = 0
        since = self.since_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Get repos in org
        repos = self._github_request(f"/orgs/{self.github_org}/repos?per_page=100")
        if not repos:
            return 0.0

        for repo in repos[:10]:  # Limit to first 10 repos for speed
            prs = self._github_request(
                f"/repos/{self.github_org}/{repo['name']}/pulls?state=closed&per_page=50"
            )
            if not prs:
                continue

            for pr in prs:
                if pr.get("merged_at") and pr.get("created_at"):
                    created = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
                    merged = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))

                    if created >= self.since_date.replace(tzinfo=created.tzinfo):
                        hours = (merged - created).total_seconds() / 3600
                        total_hours += hours
                        pr_count += 1

        return round(total_hours / max(1, pr_count), 1)

    def _get_prs_merged(self) -> int:
        """Count merged PRs in period"""
        if not self.github_token or not self.github_org:
            return 0

        total = 0
        repos = self._github_request(f"/orgs/{self.github_org}/repos?per_page=100")
        if not repos:
            return 0

        for repo in repos[:10]:
            prs = self._github_request(
                f"/repos/{self.github_org}/{repo['name']}/pulls?state=closed&per_page=100"
            )
            if prs:
                for pr in prs:
                    if pr.get("merged_at"):
                        merged = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))
                        if merged >= self.since_date.replace(tzinfo=merged.tzinfo):
                            total += 1

        return total

    def _get_review_iterations(self) -> float:
        """Get average review iterations (comments before merge)"""
        # Simplified: would need to count review comments per PR
        return 0.0

    # =========================================================================
    # Helper Methods - Quality
    # =========================================================================

    def _get_bug_count(self) -> int:
        """Get bug count (requires JIRA/Linear integration)"""
        # Placeholder - implement with your issue tracker
        return 0

    def _get_bug_reopen_rate(self) -> float:
        """Get bug reopen rate (requires JIRA/Linear integration)"""
        # Placeholder - implement with your issue tracker
        return 0.0

    def _get_test_coverage(self) -> Optional[float]:
        """Get average test coverage"""
        # Placeholder - implement with your CI system
        return None

    # =========================================================================
    # Helper Methods - Files
    # =========================================================================

    def _count_files(self, directory: Path, exclude: list[str] = None) -> int:
        """Count files in directory"""
        if not directory.exists():
            return 0

        exclude = exclude or [".gitkeep"]
        count = 0

        for f in directory.iterdir():
            if f.is_file() and f.name not in exclude:
                count += 1

        return count

    def _count_pattern_references(self, repo_path: str) -> int:
        """Count references to patterns in code"""
        patterns_dir = Path(repo_path) / ".claude" / "patterns"
        if not patterns_dir.exists():
            return 0

        # Get pattern names
        pattern_names = []
        for f in patterns_dir.glob("*.md"):
            if f.name not in ["TEMPLATE.md", ".gitkeep"]:
                # Extract pattern name from file
                pattern_names.append(f.stem)

        if not pattern_names:
            return 0

        # Search for references in code
        total_refs = 0
        for pattern in pattern_names:
            try:
                result = subprocess.run(
                    ["grep", "-r", "-l", pattern, "--include=*.ts", "--include=*.tsx",
                     "--include=*.js", "--include=*.jsx", "--include=*.java",
                     "--include=*.cs", "--include=*.vue", "."],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    total_refs += len(result.stdout.strip().split("\n"))
            except Exception:
                pass

        return total_refs

    # =========================================================================
    # Helper Methods - Hook Logs
    # =========================================================================

    def _parse_hook_logs(self) -> dict:
        """Parse pre-commit hook logs"""
        log_path = Path(self.hook_log_path)
        if not log_path.exists():
            return {
                "secrets": 0,
                "pii": 0,
                "pii_exposed": 0,
                "dangerous_files": 0,
                "antipatterns": 0,
            }

        counts = {
            "secrets": 0,
            "pii": 0,
            "pii_exposed": 0,
            "dangerous_files": 0,
            "antipatterns": 0,
        }

        try:
            with open(log_path) as f:
                for line in f:
                    if not line.strip():
                        continue

                    # Expected format: timestamp,user,event_type
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        event_type = parts[2].upper()
                        if "SECRET" in event_type:
                            counts["secrets"] += 1
                        elif "PII" in event_type:
                            counts["pii"] += 1
                        elif "DANGEROUS" in event_type:
                            counts["dangerous_files"] += 1
                        elif "ANTIPATTERN" in event_type:
                            counts["antipatterns"] += 1
        except Exception:
            pass

        return counts


def format_output(metrics: AllMetrics, format: str) -> str:
    """Format metrics for output"""
    if format == "json":
        return json.dumps(asdict(metrics), indent=2)

    elif format == "markdown":
        return f"""# Claude Code Metrics Report

**Period:** {metrics.period_start[:10]} to {metrics.period_end[:10]}
**Collected:** {metrics.collected_at[:10]}
**Type:** {"Baseline" if metrics.is_baseline else "Current"}

## Adoption

| Metric | Value |
|--------|-------|
| Projects with Claude | {metrics.adoption.projects_with_claude}/{metrics.adoption.total_projects} |
| Adoption Rate | {metrics.adoption.adoption_percentage}% |
| Starter Kit Usage | {metrics.adoption.starter_kit_usage} |

## Productivity

| Metric | Value |
|--------|-------|
| PR Cycle Time | {metrics.productivity.pr_cycle_time_hours} hours |
| PRs/Dev/Week | {metrics.productivity.prs_per_dev_per_week:.1f} |
| Commits/Dev/Week | {metrics.productivity.commits_per_dev_per_week:.1f} |
| Active Developers | {metrics.productivity.active_developers}/{metrics.productivity.total_developers} |

## Quality

| Metric | Value |
|--------|-------|
| Security Blocks | {metrics.quality.security_blocks_caught} |
| PII Patterns Detected | {metrics.quality.pii_patterns_detected} |
| Bug Count | {metrics.quality.bug_count} |
| Bug Reopen Rate | {metrics.quality.bug_reopen_rate}% |

## Knowledge Flywheel

| Metric | Value |
|--------|-------|
| Learnings | {metrics.knowledge.learnings_count} |
| Patterns | {metrics.knowledge.patterns_count} |
| Failures Documented | {metrics.knowledge.failures_documented} |
| Pattern References | {metrics.knowledge.pattern_references} |
| Avg Reuse/Pattern | {metrics.knowledge.avg_reuse_per_pattern}x |

## Compliance

| Metric | Value |
|--------|-------|
| Secrets Blocked | {metrics.compliance.secrets_blocked} |
| PII Exposure Events | {metrics.compliance.pii_exposure_events} |
| Dangerous Files Blocked | {metrics.compliance.dangerous_files_blocked} |
"""

    else:  # csv
        lines = ["metric,value"]
        for category, data in [
            ("adoption", metrics.adoption),
            ("productivity", metrics.productivity),
            ("quality", metrics.quality),
            ("knowledge", metrics.knowledge),
            ("compliance", metrics.compliance),
        ]:
            for key, value in asdict(data).items():
                lines.append(f"{category}.{key},{value}")
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Collect Claude Code metrics")
    parser.add_argument("--baseline", action="store_true", help="Collect baseline metrics")
    parser.add_argument("--months", type=int, default=1, help="Months of history to analyze")
    parser.add_argument("--output", choices=["json", "csv", "markdown"], default="json")
    parser.add_argument("--repos", nargs="+", help="Repository paths to analyze")
    parser.add_argument("--save", type=str, help="Save output to file")

    args = parser.parse_args()

    # Default to current directory if no repos specified
    repo_paths = args.repos or [os.getcwd()]

    collector = MetricsCollector(
        repo_paths=repo_paths,
        months=args.months,
    )

    metrics = collector.collect_all(is_baseline=args.baseline)
    output = format_output(metrics, args.output)

    if args.save:
        with open(args.save, "w") as f:
            f.write(output)
        print(f"Metrics saved to {args.save}")
    else:
        print(output)


if __name__ == "__main__":
    main()
