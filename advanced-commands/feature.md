---
description: Scaffold new feature with tests and docs
---

# Feature Scaffold

Scaffold a new feature with proper structure, tests, and documentation.

## Feature Structure

### Files to Create

Depending on the feature type, create:

**Backend Feature**
```
src/
├── [feature]/
│   ├── [feature].controller.ts   # API endpoints
│   ├── [feature].service.ts      # Business logic
│   ├── [feature].repository.ts   # Data access
│   ├── [feature].model.ts        # Data models
│   ├── [feature].dto.ts          # DTOs/validation
│   └── index.ts                  # Public exports
tests/
├── [feature]/
│   ├── [feature].controller.test.ts
│   ├── [feature].service.test.ts
│   └── [feature].integration.test.ts
docs/
└── [feature].md                  # Feature documentation
```

**Frontend Feature**
```
src/
├── features/
│   └── [feature]/
│       ├── components/
│       │   ├── [Feature].tsx
│       │   └── [Feature].test.tsx
│       ├── hooks/
│       │   └── use[Feature].ts
│       ├── api/
│       │   └── [feature]Api.ts
│       ├── types/
│       │   └── [feature].types.ts
│       └── index.ts
```

### Test Structure

```typescript
describe('[Feature]', () => {
  describe('[method/component]', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange
      // Act
      // Assert
    });

    it('should handle [edge case]', () => {});

    it('should throw when [error condition]', () => {});
  });
});
```

### Documentation Structure

```markdown
# [Feature Name]

## Overview
What this feature does.

## Usage
How to use this feature.

## API Reference
Detailed API documentation.

## Examples
Code examples.

## Configuration
Any configuration options.
```

## Scaffold Checklist

- [ ] Core implementation files
- [ ] Unit tests for each component
- [ ] Integration tests
- [ ] API documentation
- [ ] README/usage documentation
- [ ] Type definitions
- [ ] Index exports
- [ ] Error handling

## Output Format

Generate:
1. **File list**: All files to be created
2. **File contents**: Skeleton code for each file
3. **Tests**: Initial test cases
4. **Documentation**: README and API docs
5. **Implementation guide**: Steps to complete the feature

## Target

$ARGUMENTS

Describe the feature:
- What it should do
- API requirements
- Data models needed
- Any integrations
