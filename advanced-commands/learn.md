---
description: Capture a learning from current work
---

# Capture Learning

When you discover something valuable during development, capture it immediately.

## Learning Types

| Type | Use When |
|------|----------|
| BUG_FIX | Solved a tricky bug with non-obvious solution |
| PATTERN | Found a reusable approach that worked well |
| GOTCHA | Discovered a non-obvious trap to avoid |
| PERFORMANCE | Found an optimization that worked |
| INTEGRATION | Learned how two systems connect |
| SECURITY | Found a security consideration |

## Capture Process

1. **Identify the type** from the table above

2. **Create learning entry** in `.claude/learnings/YYYY-MM-DD.md`:

```markdown
## [TIME] - [TITLE]

**Type**: [BUG_FIX|PATTERN|GOTCHA|PERFORMANCE|INTEGRATION|SECURITY]
**Tags**: #tag1 #tag2

### Context
What were you trying to do?

### Discovery
What did you learn?

### Evidence
Code snippet, error message, or proof.

### Applicability
When should this be applied in the future?
```

3. **Update knowledge graph**:
```javascript
mcp__memory__create_entities([{
  name: "Learning: [TITLE]",
  entityType: "learning",
  observations: ["[TYPE]: [KEY INSIGHT]", "Tags: [tags]", "Date: [YYYY-MM-DD]"]
}])
```

4. **Link to related entities** if applicable:
```javascript
mcp__memory__create_relations([{
  source: "Learning: [TITLE]",
  target: "[RELATED ENTITY]",
  type: "relates_to"
}])
```

## Quality Checklist

Before saving, ensure:
- [ ] Context is clear (someone else could understand)
- [ ] Discovery is specific (not vague)
- [ ] Evidence is provided (not just assertion)
- [ ] Tags are appropriate (searchable)

## Target

$ARGUMENTS

Describe what you learned:
- What were you working on?
- What did you discover?
- Why is this valuable for the team?
