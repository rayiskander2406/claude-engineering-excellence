---
description: Generate comprehensive test cases
---

# Test Generation

Generate comprehensive tests for the specified code.

## Test Categories

### Unit Tests
- Happy path (normal usage)
- Edge cases (boundaries, empty inputs, single items)
- Error cases (invalid inputs, exceptions)
- Null/undefined handling

### Integration Tests
- Component interactions
- Database operations
- API calls
- External service mocking

### Property-Based Tests (if applicable)
- Invariants that should always hold
- Commutative operations
- Round-trip conversions

## Test Structure

Follow the AAA pattern:
1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute the code under test
3. **Assert**: Verify the results

## Naming Convention

```
test_<method>_<scenario>_<expected>

Examples:
- test_login_withValidCredentials_returnsUser
- test_calculateTotal_withEmptyCart_returnsZero
- test_parseDate_withInvalidFormat_throwsException
```

## Coverage Goals

- Aim for 80%+ line coverage
- 100% coverage of public API
- All error paths tested
- All branches covered

## Test Quality Checklist

- [ ] Tests are independent (can run in any order)
- [ ] Tests are deterministic (same result every time)
- [ ] Tests are fast (unit tests < 100ms)
- [ ] Tests have clear failure messages
- [ ] Tests don't test implementation details
- [ ] Mocks are minimal and purposeful

## Output Format

Generate tests that:
1. Use the project's existing test framework
2. Follow existing test patterns in the codebase
3. Include setup/teardown if needed
4. Have descriptive test names
5. Include comments explaining non-obvious assertions

## Target

$ARGUMENTS

Specify the file, class, or function to generate tests for.
