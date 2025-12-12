---
description: Security vulnerability assessment (OWASP Top 10)
---

# Security Audit

Perform a comprehensive security audit of the codebase or specified files.

## Audit Checklist

### OWASP Top 10

1. **Injection** (SQL, NoSQL, OS, LDAP)
   - Are queries parameterized?
   - Is user input properly escaped?

2. **Broken Authentication**
   - Password storage (bcrypt/argon2, not MD5/SHA1)?
   - Session management secure?
   - Multi-factor authentication available?

3. **Sensitive Data Exposure**
   - Secrets in code or config files?
   - Data encrypted at rest and in transit?
   - PII properly protected?

4. **XML External Entities (XXE)**
   - XML parsing configured safely?

5. **Broken Access Control**
   - Authorization checks on all endpoints?
   - Direct object reference vulnerabilities?
   - CORS configured correctly?

6. **Security Misconfiguration**
   - Debug mode disabled in production?
   - Default credentials removed?
   - Security headers present (CSP, HSTS, X-Frame-Options)?

7. **Cross-Site Scripting (XSS)**
   - Output encoding context-aware?
   - React/Vue/Angular XSS protections intact?

8. **Insecure Deserialization**
   - Untrusted data deserialized safely?

9. **Using Components with Known Vulnerabilities**
   - Dependencies up to date?
   - Known CVEs in dependencies?

10. **Insufficient Logging & Monitoring**
    - Security events logged?
    - Audit trail for sensitive operations?

### Additional Checks

- **Secrets Management**: No hardcoded credentials, API keys, or tokens
- **Input Validation**: Whitelist validation, not blacklist
- **Error Handling**: Errors don't leak sensitive information
- **Cryptography**: Strong algorithms, proper key management
- **File Uploads**: Validated, sanitized, stored safely

## Output Format

For each vulnerability:
1. **Severity**: Critical / High / Medium / Low
2. **Location**: File and line
3. **Vulnerability Type**: CWE ID if applicable
4. **Description**: What's vulnerable
5. **Proof of Concept**: How it could be exploited
6. **Remediation**: How to fix it

End with executive summary suitable for stakeholders.

## Target

$ARGUMENTS

If no target specified, audit the entire codebase with focus on authentication, API endpoints, and data handling.
