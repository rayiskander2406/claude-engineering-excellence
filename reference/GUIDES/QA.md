# Claude Code Guide for QA Engineers

> *"Find bugs before users do. Automate the repetitive. Focus on what matters."*

This guide covers Claude Code workflows tailored for QA Engineers, Test Automation Engineers, and SDETs.

---

## Your QA Toolkit

| Task | Command/Approach | When to Use |
|------|------------------|-------------|
| Generate test cases | `/test-gen` | New features |
| Write E2E tests | Just ask | Automation |
| Analyze bugs | `/debug` | Investigation |
| Create test data | Just ask | Test setup |
| Review test coverage | Just ask | Quality gates |
| Generate API tests | Just ask | Backend testing |
| Write accessibility tests | Just ask | A11y compliance |
| Create test plans | Just ask | Sprint planning |

---

## Workflow 1: Test Case Generation

### From Requirements

```
Generate test cases for this feature:

Feature: User Registration
- User can register with email and password
- Password must be 8+ characters with uppercase, lowercase, number
- Email must be unique
- User receives confirmation email
- Account is inactive until email confirmed

Include:
- Happy path
- Boundary conditions
- Error cases
- Security considerations
```

### From Code

```
/test-gen src/features/auth/register.ts
```

Or be specific:

```
Analyze this registration function and generate test cases covering:
- Input validation
- Edge cases
- Error handling
- Security vulnerabilities

[PASTE CODE]
```

### Test Case Format

```
Generate test cases in this format:

| ID | Title | Preconditions | Steps | Expected Result | Priority |
|----|-------|---------------|-------|-----------------|----------|
```

---

## Workflow 2: Test Automation - E2E

### Playwright Tests

```
Write Playwright tests for user login:
- Successful login
- Invalid password
- Non-existent user
- Account locked after 5 failures
- Remember me functionality
- SSO redirect

Use Page Object Model.
Include proper waits and assertions.
```

### Cypress Tests

```
Write Cypress tests for the shopping cart:
- Add item to cart
- Update quantity
- Remove item
- Apply discount code
- Checkout flow

Use custom commands for common actions.
Include API stubbing for edge cases.
```

### Selenium (if needed)

```
Write Selenium tests in Python for the search functionality:
- Basic search
- Search with filters
- Empty results
- Pagination
- Search suggestions

Use explicit waits.
Follow Page Object pattern.
```

### Debugging Flaky Tests

```
This E2E test is flaky:

[TEST CODE]

It fails intermittently with:
[ERROR]

Help me identify and fix the flakiness.
```

---

## Workflow 3: API Testing

### Generate API Tests

```
Generate API tests for this endpoint:

POST /api/users
Request: { name, email, role }
Response: { id, name, email, role, createdAt }

Test cases:
- Valid request
- Missing required fields
- Invalid email format
- Duplicate email
- Invalid role
- Unauthorized request
- Rate limiting

Use Jest + Supertest.
```

### Contract Testing

```
Create Pact contract tests for the user service:

Consumer: Frontend
Provider: User API

Interactions:
- Get user by ID
- Create user
- Update user
- Delete user
```

### Load Testing

```
Create a k6 load test script for our API:
- Ramp up to 500 concurrent users
- Sustained load for 10 minutes
- Ramp down

Test endpoints:
- GET /api/products (80% of traffic)
- POST /api/orders (15% of traffic)
- GET /api/users/me (5% of traffic)

Include thresholds:
- p95 latency < 500ms
- Error rate < 1%
```

---

## Workflow 4: Test Data Generation

### Realistic Test Data

```
Generate realistic test data for user testing:
- 100 users with varied demographics
- Mix of subscription tiers
- Various account ages
- Include edge cases (long names, special characters, international)

Output as JSON.
```

### Database Seeding

```
Create a database seed script for testing that:
- Creates 50 users
- Creates 200 products across 10 categories
- Creates 500 orders with various statuses
- Handles foreign key relationships
- Is idempotent

Use Prisma format.
```

### Mock Data for Specific Scenarios

```
Generate test data for these edge cases:
- User with maximum allowed addresses (10)
- Order with 100 line items
- Product with all optional fields null
- User with emoji in name
- International addresses (Japan, Germany, Brazil)
```

---

## Workflow 5: Bug Investigation

### Analyzing a Bug

```
/debug

Bug Report:
- Title: Checkout fails for users with multiple addresses
- Steps: 1. Add item, 2. Go to checkout, 3. Select alternate address, 4. Error

What I've found:
- Works for users with 1 address
- Fails for users with 2+ addresses
- API returns 500

Help me investigate.
```

### Creating Bug Reports

```
Help me write a clear bug report:

What I observed:
[DESCRIBE]

Expected:
[DESCRIBE]

Include:
- Clear title
- Steps to reproduce
- Expected vs actual
- Environment details
- Severity assessment
```

### Root Cause Analysis

```
This test started failing after a recent PR:

Test: [TEST NAME]
Error: [ERROR MESSAGE]
PR: [PR LINK/DESCRIPTION]

Help me trace the root cause.
```

---

## Workflow 6: Accessibility Testing

### Automated A11y Tests

```
Write accessibility tests for the checkout page using:
- axe-core for automated checks
- Manual test cases for keyboard navigation
- Screen reader testing checklist

WCAG 2.1 AA compliance required.
```

### A11y Checklist Generation

```
Generate an accessibility testing checklist for a modal dialog:
- Keyboard navigation
- Focus management
- ARIA attributes
- Screen reader announcements
- Color contrast
- Motion preferences
```

### Remediation Guidance

```
The accessibility scanner found these issues:

[AXE-CORE OUTPUT]

Explain each issue and how to fix it.
Prioritize by impact on users.
```

---

## Workflow 7: Performance Testing

### Performance Test Suite

```
Create a performance test strategy for our e-commerce site:
- Key user journeys to test
- Performance budgets
- Tools to use
- Metrics to capture
- Baseline vs target
```

### Lighthouse Automation

```
Create a script that:
- Runs Lighthouse on key pages
- Captures Core Web Vitals
- Compares to baselines
- Fails CI if thresholds exceeded
- Generates trend report
```

### Database Performance

```
Generate SQL queries to identify performance issues:
- Slow queries
- Missing indexes
- Table bloat
- Lock contention
```

---

## Workflow 8: Test Planning

### Sprint Test Planning

```
Create a test plan for this sprint's features:

Features:
1. User profile editing
2. Password reset flow
3. Export data to CSV

Include:
- Test scope
- Test types needed
- Resource requirements
- Risk assessment
- Entry/exit criteria
```

### Regression Test Selection

```
Given these code changes:

[DIFF OR DESCRIPTION]

Recommend which regression tests to run:
- Must run
- Should run
- Can skip

Explain the reasoning.
```

### Test Estimation

```
Estimate testing effort for this feature:

[FEATURE DESCRIPTION]

Include:
- Test case creation
- Automation development
- Manual testing
- Environment setup
- Bug fixing buffer
```

---

## Workflow 9: Test Documentation

### Test Strategy Document

```
Create a test strategy document for our mobile app:
- Testing levels (unit, integration, E2E)
- Test environments
- Device/OS coverage
- Automation approach
- CI/CD integration
- Reporting
```

### Test Case Documentation

```
Convert these manual test steps into proper test documentation:

[INFORMAL NOTES]

Format:
- Clear preconditions
- Numbered steps
- Expected results for each step
- Test data requirements
```

---

## Common QA Tasks - Quick Reference

### Generate Boundary Test Cases

```
Generate boundary test cases for:
- Age field (0-150)
- Price field (0.01-999999.99)
- Quantity field (1-100)
- Text field (1-500 characters)
```

### Create Test Matrix

```
Create a test matrix for:
- 3 browsers (Chrome, Firefox, Safari)
- 3 OS (Windows, Mac, Linux)
- 3 user roles (Admin, User, Guest)
- 2 themes (Light, Dark)

Identify which combinations are critical.
```

### Mobile Test Cases

```
Generate mobile-specific test cases for the checkout flow:
- Touch interactions
- Orientation changes
- Network conditions (offline, slow 3G)
- Interruptions (calls, notifications)
- Different screen sizes
```

### Security Test Cases

```
Generate security test cases for the login form:
- SQL injection
- XSS
- Brute force
- Session management
- CSRF
- Rate limiting
```

---

## MCP Servers for QA

### Essential Stack

```bash
# Memory - remember test patterns, bug patterns
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'

# GitHub - link to issues, PRs
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Context7 - testing framework docs
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

### QA-Specific

```bash
# Playwright - browser automation
claude mcp add playwright -- npx -y @anthropic/mcp-server-playwright

# Sentry - error tracking
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

---

## Playwright MCP Superpowers

With Playwright MCP installed:

```
Navigate to https://staging.example.com/login and:
1. Fill in email "test@example.com"
2. Fill in password "Test123!"
3. Click login button
4. Verify dashboard loads
5. Take a screenshot
```

```
Check accessibility on the current page using axe-core.
```

```
Generate a Playwright test script from my actions:
1. Go to products page
2. Filter by category "Electronics"
3. Sort by price low-high
4. Add first item to cart
```

---

## Test Quality Patterns

### Good Test Characteristics

| Characteristic | How Claude Helps |
|----------------|------------------|
| Independent | Ask for isolated test setup/teardown |
| Repeatable | Request deterministic test data |
| Clear assertions | Ask for specific, single assertions |
| Fast | Ask for mocking strategies |
| Maintainable | Request Page Object patterns |

### Ask Claude To Review Tests

```
Review these tests for:
- Test isolation issues
- Flakiness risks
- Missing edge cases
- Assertion quality
- Maintainability

[PASTE TESTS]
```

---

## Capture QA Knowledge

### After Finding a Bug Pattern

```
/learn

Bug pattern: Race condition in cart updates
Symptoms: Intermittent "quantity mismatch" errors
Root cause: No optimistic locking
Regression test added: test/cart/concurrent-updates.spec.ts
```

### After Improving Test Coverage

```
/learn

Added E2E tests for payment flow
Key scenarios:
- 3D Secure authentication
- Failed payments
- Partial refunds
Coverage: 95% of payment code paths
```

### After Fixing Flaky Tests

```
/learn

Fixed flaky login test
Cause: Race condition waiting for redirect
Solution: Wait for specific URL pattern, not just navigation
Pattern: Always use explicit waits for URL changes
```

---

## QA Daily Habits

| Morning | During Work | End of Day |
|---------|-------------|------------|
| Check failed tests | Document bugs clearly | `/retro-capture` |
| Review new PRs for testability | Update test cases | Update test documentation |
| `/search-knowledge` for patterns | Automate repetitive checks | Share bug patterns found |

---

## Collaboration Tips

### Helping Developers Write Better Tests

```
Review this developer's unit test and suggest improvements:

[TEST CODE]

Focus on:
- Edge cases missing
- Assertion quality
- Test isolation
```

### Shift-Left Testing

```
Review this feature spec and identify:
- Testability concerns
- Missing acceptance criteria
- Potential edge cases
- Performance considerations

[SPEC]
```

---

*"Quality is not QA's job alone. Use Claude to help everyone write better tests and think about edge cases."*
