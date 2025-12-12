---
description: Create blameless incident postmortem
---

# Incident Postmortem

Create a blameless postmortem following Google SRE best practices.

## Postmortem Template

```markdown
# Incident Postmortem: [Title]

**Date**: [YYYY-MM-DD]
**Authors**: [Names]
**Status**: Draft | In Review | Final
**Incident Severity**: SEV-1 | SEV-2 | SEV-3

## Executive Summary

[2-3 sentence summary: What happened, impact, root cause, current status]

## Impact

**Duration**: [Start time] to [End time] ([X] hours [Y] minutes)
**User Impact**: [Number of users affected, what they experienced]
**Revenue Impact**: [If applicable]
**SLA Impact**: [If applicable]

## Timeline

All times in UTC.

| Time | Event |
|------|-------|
| HH:MM | First alert fired |
| HH:MM | On-call acknowledged |
| HH:MM | Initial investigation started |
| HH:MM | Root cause identified |
| HH:MM | Mitigation applied |
| HH:MM | Service restored |
| HH:MM | All-clear declared |

## Root Cause

[Detailed technical explanation of what caused the incident]

## Contributing Factors

1. [Factor 1 - e.g., Missing monitoring]
2. [Factor 2 - e.g., Inadequate testing]
3. [Factor 3 - e.g., Documentation gap]

## Detection

**How was the incident detected?**
- [ ] Automated alert
- [ ] Customer report
- [ ] Internal report
- [ ] Other: [specify]

**Detection gap**: [Time between incident start and detection]

## Response

**What went well**:
- [List things that worked]

**What could be improved**:
- [List things that didn't work well]

## Action Items

| ID | Action | Owner | Priority | Due Date | Status |
|----|--------|-------|----------|----------|--------|
| 1 | | | P0/P1/P2 | | Open |
| 2 | | | | | Open |

### Categorized Actions

**Prevent recurrence**:
- [ ] [Specific action to prevent this exact issue]

**Improve detection**:
- [ ] [Better monitoring/alerting]

**Improve response**:
- [ ] [Runbook updates, training]

**Improve process**:
- [ ] [Systemic improvements]

## Lessons Learned

### What we learned
1. [Key insight 1]
2. [Key insight 2]

### What we'll do differently
1. [Change 1]
2. [Change 2]

## Supporting Information

- **Incident ticket**: [Link]
- **Slack channel**: [Link]
- **Related dashboards**: [Links]
- **Relevant logs**: [Links or queries]

---

*This postmortem follows the blameless postmortem philosophy: we focus on systems and processes, not individuals.*
```

## Blameless Postmortem Principles

1. **Focus on systems, not people**: Ask "what" and "how", not "who"
2. **Assume good intentions**: Everyone was trying to do the right thing
3. **Seek understanding, not blame**: Learn, don't punish
4. **Be thorough but concise**: Capture details without excess
5. **Follow up on actions**: Track completion of action items

## Output

Create a postmortem with:
1. All sections filled in based on provided information
2. Specific, actionable action items
3. Clear root cause analysis
4. Lessons learned that can be shared

## Target

$ARGUMENTS

Provide incident details:
- What happened
- When it happened
- What was affected
- How it was resolved
