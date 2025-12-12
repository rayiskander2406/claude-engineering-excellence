---
description: Generate conventional commit message
---

# Commit Message Generator

Analyze staged changes and generate a conventional commit message.

## Conventional Commit Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Formatting, missing semicolons, etc.
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or correcting tests
- **chore**: Maintenance tasks
- **ci**: CI/CD changes
- **build**: Build system changes

### Scope
- Optional, in parentheses
- Module, component, or area affected
- Examples: (auth), (api), (ui), (db)

### Description
- Imperative mood: "add" not "added"
- No period at end
- Under 72 characters

### Body
- Explain what and why, not how
- Wrap at 72 characters
- Separate from subject with blank line

### Footer
- Breaking changes: `BREAKING CHANGE: description`
- Issue references: `Closes #123`, `Fixes #456`

## Examples

```
feat(auth): add OAuth2 login support

Implement Google and GitHub OAuth2 providers to allow users
to sign in with their existing accounts.

Closes #234
```

```
fix(api): handle null response from payment provider

The payment provider occasionally returns null instead of
an error object. This caused unhandled exceptions in production.

Fixes #567
```

```
refactor(db): simplify query builder interface

BREAKING CHANGE: QueryBuilder.execute() now returns a Promise
instead of accepting a callback.
```

## Output

Analyze the staged changes (git diff --staged) and generate:
1. The complete commit message
2. Explanation of why this type/scope was chosen
3. Alternative commit messages if the changes could be interpreted differently

## Target

$ARGUMENTS

If arguments provided, use as additional context for the commit message.
