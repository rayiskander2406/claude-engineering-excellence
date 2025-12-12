---
description: API design review and consistency check
---

# API Design Review

Review API design for consistency, usability, and best practices.

## Review Criteria

### RESTful Design
- Resource-based URLs (nouns, not verbs)
- Proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Appropriate status codes
- Consistent URL patterns

### Naming Conventions
- Consistent casing (camelCase, snake_case)
- Plural vs singular consistency
- Clear, descriptive names
- Abbreviations avoided or consistent

### Request/Response Design
- Consistent response envelope
- Proper error format
- Pagination for lists
- Filtering and sorting support
- Field selection (sparse fieldsets)

### Versioning
- Version strategy present
- Backward compatibility considered
- Deprecation approach defined

### Security
- Authentication required where appropriate
- Authorization documented
- Rate limiting present
- CORS configured correctly
- Input validation documented

### Documentation
- All endpoints documented
- Request/response examples
- Error codes explained
- Authentication explained

## Best Practice Checklist

- [ ] URLs are resource-based
- [ ] HTTP methods match actions
- [ ] Status codes are appropriate
- [ ] Pagination present for lists
- [ ] Consistent error format
- [ ] Authentication documented
- [ ] Rate limits documented
- [ ] Versioning strategy clear
- [ ] No sensitive data in URLs
- [ ] Idempotency considered

## Output Format

### Summary
Overall API quality assessment.

### Consistency Issues
Inconsistencies in naming, format, or patterns.

### Design Issues
Deviations from RESTful best practices.

### Security Concerns
Potential security issues.

### Usability Issues
Things that make the API harder to use.

### Recommendations
Prioritized list of improvements.

### Example Corrections
Before/after examples for key fixes.

## Target

$ARGUMENTS

Specify the API to review: OpenAPI spec, route files, or endpoint descriptions.
