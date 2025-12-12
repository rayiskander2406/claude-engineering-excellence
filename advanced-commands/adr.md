---
description: Create Architecture Decision Record
---

# Architecture Decision Record

Create an ADR documenting a significant technical decision.

## ADR Template

```markdown
# ADR-NNNN: [Title]

## Status

[Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]

## Date

[YYYY-MM-DD]

## Context

What is the issue that we're seeing that is motivating this decision or change?

- Current situation
- Problem or opportunity
- Constraints
- Stakeholder concerns

## Decision

What is the change that we're proposing and/or doing?

State the decision as a clear, declarative statement.

## Consequences

What becomes easier or more difficult to do because of this change?

### Positive
- Benefits of this decision

### Negative
- Drawbacks or trade-offs

### Neutral
- Other effects

## Alternatives Considered

### Alternative 1: [Name]
**Description**: What is this alternative?
**Pros**:
**Cons**:
**Why rejected**:

### Alternative 2: [Name]
**Description**: What is this alternative?
**Pros**:
**Cons**:
**Why rejected**:

## References

- Links to relevant resources
- Related ADRs
- External documentation
```

## When to Write an ADR

- Choosing a framework or library
- Selecting a database or data store
- Defining API design patterns
- Setting authentication/authorization approach
- Choosing deployment strategy
- Making significant architectural changes
- Establishing coding standards

## ADR Best Practices

1. **One decision per ADR**: Keep focused
2. **Explain context first**: Future readers need background
3. **Document alternatives**: Show due diligence
4. **Be honest about trade-offs**: No decision is perfect
5. **Keep it concise**: Target 1-2 pages
6. **Update status**: Mark as deprecated/superseded when appropriate

## Output

Create an ADR with:
1. Auto-generated number (next in sequence)
2. All sections filled in
3. Saved to `docs/adr/` directory
4. Linked to any related ADRs

## Target

$ARGUMENTS

Describe the decision to document. Include:
- What decision was made
- Why it was needed
- What alternatives were considered
