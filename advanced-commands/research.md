---
description: Systematic technology research and evaluation
---

# Technology Research

Conduct systematic research on a technology, library, or approach.

## Research Framework

### 1. Problem Definition
- What problem are we solving?
- What are the requirements?
- What constraints exist?

### 2. Landscape Survey
- What solutions exist?
- Who uses them?
- How mature are they?

### 3. Deep Evaluation
- Technical capabilities
- Performance characteristics
- Security considerations
- Maintenance burden

### 4. Decision
- Recommendation
- Trade-offs acknowledged
- Migration path

## Evaluation Criteria

### Technical
- Does it solve the problem?
- Performance characteristics
- Scalability
- Security posture
- Integration complexity

### Ecosystem
- Community size and activity
- Documentation quality
- Available learning resources
- Commercial support options

### Maintenance
- Release frequency
- Breaking change history
- Long-term viability
- Bus factor (maintainer count)

### Compatibility
- Works with our stack
- License compatible
- Team familiarity
- Learning curve

## Research Template

```markdown
# Research: [Topic]

## Problem Statement
What are we trying to solve?

## Requirements
| Requirement | Priority | Notes |
|-------------|----------|-------|
| | Must have | |
| | Nice to have | |

## Options Evaluated

### Option 1: [Name]
**Description**: What is it?
**Pros**:
-
**Cons**:
-
**Technical Assessment**:
- Performance:
- Security:
- Scalability:
**Community Health**:
- Stars/Downloads:
- Last release:
- Maintainers:
**Verdict**: Recommended / Not recommended

### Option 2: [Name]
[Same structure]

## Comparison Matrix

| Criterion | Option 1 | Option 2 | Option 3 |
|-----------|----------|----------|----------|
| Performance | | | |
| Security | | | |
| Ease of use | | | |
| Community | | | |
| Cost | | | |

## Recommendation

**Recommended Option**: [Name]

**Rationale**:
1. [Reason 1]
2. [Reason 2]

**Trade-offs**:
1. [Trade-off 1]
2. [Trade-off 2]

**Migration Path**:
[How to adopt]

## References
- [Links to documentation, articles, benchmarks]
```

## Research Best Practices

1. **Primary sources**: Official docs, not just blog posts
2. **Multiple perspectives**: Don't just read positive reviews
3. **Hands-on evaluation**: Try before committing
4. **Document everything**: Future you will thank present you
5. **Reproducible**: Others can verify your research

## Output Format

Generate:
1. **Executive summary**: Key findings in 2-3 paragraphs
2. **Detailed comparison**: All options evaluated
3. **Recommendation**: Clear recommendation with rationale
4. **Sources**: All sources cited
5. **Claude Code prompt**: To reproduce/extend this research

## Target

$ARGUMENTS

Describe what to research:
- Technology/library/tool to evaluate
- Problem to solve
- Specific requirements
- Constraints to consider
