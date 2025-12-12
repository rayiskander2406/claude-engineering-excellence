# Claude Code Metrics Framework

> Measuring what matters: Productivity, Quality, Knowledge, Compliance

---

## Why Measure?

Without metrics, you can't answer:
- Is Claude Code actually helping?
- Is the Self-Learning Flywheel working?
- Are we staying compliant?
- What's the ROI for leadership?

This framework gives you **actionable data** without drowning in vanity metrics.

---

## The Four Pillars

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    PRODUCTIVITY        QUALITY         KNOWLEDGE    COMPLIANCE  │
│    ────────────        ───────         ─────────    ──────────  │
│    Are we faster?      Is code         Is the       Are we      │
│                        better?         flywheel     secure?     │
│                                        working?                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Metric Definitions

### Pillar 1: Productivity

| Metric | Definition | Target | Collection |
|--------|------------|--------|------------|
| **PR Cycle Time** | Hours from PR open to merge | ↓30% from baseline | GitHub API |
| **PRs Per Dev Per Week** | Merged PRs / active devs / week | ↑20% from baseline | GitHub API |
| **First Commit Time** | Days from onboarding to first merged PR | <3 days | Manual tracking |
| **Review Iterations** | Comments/changes before approval | <2 rounds avg | GitHub API |

**Why these matter:**
- PR Cycle Time = end-to-end delivery speed
- PRs Per Week = shipping velocity
- First Commit Time = onboarding effectiveness
- Review Iterations = code quality at submission

---

### Pillar 2: Quality

| Metric | Definition | Target | Collection |
|--------|------------|--------|------------|
| **Bug Reopen Rate** | % of bugs reopened within 30 days | <10% | JIRA/Linear |
| **Production Incidents** | P1/P2 incidents per month | ↓25% from baseline | Incident tracker |
| **Security Findings** | Vulnerabilities in quarterly audit | ↓50% from baseline | Security audit |
| **Test Coverage Delta** | Coverage change on AI-assisted code | ≥0% (no decrease) | CI pipeline |

**Why these matter:**
- Bug Reopen = fix quality
- Incidents = real-world impact
- Security Findings = compliance posture
- Test Coverage = sustainable quality

---

### Pillar 3: Knowledge (Flywheel)

| Metric | Definition | Target | Collection |
|--------|------------|--------|------------|
| **Learnings Created** | New entries in `.claude/learnings/` | +10/month | File count |
| **Patterns Promoted** | Learnings → patterns conversion | +2/month | File count |
| **Pattern Reuse Rate** | Times patterns referenced in code | 3x per pattern | Grep analysis |
| **Knowledge Search Rate** | `/search-knowledge` usage | +20%/month | Command logs |

**Why these matter:**
- Learnings Created = capture is happening
- Patterns Promoted = quality knowledge emerging
- Pattern Reuse = knowledge is compounding
- Search Rate = team is using the system

---

### Pillar 4: Compliance

| Metric | Definition | Target | Collection |
|--------|------------|--------|------------|
| **Pre-commit Blocks** | Secrets/PII caught before commit | Track trend | Hook logs |
| **PII Exposure Events** | Student data in logs/errors | 0 | Audit |
| **Compliance Audit Score** | External audit results | 100% | Quarterly audit |
| **Security Training Completion** | Team completed EdTech training | 100% | LMS |

**Why these matter:**
- Pre-commit Blocks = defense working
- PII Events = FERPA/COPPA compliance
- Audit Score = regulatory readiness
- Training = human layer of defense

---

## Collection Schedule

| Frequency | Metrics | Owner |
|-----------|---------|-------|
| **Real-time** | Pre-commit blocks | Automated |
| **Daily** | PR cycle time, commits | Automated |
| **Weekly** | Flywheel counts, adoption | Tech Lead |
| **Monthly** | Full report, satisfaction survey | Engineering Manager |
| **Quarterly** | Compliance audit, trend analysis | Security + Leadership |

---

## Baseline Requirements

Before rollout, capture 3 months of historical data:

```bash
# Run baseline collection
python scripts/collect_metrics.py --baseline --months=3

# Outputs:
# - baseline_productivity.json
# - baseline_quality.json
# - baseline_velocity.json
```

**Critical:** Without baseline, you can't prove improvement.

---

## Dashboard Layout

```
╔═══════════════════════════════════════════════════════════════════════╗
║                    CLAUDE CODE ADOPTION DASHBOARD                      ║
║                         December 2024                                  ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  ADOPTION                          TREND                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                  ║
║  Active Users: 42/50 (84%)         ████████████████████░░░░            ║
║  Projects: 12/15 (80%)             Week 1 ──────────────► Week 8       ║
║                                                                        ║
║  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        ║
║  │  PRODUCTIVITY   │  │     QUALITY     │  │   KNOWLEDGE     │        ║
║  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤        ║
║  │ PR Cycle: 4.2h  │  │ Bugs: -23%      │  │ Learnings: 127  │        ║
║  │ (was 6.1h) ↓31% │  │ Incidents: -18% │  │ Patterns: 18    │        ║
║  │                 │  │ Sec Blocks: 847 │  │ Reuse: 3.2x     │        ║
║  │ PRs/wk: +22%    │  │                 │  │                 │        ║
║  └─────────────────┘  └─────────────────┘  └─────────────────┘        ║
║                                                                        ║
║  COMPLIANCE                        SATISFACTION                        ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                  ║
║  PII Leaks: 0        ✓             NPS: 72                             ║
║  Audit Score: 100%   ✓             Avg Rating: 8.2/10                  ║
║  Training: 50/50     ✓             "Saves me 2+ hrs/day" - 68%        ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## Satisfaction Survey (Monthly)

Run a 2-minute survey monthly:

### Questions

1. **Overall satisfaction with Claude Code** (1-10)
2. **Hours saved per week** (0, 1-2, 2-4, 4+)
3. **Most valuable feature** (Multiple choice)
   - Code generation
   - Code review assistance
   - Bug fixing
   - Learning from patterns
   - Documentation
4. **Biggest frustration** (Open text)
5. **Would you recommend to a colleague?** (NPS: 0-10)

### Tracking

```
Month    NPS    Avg Rating    Response Rate
─────    ───    ──────────    ─────────────
Oct      58     7.4           82%
Nov      65     7.8           88%
Dec      72     8.2           91%
```

---

## Anti-Metrics (Do NOT Track)

| Metric | Why It's Harmful |
|--------|------------------|
| **Lines of code** | Incentivizes bloat |
| **Commits per day** | Incentivizes small, meaningless commits |
| **Claude session count** | More sessions ≠ more value |
| **"AI-written" percentage** | Unmeasurable, creates wrong incentives |
| **Time in Claude** | Longer ≠ better |

---

## Reporting to Leadership

### Monthly Executive Summary

```markdown
## Claude Code - Month X Summary

### Headline Metrics
- **Productivity**: PR cycle time ↓31% (6.1h → 4.2h)
- **Quality**: Production bugs ↓23%
- **Compliance**: 0 PII exposure events, 847 secrets blocked
- **Adoption**: 84% of team active

### ROI Estimate
- Hours saved: ~168 hrs/month (42 devs × 4 hrs/week)
- At $75/hr average: **$12,600/month value**
- Tool cost: $X/month
- **Net ROI: $Y/month**

### Risks & Actions
- 8 developers not yet active → Schedule training
- Pattern reuse below target → Promote in standups
```

---

## Getting Started

1. **Run baseline collection**
   ```bash
   python scripts/collect_metrics.py --baseline
   ```

2. **Enable hook logging**
   ```bash
   # Already configured in STARTER_KIT pre-commit hook
   ```

3. **Schedule monthly survey**
   - Use Google Forms, Typeform, or similar
   - Send first Monday of each month

4. **Set up dashboard**
   - Use provided template
   - Connect to GitHub API, JIRA/Linear

5. **First report at 30 days**
   ```bash
   python scripts/generate_report.py --month=1
   ```

---

## Files in This Package

| File | Purpose |
|------|---------|
| `METRICS.md` | This guide |
| `scripts/collect_metrics.py` | Automated metric collection |
| `scripts/generate_report.py` | Monthly report generator |
| `templates/dashboard.html` | Interactive dashboard |
| `templates/survey.md` | Monthly survey questions |

---

*"What gets measured gets managed. What gets managed gets improved."*
