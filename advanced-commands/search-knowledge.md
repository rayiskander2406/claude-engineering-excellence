---
description: Search project's accumulated knowledge
---

# Search Knowledge

Query the project's institutional memory to find relevant learnings, patterns, decisions, and failures.

## Search Process

### 1. Query Knowledge Graph

```javascript
mcp__memory__search_nodes("[YOUR QUERY]")
```

This searches:
- Learnings (discoveries from past work)
- Patterns (proven solutions)
- Decisions (ADRs)
- Failures (what not to do)

### 2. Search Files

If knowledge graph doesn't have enough, search files:

```bash
# Search learnings
grep -ri "[QUERY]" .claude/learnings/

# Search patterns
grep -ri "[QUERY]" .claude/patterns/

# Search failures
grep -ri "[QUERY]" .claude/failures/

# Search decisions
grep -ri "[QUERY]" .claude/decisions/
```

### 3. Synthesize Findings

Combine results into actionable guidance:

```markdown
## Search Results for "[QUERY]"

### Relevant Patterns
- **[Pattern Name]**: [Brief description and link]

### Related Learnings
- [DATE]: [Learning title] - [Key insight]

### Known Failures to Avoid
- [What not to do and why]

### Relevant Decisions
- ADR-[N]: [Decision that affects this]

### Recommendation
Based on accumulated knowledge: [actionable guidance]
```

### 4. Flag Knowledge Gaps

If the search reveals gaps:

```markdown
### Knowledge Gap Identified
Topic "[QUERY]" has limited coverage. Consider:
- [ ] Capturing learnings as you work on this
- [ ] Creating a pattern if solution emerges
- [ ] Documenting any failures encountered
```

## Search Tips

| Looking For | Try Searching |
|-------------|---------------|
| How to do X | "[X] pattern" or "[X] approach" |
| Why we chose X | "ADR [X]" or "decision [X]" |
| What went wrong with X | "[X] failure" or "[X] gotcha" |
| Performance issues | "performance" + "[component]" |
| Security concerns | "security" + "[feature]" |

## Target

$ARGUMENTS

What are you looking for?
- Describe your problem or question
- Include relevant technology/component names
- Mention any context that might help narrow results
