---
description: Promote a validated learning to a proven pattern
---

# Promote Learning to Pattern

Elevate a learning that has been validated through repeated use into a proven pattern.

## Promotion Criteria

A learning is ready for promotion when:

- [ ] Used successfully 3+ times
- [ ] No negative side effects observed
- [ ] Applicable beyond original context
- [ ] Another team member has validated

## Promotion Process

### 1. Gather Related Learnings

Search for all learnings on the topic:
```bash
grep -r "[TOPIC]" .claude/learnings/
```

Query knowledge graph:
```javascript
mcp__memory__search_nodes("[TOPIC]")
```

### 2. Create Pattern File

Create `.claude/patterns/[pattern-name].md`:

```markdown
# Pattern: [NAME]

**Status**: PROVEN
**First Discovered**: [DATE] by [WHO]
**Validated**: [DATE] after [N] successful uses
**Last Updated**: [DATE]

## Problem

What problem does this pattern solve?
Be specific about the symptoms and context.

## Solution

The recommended approach:

```[language]
// Code example from this project
```

## Why This Works

The reasoning and evidence behind the pattern.

## When to Use

- Scenario 1: [description]
- Scenario 2: [description]

## When NOT to Use

- Anti-scenario 1: [description]
- Anti-scenario 2: [description]

## Examples

### Example 1: [Context]
[Real code from this project]

### Example 2: [Context]
[Real code from this project]

## Related Patterns

- [Link to related pattern]

## History

| Date | Event |
|------|-------|
| [DATE] | First discovered |
| [DATE] | Validated after N uses |
| [DATE] | Pattern documented |
```

### 3. Update CLAUDE.md

Add reference to the pattern:

```markdown
## Project Patterns
- **[Pattern Name]**: See `.claude/patterns/[filename].md` - [brief description]
```

### 4. Update Knowledge Graph

```javascript
// Create pattern entity
mcp__memory__create_entities([{
  name: "Pattern: [NAME]",
  entityType: "pattern",
  observations: ["Status: PROVEN", "Solves: [PROBLEM]", "Created: [DATE]"]
}])

// Link to source learnings
mcp__memory__create_relations([{
  source: "Pattern: [NAME]",
  target: "Learning: [ORIGINAL LEARNING]",
  type: "derived_from"
}])
```

### 5. Archive Source Learnings

Mark the original learnings as "promoted to pattern" so they're not promoted again.

## Target

$ARGUMENTS

Which learning should be promoted?
- Provide the learning title or date
- Explain why it's ready for promotion
- List the successful uses that validated it
