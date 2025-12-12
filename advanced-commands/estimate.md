---
description: Generate effort estimates with confidence ranges
---

# Effort Estimation

Generate effort estimates with confidence ranges and risk analysis.

## Estimation Approach

### PERT Estimation
- **Optimistic (O)**: Best case, everything goes smoothly
- **Most Likely (M)**: Realistic expectation
- **Pessimistic (P)**: Worst case, problems encountered

**Expected**: (O + 4M + P) / 6

### Confidence Levels
- **High confidence**: Well-understood, done before, few unknowns
- **Medium confidence**: Some unknowns, similar work done before
- **Low confidence**: Many unknowns, new territory

### T-Shirt Sizing
| Size | Description |
|------|-------------|
| XS | Trivial, < 2 hours |
| S | Small, 2-4 hours |
| M | Medium, 1-2 days |
| L | Large, 3-5 days |
| XL | Very large, 1-2 weeks |
| XXL | Epic, needs breakdown |

## Estimation Template

```markdown
# Estimate: [Task/Feature]

## Summary
**T-Shirt Size**: [XS-XXL]
**Expected Effort**: [X] days
**Confidence**: [High/Medium/Low]

## Breakdown

| Component | Optimistic | Most Likely | Pessimistic |
|-----------|------------|-------------|-------------|
| [Task 1] | | | |
| [Task 2] | | | |
| Testing | | | |
| Code review | | | |
| **Total** | | | |

## Assumptions
- [Assumption 1]
- [Assumption 2]

## Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| | | | |

## Dependencies
- [Dependency 1]
- [Dependency 2]

## Comparable Work
- [Similar past work]: [Actual time]

## Recommendation
[Final recommendation with caveats]
```

## Estimation Heuristics

### Common Multipliers
- First time doing something: 2-3x estimate
- Integration with external systems: +50%
- Legacy code modification: +30-50%
- Missing documentation: +20%
- Parallel work streams: +20% coordination overhead

### Common Omissions
- Testing (often underestimated)
- Code review cycles
- Documentation
- Deployment and verification
- Bug fixes from code review

## Output Format

Generate:
1. **Quick estimate**: T-shirt size and days
2. **Detailed breakdown**: By component
3. **Risk analysis**: What could affect estimate
4. **Confidence assessment**: How sure are we
5. **Recommendations**: Suggestions for more accurate estimate

## Target

$ARGUMENTS

Describe the task or feature to estimate. Include:
- What needs to be done
- Any known constraints
- Available context
