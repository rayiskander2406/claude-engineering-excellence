# Claude Code Usage Policy

> *"With great power comes great responsibility."*

This policy defines acceptable use of Claude Code across our organization. All team members using Claude Code must read and follow these guidelines.

**Effective Date:** [DATE]
**Last Updated:** [DATE]
**Policy Owner:** [ROLE/NAME]

---

## Quick Reference

| Category | Rule |
|----------|------|
| **Secrets** | NEVER paste API keys, passwords, tokens, or credentials |
| **PII** | NEVER paste customer data, emails, or personal information |
| **Proprietary** | OK to use with our code; NEVER paste competitor code |
| **Generated Code** | You own it, you review it, you're responsible for it |
| **Security Issues** | Report immediately; don't try to fix alone |

---

## 1. What You CAN Do

### Encouraged Uses

| Use Case | Examples |
|----------|----------|
| **Write code** | Features, bug fixes, refactoring |
| **Review code** | `/code-review`, security analysis |
| **Debug issues** | Error analysis, root cause investigation |
| **Write tests** | Unit tests, integration tests, E2E tests |
| **Documentation** | READMEs, API docs, architecture docs |
| **Learn** | Explain code, understand patterns |
| **Automate** | Scripts, CI/CD, infrastructure as code |
| **Research** | Technology evaluation, best practices |

### Allowed Data

| Data Type | Allowed? | Notes |
|-----------|----------|-------|
| Our source code | Yes | This is the primary use case |
| Open source code | Yes | Respect licenses |
| Error messages | Yes | Sanitize if they contain PII |
| Stack traces | Yes | Sanitize if they contain PII |
| Log snippets | Yes | **Remove PII/secrets first** |
| Architecture diagrams | Yes | Great for documentation |
| API contracts | Yes | OpenAPI specs, schemas |
| Test data (synthetic) | Yes | Use fake data, not real |

---

## 2. What You MUST NOT Do

### Never Share These With Claude

| Category | Examples | Risk |
|----------|----------|------|
| **Credentials** | API keys, passwords, tokens, certificates | Breach, unauthorized access |
| **Secrets** | `.env` contents, vault secrets, private keys | System compromise |
| **Customer PII** | Names, emails, addresses, phone numbers | Privacy violation, legal liability |
| **Financial Data** | Credit cards, bank accounts, SSNs | Regulatory violation |
| **Health Data** | Medical records, health information | HIPAA violation |
| **Production Data** | Real user data from databases | Privacy breach |
| **Competitor Code** | Code from other companies | Legal liability |
| **M&A Information** | Acquisition targets, deal terms | SEC violation |
| **Security Vulnerabilities** | Unpatched CVEs in our systems | Exploitation risk |

### Red Flags - Stop and Think

If you're about to paste something and you feel hesitation, **STOP**. Ask yourself:

1. Does this contain any real user data?
2. Does this contain any credentials or secrets?
3. Would I be comfortable if this appeared in a data breach?
4. Is this code I have the right to share?

**When in doubt, don't paste it.** Ask your tech lead or security team.

---

## 3. Code Ownership & Responsibility

### You Own What Claude Generates

```
┌─────────────────────────────────────────────────────────────┐
│                    RESPONSIBILITY CHAIN                     │
│                                                             │
│   Claude Generates Code                                     │
│            ↓                                                │
│   YOU Review It ← ← ← ← ← YOU are responsible here         │
│            ↓                                                │
│   YOU Commit It                                             │
│            ↓                                                │
│   YOU Own It Forever                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Your Responsibilities

| Responsibility | What This Means |
|----------------|-----------------|
| **Review all generated code** | Never commit without reading |
| **Test before committing** | Run tests, verify behavior |
| **Understand what it does** | Don't commit code you don't understand |
| **Security review** | Check for vulnerabilities |
| **License compliance** | Ensure no license violations |
| **Performance** | Verify it performs acceptably |

### What "Review" Means

Minimum review checklist before committing Claude-generated code:

```
[ ] I have read every line of generated code
[ ] I understand what the code does
[ ] I have tested it locally
[ ] I have checked for hardcoded values
[ ] I have checked for security issues (injection, XSS, etc.)
[ ] I would be comfortable defending this code in a code review
[ ] The code follows our team's standards
```

---

## 4. Security Requirements

### Before Using Claude on Security-Sensitive Code

| Code Type | Requirement |
|-----------|-------------|
| Authentication | Get security team review |
| Authorization | Get security team review |
| Cryptography | Get security team review |
| Payment processing | Get security team review |
| PII handling | Get security team review |
| Infrastructure | Get DevOps/security review |

### Reporting Security Issues

If Claude generates code with a security vulnerability:

1. **Don't commit it**
2. **Don't try to fix it yourself** (unless you're security-trained)
3. **Report to security team** via [CHANNEL]
4. **Document the issue** for team learning

If you discover Claude can be used to bypass security controls:

1. **Stop immediately**
2. **Report to security team** via [CHANNEL]
3. **Do not share the technique** with others

---

## 5. Data Classification

### What Can Be Shared With Claude

| Classification | Can Share? | Examples |
|----------------|------------|----------|
| **Public** | Yes | Open source code, public docs |
| **Internal** | Yes | Our source code, internal docs |
| **Confidential** | With caution | Remove secrets, sanitize PII |
| **Restricted** | No | Customer data, credentials, M&A |

### Sanitization Requirements

Before sharing logs, configs, or data with Claude:

```bash
# BAD - Contains secrets
DATABASE_URL=postgres://admin:SuperSecret123@prod.db.com:5432/users
API_KEY=sk-live-abc123xyz789

# GOOD - Sanitized
DATABASE_URL=postgres://[USER]:[PASSWORD]@[HOST]:5432/[DATABASE]
API_KEY=[REDACTED]
```

```bash
# BAD - Contains PII
Error: User john.doe@company.com failed to authenticate

# GOOD - Sanitized
Error: User [EMAIL] failed to authenticate
```

---

## 6. Approved Workflows

### Standard Development Workflow

```
1. Create feature branch
2. Use Claude for implementation
3. Review ALL generated code
4. Run tests locally
5. Commit with conventional commit message
6. Create PR with /pr-prep
7. Code review by human peer
8. Merge after approval
```

### Security-Sensitive Workflow

```
1. Create feature branch
2. Use Claude for implementation
3. Review ALL generated code
4. Run tests locally
5. Security self-review checklist
6. Request security team review
7. Address security feedback
8. Commit and create PR
9. Code review by human peer + security
10. Merge after all approvals
```

---

## 7. Prohibited Activities

### Explicitly Prohibited

| Activity | Reason |
|----------|--------|
| Bypassing code review | All code needs human review |
| Committing without testing | Quality requirement |
| Sharing credentials | Security violation |
| Using on competitor code | Legal risk |
| Generating malicious code | Ethical/legal violation |
| Automating spam/abuse | Ethical/legal violation |
| Circumventing security controls | Security violation |
| Bulk data extraction | May violate ToS |

### Disciplinary Actions

| Violation | Consequence |
|-----------|-------------|
| Accidental PII sharing | Training, documentation |
| Accidental secret exposure | Rotate secrets, training |
| Intentional policy violation | Disciplinary action |
| Repeated violations | Access revocation |
| Malicious use | Termination, legal action |

---

## 8. Best Practices

### Do

- Use `/code-review` before committing
- Use `/security-audit` on sensitive code
- Capture learnings with `/learn`
- Share patterns that work with `/promote`
- Ask Claude to explain code you don't understand
- Use synthetic/fake data for testing prompts

### Don't

- Blindly trust generated code
- Skip the review step
- Commit large changes without understanding them
- Use real customer data in prompts
- Share security vulnerabilities in prompts
- Assume Claude's security advice is complete

---

## 9. Incident Response

### If You Accidentally Share Sensitive Data

**Immediate actions:**

1. **Don't panic** - but act quickly
2. **Document what was shared** - screenshot if needed
3. **Report immediately** to:
   - Security team: [CONTACT]
   - Your manager: [CONTACT]
4. **Rotate any exposed credentials** immediately

**What happens next:**

- Security team assesses the risk
- Affected credentials are rotated
- Incident is documented
- No blame - focus on learning

### If You Find a Security Issue in Generated Code

1. Don't commit the code
2. Document the issue
3. Report to security team
4. Add to `.claude/failures/` for team learning

---

## 10. Compliance

### Regulatory Considerations

| Regulation | Requirement |
|------------|-------------|
| **GDPR** | No EU personal data in prompts |
| **HIPAA** | No health information in prompts |
| **PCI-DSS** | No cardholder data in prompts |
| **SOC 2** | Follow access controls, audit logging |
| **SOX** | Financial code requires additional review |

### Audit Trail

All Claude Code usage may be logged for:
- Security monitoring
- Compliance auditing
- Usage analytics

Assume your prompts can be reviewed by security/compliance teams.

---

## 11. Getting Help

### Questions About This Policy

- **Policy clarification:** [CONTACT]
- **Security questions:** [CONTACT]
- **Legal questions:** [CONTACT]

### Technical Help

- **Claude Code issues:** [CHANNEL]
- **MCP server problems:** [CHANNEL]
- **Best practices:** Check `FAQ.md` first

### Reporting Issues

- **Security incidents:** [CONTACT] (immediate)
- **Policy violations:** [CONTACT]
- **Suggestions:** [CHANNEL]

---

## 12. Metrics Visibility & Privacy

### Purpose of Metrics

Metrics exist to **improve our tools and processes**, not to evaluate individual performance. We measure adoption and impact to:
- Identify where teams need support
- Justify continued investment
- Celebrate collective wins
- Find opportunities to improve

### Visibility Tiers

| Audience | What They See | What They DON'T See |
|----------|---------------|---------------------|
| **Individual Developer** | Your own data only | Other individuals' data |
| **Tech Lead** | Team aggregates, project-level | Individual developer metrics |
| **Engineering Manager** | Org-wide aggregates, trends | Individual identifiable data |
| **Leadership/Execs** | High-level dashboard, ROI | Any individual or team breakdown |
| **Security/Compliance** | Compliance metrics only | Productivity or adoption data |

### What We Share Publicly (All Team)

- Overall adoption rate (e.g., "84% of team active")
- Total security blocks (e.g., "847 secrets caught")
- Flywheel health (e.g., "127 learnings, 18 patterns")
- Compliance status (e.g., "0 PII exposure events")
- Satisfaction survey aggregates

### What We NEVER Do

| Anti-Pattern | Why It's Prohibited |
|--------------|---------------------|
| Individual leaderboards | Creates unhealthy competition, gaming |
| Public "Claude usage" stats per person | Measures activity, not value |
| Naming individuals in reports | Creates blame culture |
| Tying metrics to performance reviews | Discourages honest adoption |
| Sharing individual PR cycle times | Penalizes complex, important work |

### Individual Privacy Rights

As a team member, you have the right to:

1. **See your own data** - Request your personal metrics anytime
2. **Understand aggregation** - Know how your data contributes to team metrics
3. **Opt out of surveys** - Participation is encouraged but voluntary
4. **Question methodology** - Challenge how metrics are calculated
5. **Context for outliers** - Explain unusual patterns in your data

### Using Metrics for Support, Not Punishment

Metrics may reveal that a team member or project needs help. The response is:

```
CORRECT RESPONSE:
"Project X has low flywheel engagement. Let's schedule training and
check if they have blockers."

WRONG RESPONSE:
"Developer Y has the lowest adoption rate. Put them on a PIP."
```

### Security & Compliance Metrics Exception

Security metrics (PII events, secrets blocked, audit findings) may be reported with more detail for compliance purposes. However:
- Individual attribution only shared with security team
- Focus is on remediation, not blame
- Root cause analysis is confidential
- Systemic issues lead to training, not punishment

### Data Retention

| Data Type | Retention Period |
|-----------|------------------|
| Aggregate metrics | Indefinite (for trend analysis) |
| Individual metrics | 12 months rolling |
| Survey responses | 12 months rolling |
| Security incidents | Per compliance requirements |

### Questions About Your Data

Contact [PRIVACY_CONTACT] if you want to:
- See your individual metrics
- Understand how data is aggregated
- Request correction of inaccurate data
- Understand how your data is used

---

## 13. Policy Updates

This policy will be reviewed quarterly and updated as needed.

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [DATE] | Initial policy |
| 1.1 | [DATE] | Added Metrics Visibility & Privacy section |

### Changelog

**v1.1** - Metrics Visibility
- Added Section 12: Metrics Visibility & Privacy
- Defined visibility tiers for different audiences
- Established individual privacy rights
- Prohibited anti-patterns (leaderboards, individual shaming)
- Added data retention guidelines

**v1.0** - Initial release
- Established acceptable use guidelines
- Defined data classification
- Set security requirements
- Created incident response procedures

---

## Acknowledgment

By using Claude Code, you acknowledge that you have read, understood, and agree to follow this policy.

Questions? Concerns? Reach out to [CONTACT] before proceeding.

---

*"Trust but verify. Claude is a powerful tool, but you are the engineer."*
