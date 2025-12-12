---
description: Systematic debugging and root cause analysis
---

# Debugging Assistant

Systematically debug the specified issue using structured analysis.

## Debugging Process

### 1. Reproduce
- Can the issue be reproduced consistently?
- What are the exact steps to reproduce?
- What environment/conditions are required?

### 2. Isolate
- What's the smallest code that demonstrates the issue?
- Is it environmental or code-related?
- Does it happen in all scenarios or specific ones?

### 3. Analyze
- What does the error message/behavior tell us?
- What does the stack trace reveal?
- What changed recently that could cause this?

### 4. Hypothesize
- What are the possible causes?
- Rank by likelihood
- What evidence supports/refutes each?

### 5. Test
- How can we verify each hypothesis?
- What's the quickest way to test?
- What would prove/disprove the cause?

### 6. Fix
- What's the correct fix?
- Are there side effects?
- How do we prevent recurrence?

## Common Causes Checklist

- [ ] Null/undefined reference
- [ ] Off-by-one error
- [ ] Race condition
- [ ] State mutation issue
- [ ] Wrong data type
- [ ] Missing error handling
- [ ] Configuration issue
- [ ] Dependency version mismatch
- [ ] Cache staleness
- [ ] Memory leak
- [ ] Resource exhaustion

## Output Format

### Issue Summary
Brief description of the problem.

### Root Cause
What's actually causing the issue.

### Evidence
How we know this is the cause.

### Fix
The code change needed.

### Prevention
How to prevent this in the future (tests, linting rules, etc.).

### Related Issues
Other places this might occur.

## Target

$ARGUMENTS

Provide:
- Error message or unexpected behavior
- Stack trace (if available)
- Steps to reproduce
- Relevant code or files
