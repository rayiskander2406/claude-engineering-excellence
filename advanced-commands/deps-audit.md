---
description: Audit dependencies for security and health
---

# Dependency Audit

Audit project dependencies for security vulnerabilities, license compliance, and maintenance health.

## Audit Categories

### 1. Security Vulnerabilities
- Known CVEs in dependencies
- Severity levels (Critical, High, Medium, Low)
- Available patches/updates
- Transitive vulnerability exposure

### 2. License Compliance
- License types detected
- Compatibility with project license
- Copyleft vs permissive
- Commercial use restrictions

### 3. Maintenance Health
- Last update date
- Open issues count
- Maintainer activity
- Bus factor (single maintainer risk)

### 4. Version Currency
- How far behind latest?
- Breaking changes in updates
- Deprecated dependencies
- End-of-life packages

## Risk Indicators

### Red Flags
- Known security vulnerabilities (unpatched)
- No updates in 2+ years
- Deprecated with no replacement
- Single maintainer, inactive
- License incompatibility
- Archived repository

### Yellow Flags
- Updates available (not critical)
- Minor version behind
- Low download counts
- Limited documentation
- Few maintainers

### Green Flags
- Active development
- Regular releases
- Good documentation
- Healthy community
- Clear license

## Output Format

### Summary
| Category | Status | Count |
|----------|--------|-------|
| Critical vulnerabilities | | |
| High vulnerabilities | | |
| License issues | | |
| Outdated (major) | | |
| Unmaintained | | |

### Critical Issues
Require immediate attention:
1. [Dependency]: [Issue] - [Remediation]

### Recommended Updates
Safe to update:
1. [Dependency]: [Current] → [Latest]

### License Report
| Dependency | License | Compatible |
|------------|---------|------------|
| | | |

### Health Concerns
Dependencies with maintenance concerns:
1. [Dependency]: [Concern] - [Alternative]

### Action Plan
Prioritized list of dependency actions.

## Target

$ARGUMENTS

Options:
- No args: Audit all dependencies
- Package name: Audit specific dependency
- "security": Focus on security only
- "licenses": Focus on licenses only
