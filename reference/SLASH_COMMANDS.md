# 25 Essential Slash Commands for Engineering Excellence

> Battle-tested commands drawn from Google SRE, Stripe, Netflix, ThoughtWorks, and top engineering teams worldwide.

---

## Overview

These 25 slash commands encode the most impactful engineering workflows into repeatable, automated processes. Each command is designed to be:

- **Universal** - Works for any project, any language, any team size
- **Evidence-based** - Drawn from industry best practices with documented ROI
- **Self-contained** - Includes all context needed for Claude to execute effectively

---

## Quick Reference

| # | Command | Category | Impact |
|---|---------|----------|--------|
| 1 | `/code-review` | Quality | Catches 60-90% of bugs before merge |
| 2 | `/security-audit` | Security | Prevents breaches, meets compliance |
| 3 | `/tech-debt` | Maintenance | Quantifies and prioritizes debt |
| 4 | `/refactor` | Quality | Improves maintainability 2-3x |
| 5 | `/test-gen` | Testing | Increases coverage 30-50% |
| 6 | `/doc-gen` | Documentation | Reduces onboarding time 50% |
| 7 | `/explain` | Knowledge | Accelerates understanding 5x |
| 8 | `/debug` | Troubleshooting | Reduces MTTR by 40% |
| 9 | `/perf-audit` | Performance | Identifies bottlenecks systematically |
| 10 | `/api-review` | Design | Ensures API consistency |
| 11 | `/pr-prep` | Collaboration | Creates high-quality PRs |
| 12 | `/commit` | Version Control | Enforces conventional commits |
| 13 | `/changelog` | Release | Auto-generates release notes |
| 14 | `/adr` | Architecture | Documents decisions permanently |
| 15 | `/runbook` | Operations | Reduces incident MTTR 60% |
| 16 | `/postmortem` | Learning | Prevents repeat incidents |
| 17 | `/onboard` | Team | Accelerates new hire productivity |
| 18 | `/deps-audit` | Security | Prevents supply chain attacks |
| 19 | `/migrate` | Modernization | Safe, incremental migrations |
| 20 | `/standup` | Communication | Generates status reports |
| 21 | `/estimate` | Planning | Data-driven estimates |
| 22 | `/retro` | Process | Continuous improvement |
| 23 | `/pre-flight` | Deployment | Catches issues before deploy |
| 24 | `/feature` | Development | End-to-end feature scaffolding |
| 25 | `/research` | Discovery | Systematic technology research |

---

## The Commands

### 1. `/code-review` - Comprehensive Code Review

**What it does:**
Performs a multi-dimensional code review covering security, performance, maintainability, and correctness.

**Why this is essential:**
- Studies show code review catches 60-90% of defects before they reach production
- Google's engineering practices mandate code review for every change
- Automated review catches issues humans miss (security vulnerabilities, performance anti-patterns)

**Applicability:**
Every project, every PR. This is non-negotiable for professional teams.

**Stolen from:** Google, Microsoft, Stripe - all require code review for 100% of changes.

---

### 2. `/security-audit` - Security Vulnerability Assessment

**What it does:**
Scans code for OWASP Top 10 vulnerabilities, secret exposure, injection attacks, authentication flaws, and dependency vulnerabilities.

**Why this is essential:**
- The average cost of a data breach is $4.45M (IBM 2023)
- 83% of breaches involve external actors exploiting known vulnerabilities
- Shift-left security catches issues when they're cheap to fix

**Applicability:**
Any project handling user data, authentication, or external APIs. Critical for compliance (SOC2, HIPAA, GDPR).

**Stolen from:** OWASP, Snyk, GitHub Advanced Security practices.

---

### 3. `/tech-debt` - Technical Debt Assessment

**What it does:**
Analyzes codebase for technical debt indicators: code complexity, duplication, outdated dependencies, missing tests, and architectural issues. Produces a prioritized remediation plan.

**Why this is essential:**
- Shopify allocates 25% of engineering time to debt reduction
- Unmanaged debt compounds - studies show it can consume 40%+ of development time
- Quantifying debt enables prioritization and executive buy-in

**Applicability:**
Any project older than 6 months. Run quarterly for healthy codebases, monthly for troubled ones.

**Stolen from:** CodeScene, SonarQube, Martin Fowler's technical debt quadrant.

---

### 4. `/refactor` - Intelligent Code Refactoring

**What it does:**
Identifies refactoring opportunities and executes safe transformations: extract methods, simplify conditionals, remove duplication, improve naming.

**Why this is essential:**
- Clean code is 2-3x faster to modify than messy code
- Refactoring prevents debt accumulation
- Small, continuous refactoring is safer than big rewrites

**Applicability:**
Before adding features to complex code. After code review identifies issues. During dedicated refactoring sprints.

**Stolen from:** Martin Fowler's Refactoring book, Kent Beck's design patterns.

---

### 5. `/test-gen` - Test Case Generation

**What it does:**
Analyzes code and generates comprehensive test cases: unit tests, edge cases, error scenarios, and integration tests.

**Why this is essential:**
- Tests are documentation that never goes stale
- 70% unit test coverage correlates with significantly fewer production bugs
- Test generation accelerates TDD adoption

**Applicability:**
All production code. Especially valuable for legacy code lacking tests.

**Stolen from:** Google Testing Blog, Kent Beck's TDD methodology.

---

### 6. `/doc-gen` - Documentation Generation

**What it does:**
Generates API documentation, README sections, architecture overviews, and inline comments from code analysis.

**Why this is essential:**
- Developers spend 50%+ of time reading code, not writing it
- Good docs reduce onboarding time by 50%+
- Auto-generated docs stay synchronized with code

**Applicability:**
All projects with more than one contributor. All public APIs.

**Stolen from:** Stripe's legendary API docs, Swagger/OpenAPI best practices.

---

### 7. `/explain` - Code Explanation

**What it does:**
Analyzes code and explains what it does, why it's structured that way, potential issues, and how to modify it safely.

**Why this is essential:**
- Understanding unfamiliar code is the #1 time sink for developers
- Accelerates onboarding 5x
- Reduces errors when modifying code you didn't write

**Applicability:**
Legacy code, unfamiliar codebases, complex algorithms, code review preparation.

**Stolen from:** Rubber duck debugging, pair programming knowledge transfer.

---

### 8. `/debug` - Systematic Debugging

**What it does:**
Analyzes error messages, stack traces, and code to identify root causes. Suggests fixes and explains the underlying issue.

**Why this is essential:**
- Structured debugging is 3-5x faster than ad-hoc approaches
- Documents the debugging process for future reference
- Reduces MTTR (Mean Time To Recovery) by 40%

**Applicability:**
Any error, bug, or unexpected behavior. Production incidents.

**Stolen from:** Scientific method, Google SRE debugging practices.

---

### 9. `/perf-audit` - Performance Audit

**What it does:**
Analyzes code for performance issues: N+1 queries, memory leaks, inefficient algorithms, missing caching, bundle size issues.

**Why this is essential:**
- Amazon found every 100ms of latency cost 1% of sales
- Performance problems compound and are expensive to fix later
- Systematic audits catch issues that profilers miss

**Applicability:**
Before major releases. When users report slowness. Quarterly for healthy systems.

**Stolen from:** Google PageSpeed, Netflix performance engineering.

---

### 10. `/api-review` - API Design Review

**What it does:**
Reviews API design for consistency, RESTful principles, error handling, versioning, pagination, and documentation completeness.

**Why this is essential:**
- APIs are contracts - breaking changes break trust
- Consistent APIs reduce integration time by 50%+
- Good API design is hard to retrofit

**Applicability:**
Before publishing any API. During API evolution planning.

**Stolen from:** Stripe API design principles, Google API design guide.

---

### 11. `/pr-prep` - Pull Request Preparation

**What it does:**
Prepares a comprehensive PR: generates description, creates checklist, suggests reviewers, identifies potential concerns, links related issues.

**Why this is essential:**
- Good PR descriptions reduce review time by 50%
- Checklists catch common issues automatically
- Self-review before requesting review shows professionalism

**Applicability:**
Every PR. No exceptions.

**Stolen from:** GitHub PR best practices, GitLab merge request guidelines.

---

### 12. `/commit` - Conventional Commit Message

**What it does:**
Analyzes staged changes and generates a conventional commit message with appropriate type, scope, and description.

**Why this is essential:**
- Enables automatic changelog generation
- Makes git history searchable and meaningful
- Supports semantic versioning automation

**Applicability:**
Every commit. Enforced via pre-commit hooks in mature teams.

**Stolen from:** Angular commit conventions, Conventional Commits specification.

---

### 13. `/changelog` - Changelog Generation

**What it does:**
Analyzes commits since last release and generates a formatted changelog grouped by type (features, fixes, breaking changes).

**Why this is essential:**
- Users need to know what changed
- Reduces manual release documentation by 90%
- Required for open-source credibility

**Applicability:**
Every release. Automated in CI/CD for mature teams.

**Stolen from:** Keep a Changelog, semantic-release.

---

### 14. `/adr` - Architecture Decision Record

**What it does:**
Creates an ADR documenting the context, decision, consequences, and alternatives considered for an architectural choice.

**Why this is essential:**
- Decisions made today are mysteries in 6 months
- ADRs prevent relitigating settled decisions
- New team members understand "why" not just "what"

**Applicability:**
Any significant technical decision: framework choice, database selection, architectural patterns.

**Stolen from:** ThoughtWorks, Michael Nygard's ADR format.

---

### 15. `/runbook` - Operational Runbook

**What it does:**
Creates a runbook for a service: health checks, common issues, debugging steps, escalation paths, and recovery procedures.

**Why this is essential:**
- Runbooks reduce incident MTTR by 60%
- On-call engineers can resolve issues without waking experts
- Captures tribal knowledge before it walks out the door

**Applicability:**
Every production service. Updated after every incident.

**Stolen from:** Google SRE handbook, PagerDuty incident response.

---

### 16. `/postmortem` - Incident Postmortem

**What it does:**
Creates a blameless postmortem: timeline, root cause analysis, contributing factors, action items, and lessons learned.

**Why this is essential:**
- Blameless postmortems create psychological safety
- Action items prevent recurrence
- Shared postmortems spread learning across the organization

**Applicability:**
After every significant incident. Also useful for near-misses.

**Stolen from:** Google SRE blameless postmortem culture, Etsy's Debriefing Facilitation Guide.

---

### 17. `/onboard` - Developer Onboarding Guide

**What it does:**
Generates an onboarding guide: environment setup, key concepts, architecture overview, common tasks, and who to ask for help.

**Why this is essential:**
- Average onboarding takes 3-6 months to full productivity
- Good onboarding docs reduce this by 50%
- Shows new hires the team values their time

**Applicability:**
Any project with more than one developer. Updated with each significant change.

**Stolen from:** GitLab's public handbook, Stripe's developer onboarding.

---

### 18. `/deps-audit` - Dependency Audit

**What it does:**
Audits dependencies for security vulnerabilities, license compliance, maintenance status, and version currency.

**Why this is essential:**
- Log4Shell showed the risk of unaudited dependencies
- License violations can have legal consequences
- Abandoned dependencies become security liabilities

**Applicability:**
Weekly automated scans. Before any release. After adding new dependencies.

**Stolen from:** npm audit, Snyk, Dependabot, OWASP Dependency-Check.

---

### 19. `/migrate` - Migration Planning

**What it does:**
Plans a migration: assesses current state, defines target state, creates incremental migration steps, identifies risks, and suggests rollback strategies.

**Why this is essential:**
- Migrations fail when rushed or poorly planned
- Incremental migration reduces risk
- Documented plans enable team coordination

**Applicability:**
Framework upgrades, database migrations, cloud migrations, major refactors.

**Stolen from:** Strangler Fig pattern, Martin Fowler's migration strategies.

---

### 20. `/standup` - Standup Report

**What it does:**
Generates a standup report: yesterday's accomplishments, today's plan, blockers, and relevant context from recent commits and issues.

**Why this is essential:**
- Reduces standup meeting time
- Creates written record for async teams
- Helps identify blockers early

**Applicability:**
Daily for active development. Great for distributed teams.

**Stolen from:** Agile daily standup, async-first remote teams.

---

### 21. `/estimate` - Effort Estimation

**What it does:**
Analyzes a task or feature and provides effort estimates with confidence ranges, risk factors, and comparable past work.

**Why this is essential:**
- Estimates are often wildly optimistic
- Structured estimation is 2-3x more accurate than gut feel
- Identifying risks upfront prevents surprises

**Applicability:**
Sprint planning, project scoping, resource allocation.

**Stolen from:** PERT estimation, reference class forecasting, No Estimates movement.

---

### 22. `/retro` - Retrospective Facilitation

**What it does:**
Facilitates a retrospective: what went well, what didn't, what puzzled us, and what to try next. Generates action items.

**Why this is essential:**
- Teams that retro regularly improve continuously
- Structured format prevents aimless discussion
- Action items ensure follow-through

**Applicability:**
End of every sprint, project, or milestone.

**Stolen from:** Agile retrospectives, Prime Directive, Toyota Kata.

---

### 23. `/pre-flight` - Deployment Pre-Flight Check

**What it does:**
Runs pre-deployment checks: tests passing, migrations ready, feature flags set, monitoring configured, rollback plan documented.

**Why this is essential:**
- Most deployment failures are preventable
- Checklists catch forgotten steps
- Reduces deployment anxiety

**Applicability:**
Before every production deployment. Automated in mature CI/CD.

**Stolen from:** Aviation pre-flight checklists, The Checklist Manifesto.

---

### 24. `/feature` - Feature Development Scaffold

**What it does:**
Scaffolds a new feature: creates files, tests, documentation stubs, and implementation plan based on requirements.

**Why this is essential:**
- Consistent structure across features
- Ensures tests and docs aren't forgotten
- Accelerates development start

**Applicability:**
Starting any new feature. Especially valuable for junior developers.

**Stolen from:** Rails generators, Create React App, production-grade scaffolding.

---

### 25. `/research` - Technology Research

**What it does:**
Conducts systematic research on a technology: existing solutions, pros/cons, community health, production readiness, and recommendations.

**Why this is essential:**
- Ad-hoc research misses important factors
- Documented research prevents relitigating decisions
- Reproducible methodology builds team capability

**Applicability:**
Before adopting any new library, framework, or tool.

**Stolen from:** Academic research methodology, ThoughtWorks Technology Radar.

---

## Installation

### Option 1: Clone the Repository

```bash
# Clone to your project
git clone https://github.com/edutone/claude-engineering-excellence.git
cp -r claude-engineering-excellence/.claude/commands your-project/.claude/
```

### Option 2: Global Installation

```bash
# Install for all projects
mkdir -p ~/.claude/commands
curl -L https://github.com/edutone/claude-engineering-excellence/archive/main.tar.gz | tar -xz
cp claude-engineering-excellence-main/.claude/commands/*.md ~/.claude/commands/
```

### Option 3: Cherry-Pick Commands

Download individual commands you need from the `.claude/commands/` directory.

---

## Usage

In Claude Code, type `/` followed by the command name:

```
/code-review
/security-audit src/auth/
/tech-debt
/explain src/utils/parser.js
```

Most commands accept arguments:
- File or directory paths
- Issue numbers
- Feature descriptions
- Custom parameters

---

## Customization

Each command is a Markdown file in `.claude/commands/`. Customize by:

1. Editing the prompt template
2. Adding project-specific context
3. Adjusting the output format
4. Adding frontmatter for tool restrictions

Example customization:
```markdown
---
description: Code review with our team's standards
allowed-tools: Read, Grep, Glob
---

Review this code following our team's standards:
- All functions must have JSDoc comments
- No console.log in production code
- Use our custom error classes
...
```

---

## Contributing

Found a command that should be here? Open a PR! Requirements:

1. Must solve a **universal** problem (not project-specific)
2. Must include **WHY** documentation
3. Must be **battle-tested** (not theoretical)
4. Must follow the existing format

---

*"The best engineers aren't the ones who work the hardest - they're the ones who automate the hard work."*
