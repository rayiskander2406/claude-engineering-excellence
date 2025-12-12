---
description: Prepare comprehensive pull request
---

# Pull Request Preparation

Prepare a comprehensive, high-quality pull request.

## PR Components

### Title
- Use conventional commit format: `type(scope): description`
- Keep under 72 characters
- Be specific and descriptive

### Description
Structure:
```markdown
## Summary
What does this PR do? (1-2 sentences)

## Motivation
Why is this change needed? Link to issue if applicable.

## Changes
- Bullet list of key changes
- Group related changes
- Highlight breaking changes

## Testing
How was this tested?
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Screenshots
(If UI changes)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review performed
- [ ] Documentation updated
- [ ] No new warnings introduced
- [ ] Tests pass locally
```

### Review Guidance
- Point reviewers to key areas
- Explain non-obvious decisions
- Highlight areas of uncertainty

## Self-Review Checklist

Before requesting review:
- [ ] Diff reviewed line by line
- [ ] No commented-out code
- [ ] No debug statements
- [ ] No TODO comments for this PR
- [ ] All tests pass
- [ ] Linting passes
- [ ] Documentation updated
- [ ] Commit history clean

## Output Format

Generate:
1. **PR Title**: Conventional commit format
2. **PR Description**: Full template filled in
3. **Review Notes**: Key areas for reviewers
4. **Suggested Reviewers**: Based on code owners or file history
5. **Labels**: Suggested labels (feature, bugfix, etc.)
6. **Linked Issues**: Related issues to link

## Target

$ARGUMENTS

If no arguments, analyze staged changes or recent commits.
