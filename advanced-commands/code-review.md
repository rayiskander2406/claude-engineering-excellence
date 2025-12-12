---
description: Comprehensive multi-dimensional code review
---

# Code Review

Perform a comprehensive code review of the specified code or recent changes.

## Review Dimensions

### 1. Correctness
- Does the code do what it's supposed to do?
- Are there logic errors or edge cases not handled?
- Are there off-by-one errors, null pointer issues, or race conditions?

### 2. Security
- SQL injection, XSS, CSRF vulnerabilities?
- Secrets or credentials exposed?
- Input validation and sanitization?
- Authentication/authorization properly enforced?

### 3. Performance
- N+1 queries or inefficient database access?
- Unnecessary loops or computations?
- Memory leaks or unbounded growth?
- Missing caching opportunities?

### 4. Maintainability
- Is the code readable and self-documenting?
- Are names clear and consistent?
- Is there unnecessary complexity?
- DRY violations or copy-paste code?

### 5. Testing
- Are there tests for new functionality?
- Do tests cover edge cases?
- Are tests maintainable and not brittle?

### 6. Documentation
- Are public APIs documented?
- Are complex algorithms explained?
- Is the why captured, not just the what?

## Output Format

For each issue found:
1. **Location**: File and line number
2. **Severity**: Critical / Major / Minor / Suggestion
3. **Category**: Security / Performance / Correctness / Style / etc.
4. **Issue**: What's wrong
5. **Recommendation**: How to fix it

End with a summary: total issues by severity, overall assessment, and top 3 priorities.

## Target

$ARGUMENTS

If no target specified, review recent changes (git diff).
