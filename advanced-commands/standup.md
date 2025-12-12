---
description: Generate standup report from activity
---

# Standup Report Generator

Generate a standup report based on recent activity.

## Standup Format

```markdown
# Standup Report - [Date]

## Yesterday
- [Completed task 1]
- [Completed task 2]
- [Progress on ongoing work]

## Today
- [Planned task 1]
- [Planned task 2]
- [Continuing work on X]

## Blockers
- [Blocker 1] - Need [what/who]
- None

## Notes
- [Any relevant context]
- [Upcoming PTO/meetings]
```

## Information Sources

Gather information from:
1. **Git commits**: Recent commits by the user
2. **Pull requests**: Open, merged, or reviewed PRs
3. **Issues**: Assigned issues, status changes
4. **Calendar**: Relevant meetings (if accessible)

## Standup Best Practices

### Good Updates
- Specific and measurable
- Focus on outcomes, not activities
- Highlight blockers early
- Keep brief (< 2 minutes when spoken)

### Avoid
- Vague statements ("worked on stuff")
- Implementation details others don't need
- Rehashing what's in tickets
- Skipping blockers to seem productive

## Output Format

Generate:
1. **Formatted standup** ready to paste
2. **Detailed version** with links to commits/PRs
3. **Blockers analysis** with suggested actions

## Customization

Adjust based on team preferences:
- Include/exclude specific detail
- Add metrics (PRs reviewed, lines changed)
- Include upcoming items
- Format for async vs sync standups

## Target

$ARGUMENTS

Options:
- No args: Generate from last 24 hours
- "week": Generate weekly summary
- Date range: Specific period
