---
description: Performance audit and optimization recommendations
---

# Performance Audit

Analyze code for performance issues and optimization opportunities.

## Performance Categories

### Database Performance
- N+1 queries
- Missing indexes
- Unoptimized queries
- Connection pool issues
- Transaction scope

### Application Performance
- Algorithm complexity (O(n²) when O(n) possible)
- Unnecessary iterations
- Memory allocation in hot paths
- Blocking operations
- Missing caching

### Frontend Performance
- Bundle size
- Render blocking resources
- Unnecessary re-renders
- Image optimization
- Code splitting opportunities

### API Performance
- Response payload size
- Missing pagination
- Over-fetching
- Missing compression
- Caching headers

### Infrastructure
- Missing CDN
- Suboptimal region placement
- Resource under/over-provisioning
- Missing auto-scaling

## Analysis Techniques

### Static Analysis
- Code patterns that indicate performance issues
- Complexity analysis
- Dependency analysis

### Runtime Analysis (Recommendations)
- Where to add profiling
- What metrics to collect
- How to interpret results

## Output Format

### Executive Summary
Overall performance assessment and top concerns.

### Issues Found
For each issue:
1. **Severity**: Critical / Major / Minor
2. **Location**: File and line
3. **Issue**: What's the performance problem
4. **Impact**: How bad is it? (with estimates if possible)
5. **Recommendation**: How to fix it
6. **Effort**: S/M/L/XL

### Quick Wins
Low-effort, high-impact optimizations.

### Strategic Improvements
Larger optimizations requiring more investment.

### Monitoring Recommendations
What metrics to track going forward.

## Target

$ARGUMENTS

Specify the area to audit: a file, module, feature, or the entire codebase.
