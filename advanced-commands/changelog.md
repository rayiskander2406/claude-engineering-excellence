---
description: Generate changelog from commits
---

# Changelog Generator

Generate a changelog from commits since the last release.

## Changelog Format

Follow [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
# Changelog

## [Unreleased]

## [1.2.0] - 2025-12-12

### Added
- New feature descriptions

### Changed
- Modifications to existing functionality

### Deprecated
- Features that will be removed

### Removed
- Features that were removed

### Fixed
- Bug fixes

### Security
- Security-related fixes
```

## Mapping Conventional Commits

| Commit Type | Changelog Section |
|-------------|-------------------|
| feat | Added |
| fix | Fixed |
| perf | Changed |
| refactor | Changed |
| docs | (usually omit) |
| style | (usually omit) |
| test | (usually omit) |
| chore | (usually omit) |
| BREAKING CHANGE | Changed (highlighted) |
| security fix | Security |

## Guidelines

### Good Changelog Entries
- Written for users, not developers
- Explain impact, not implementation
- Group related changes
- Highlight breaking changes prominently

### Examples

**Good**: "Added dark mode support for better accessibility"
**Bad**: "Added isDarkMode state variable to ThemeContext"

**Good**: "Fixed login failures when using special characters in password"
**Bad**: "Fixed regex bug in validatePassword function"

## Output Format

Generate:
1. **Changelog entries** in proper format
2. **Release summary** (one paragraph for release notes)
3. **Breaking changes** highlighted separately
4. **Migration guide** if there are breaking changes
5. **Contributors** list from commit authors

## Target

$ARGUMENTS

Options:
- No args: Generate from last tag to HEAD
- Version number: Generate for specific version
- Date range: Generate for specific period
