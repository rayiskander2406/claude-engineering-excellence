# Claude Code Guide for Developers

> *"Write better code faster, learn continuously, ship with confidence."*

This guide covers day-to-day Claude Code workflows for software developers.

---

## Your Daily Toolkit

| Task | Command | When to Use |
|------|---------|-------------|
| Understand code | `/explain` | Before modifying unfamiliar code |
| Write features | Just ask | New functionality |
| Fix bugs | `/debug` | When stuck on an issue |
| Review code | `/code-review` | Before every commit |
| Write tests | `/test-gen` | After writing features |
| Commit changes | `/commit` | Ready to commit |
| Create PR | `/pr-prep` | Ready for review |
| Capture learning | `/learn` | Discovered something useful |

---

## Workflow 1: Starting a New Feature

### Step 1: Understand the Context

```
/search-knowledge [feature area]
```

Check if the team has patterns or learnings related to your feature.

### Step 2: Plan Before Coding

Ask Claude to help plan:

```
I need to implement [FEATURE].

Requirements:
- [Requirement 1]
- [Requirement 2]

What's the best approach? Consider:
- Existing patterns in this codebase
- Error handling
- Testing strategy
```

### Step 3: Implement Incrementally

Don't ask for the entire feature at once. Break it down:

```
Let's start with the data model for [FEATURE].
```

Then:

```
Now let's add the service layer.
```

Then:

```
Now let's add the API endpoint.
```

### Step 4: Generate Tests

```
/test-gen src/features/[feature]/
```

Or be specific:

```
Write unit tests for the UserService covering:
- Happy path for createUser
- Validation errors
- Duplicate email handling
- Database failures
```

### Step 5: Review Before Committing

```
/code-review
```

Fix any issues Claude identifies.

### Step 6: Commit and PR

```
/commit
```

Then:

```
/pr-prep
```

---

## Workflow 2: Fixing a Bug

### Step 1: Gather Information

Share with Claude:
- Error message/stack trace
- Steps to reproduce
- What you've already tried

```
I'm seeing this error:

[ERROR MESSAGE]

It happens when [STEPS TO REPRODUCE].

I've tried [WHAT YOU TRIED].

Help me debug this.
```

### Step 2: Use Systematic Debugging

```
/debug
```

This walks through:
1. Understanding the error
2. Forming hypotheses
3. Testing each hypothesis
4. Identifying root cause
5. Implementing fix

### Step 3: Write a Regression Test

Before fixing, write a test that fails:

```
Write a test that reproduces this bug so we can verify the fix and prevent regression.
```

### Step 4: Fix and Verify

Implement the fix, run tests, then:

```
/code-review
```

### Step 5: Capture the Learning

```
/learn
```

Document:
- What caused the bug
- How you found it
- How you fixed it
- How to prevent similar bugs

---

## Workflow 3: Refactoring Code

### Step 1: Understand Current State

```
/explain src/legacy/[file]
```

Ask:
- What does this code do?
- Why is it structured this way?
- What are the dependencies?

### Step 2: Identify Refactoring Opportunities

```
Analyze this code for refactoring opportunities:
- Code duplication
- Complex conditionals
- Long methods
- Poor naming
- Missing abstractions
```

### Step 3: Plan the Refactoring

```
Create a step-by-step refactoring plan that:
- Maintains behavior (no functional changes)
- Can be done incrementally
- Keeps tests passing at each step
```

### Step 4: Refactor Incrementally

Follow the plan one step at a time. Run tests after each step.

### Step 5: Review the Refactoring

```
/code-review
```

Ensure no behavioral changes snuck in.

---

## Workflow 4: Code Review (Reviewing Others' Code)

### Step 1: Understand the Changes

```
Explain what this PR does and identify any concerns:

[PASTE DIFF OR DESCRIBE CHANGES]
```

### Step 2: Check for Common Issues

Ask Claude to look for:

```
Review this code for:
- Security vulnerabilities
- Performance issues
- Error handling gaps
- Test coverage
- Code style violations
- Potential edge cases
```

### Step 3: Generate Review Comments

```
Generate constructive code review comments for this PR, categorized by:
- Must fix (blocking)
- Should fix (important)
- Consider (suggestions)
- Nitpick (style)
```

---

## Workflow 5: Learning a New Codebase

### Step 1: Get the Big Picture

```
/search-knowledge architecture overview
```

Or ask:

```
Analyze this codebase and explain:
- Overall architecture
- Key components and their responsibilities
- Data flow
- Important patterns used
```

### Step 2: Trace a Request

```
Trace how a [TYPE] request flows through the system from entry point to response.
```

### Step 3: Understand Key Files

```
/explain src/core/[important-file]
```

### Step 4: Find Patterns

```
What patterns does this codebase use for:
- Error handling
- Validation
- Authentication
- Database access
- Testing
```

---

## Power User Tips

### Be Specific About What You Want

```
# Bad
Make this code better

# Good
Refactor this function to:
- Extract the validation logic into a separate method
- Add error handling for null inputs
- Use early returns instead of nested ifs
```

### Provide Context

```
# Bad
Why doesn't this work?

# Good
I'm trying to fetch user data with React Query v5.
This code returns undefined even though the API returns data.
Here's the hook: [CODE]
Here's the API response: [RESPONSE]
```

### Ask for Explanations

```
# Don't just accept code - understand it
Why did you choose this approach over [ALTERNATIVE]?
```

### Use Constraints

```
Implement this feature with these constraints:
- No external dependencies
- Must work with Node 18
- Should be under 50 lines
- Must handle these edge cases: [LIST]
```

### Iterate

```
# First pass
Implement basic user validation

# Refinement
Now add email format validation using regex

# Refinement
Add rate limiting for failed validations
```

---

## Common Tasks - Quick Reference

### Generate TypeScript Types from JSON

```
Generate TypeScript interfaces for this JSON response:
[JSON]
```

### Convert Between Formats

```
Convert this SQL query to Prisma:
[SQL]
```

### Add Error Handling

```
Add comprehensive error handling to this function:
[CODE]
```

### Optimize Performance

```
This function is slow with large datasets. Suggest optimizations:
[CODE]
```

### Write Documentation

```
Write JSDoc documentation for this function:
[CODE]
```

### Generate Mock Data

```
Generate realistic mock data for testing the User model:
[SCHEMA]
```

---

## What Claude Does Well

| Task | Claude's Strength |
|------|-------------------|
| Boilerplate code | Excellent - saves huge time |
| Standard patterns | Excellent - knows best practices |
| Explaining code | Excellent - patient teacher |
| Debugging | Very good - systematic approach |
| Test generation | Very good - covers edge cases |
| Refactoring | Very good - safe transformations |
| Architecture | Good - needs your domain knowledge |
| Novel algorithms | Fair - verify carefully |

## What Requires Extra Care

| Task | Why | What to Do |
|------|-----|------------|
| Security code | Can miss edge cases | Always get security review |
| Performance-critical | May not know your scale | Benchmark yourself |
| Domain-specific | Doesn't know your business | Provide context |
| Novel problems | No training data | Verify thoroughly |

---

## Capture Your Learnings

The team gets smarter when you share:

### After Solving a Tricky Bug
```
/learn
```

### After Finding a Better Approach
```
/learn
```

### After Discovering a Gotcha
```
/learn
```

When a learning is proven (3+ uses):
```
/promote
```

---

## Daily Habits of Effective Claude Users

| Morning | During Work | End of Day |
|---------|-------------|------------|
| `/search-knowledge` for context | `/code-review` before commits | `/retro-capture` for learnings |
| Check `.claude/patterns/` | Ask "why" not just "how" | Update knowledge graph |
| Plan your tasks | Test generated code | Share useful prompts |

---

*"Claude is your pair programmer, not your replacement. You bring the domain knowledge, judgment, and accountability."*
