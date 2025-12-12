---
description: Intelligent code refactoring with safe transformations
---

# Code Refactoring

Analyze and refactor the specified code to improve quality while preserving behavior.

## Refactoring Patterns to Consider

### Extract/Inline
- **Extract Method**: Long methods → smaller, named methods
- **Extract Variable**: Complex expressions → named variables
- **Extract Class**: Large classes → focused classes
- **Inline**: Over-abstracted code → simpler direct code

### Simplify
- **Simplify Conditional**: Complex if/else → guard clauses, polymorphism
- **Remove Dead Code**: Unreachable or unused code
- **Replace Magic Numbers**: Literals → named constants
- **Consolidate Duplicates**: Copy-paste → shared functions

### Improve Structure
- **Move Method/Field**: To where they belong
- **Replace Conditional with Polymorphism**
- **Introduce Parameter Object**: Many params → object
- **Replace Temp with Query**: Variables → methods

### Clean Up
- **Rename**: Variables, methods, classes to be clearer
- **Reorder Parameters**: Most important first
- **Remove Middle Man**: Unnecessary delegation
- **Encapsulate Field**: Direct access → getters/setters

## Safety Guidelines

1. **Behavior Preservation**: Changes must not alter functionality
2. **Test Coverage**: Ensure tests exist before refactoring
3. **Small Steps**: Make small, incremental changes
4. **Verify Each Step**: Run tests after each change

## Output Format

### Analysis
- What needs refactoring and why
- Proposed changes
- Risk assessment

### Refactored Code
- Show the refactored code
- Explain each transformation
- Highlight key improvements

### Before/After Metrics
- Lines of code
- Cyclomatic complexity
- Duplication percentage

### Verification Steps
- Tests to run
- Manual verification needed
- Rollback plan

## Target

$ARGUMENTS

Specify the file, function, or class to refactor.
