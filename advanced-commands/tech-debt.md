---
description: Technical debt assessment and prioritization
---

# Technical Debt Assessment

Analyze the codebase for technical debt and create a prioritized remediation plan.

## Debt Categories

### 1. Code Quality Debt
- Complex functions (high cyclomatic complexity)
- Long methods/classes
- Deep nesting
- Code duplication
- Poor naming
- Missing or outdated comments

### 2. Architectural Debt
- Circular dependencies
- God classes/modules
- Violation of SOLID principles
- Missing abstraction layers
- Tight coupling

### 3. Testing Debt
- Low test coverage
- Missing unit tests
- Brittle tests
- No integration tests
- Missing edge case coverage

### 4. Documentation Debt
- Missing README
- Outdated documentation
- Missing API documentation
- Undocumented configuration

### 5. Dependency Debt
- Outdated dependencies
- Deprecated packages
- Known vulnerabilities
- Unmaintained libraries

### 6. Infrastructure Debt
- Manual deployment steps
- Missing monitoring
- No CI/CD
- Hardcoded configuration

## Assessment Criteria

For each debt item, evaluate:
- **Impact**: How much does this slow us down? (1-10)
- **Risk**: What's the likelihood of causing issues? (1-10)
- **Effort**: How hard is it to fix? (T-shirt size: S/M/L/XL)
- **Urgency**: Is this blocking other work? (Yes/No)

## Output Format

### Summary
- Overall debt score (1-100)
- Debt by category (pie chart data)
- Trend assessment (getting better/worse?)

### Top 10 Debt Items
For each:
1. Description
2. Location
3. Impact × Risk score
4. Suggested fix
5. Estimated effort

### Recommended Actions
- Quick wins (high impact, low effort)
- Strategic investments (high impact, high effort)
- Scheduled maintenance (low impact, low effort)
- Consider ignoring (low impact, high effort)

### 90-Day Plan
Prioritized list of debt to address in the next quarter.

## Target

$ARGUMENTS

If no target specified, analyze the entire codebase.
