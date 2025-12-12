---
description: Pre-deployment checklist and verification
---

# Pre-Flight Deployment Check

Run pre-deployment checks to ensure safe deployment.

## Pre-Flight Checklist

### Code Quality
- [ ] All tests passing
- [ ] No linting errors
- [ ] No TypeScript/type errors
- [ ] Code review approved
- [ ] No merge conflicts

### Build & Artifacts
- [ ] Build succeeds
- [ ] Artifacts generated correctly
- [ ] Docker image builds (if applicable)
- [ ] No build warnings to address

### Database
- [ ] Migrations tested
- [ ] Migrations are backward compatible
- [ ] Rollback scripts ready
- [ ] Data backups current

### Configuration
- [ ] Environment variables set
- [ ] Feature flags configured
- [ ] Secrets rotated if needed
- [ ] Config changes documented

### Dependencies
- [ ] No known vulnerabilities
- [ ] No breaking dependency changes
- [ ] Lock file committed

### Monitoring
- [ ] Alerts configured
- [ ] Dashboards ready
- [ ] Log aggregation working
- [ ] Error tracking configured

### Documentation
- [ ] Changelog updated
- [ ] API docs updated (if changed)
- [ ] Runbooks updated (if needed)
- [ ] User-facing docs updated

### Communication
- [ ] Team notified
- [ ] Stakeholders informed
- [ ] On-call aware
- [ ] Maintenance window (if needed)

### Rollback Plan
- [ ] Rollback procedure documented
- [ ] Previous version available
- [ ] Rollback tested (recently)
- [ ] Rollback triggers defined

## Deployment Readiness

### Go/No-Go Criteria
| Criterion | Status | Notes |
|-----------|--------|-------|
| All tests pass | | |
| Code review complete | | |
| Migrations tested | | |
| Monitoring ready | | |
| Rollback plan ready | | |

### Risk Assessment
| Risk | Mitigation |
|------|------------|
| | |

## Output Format

Generate:
1. **Checklist status**: All items checked
2. **Blockers**: Any items preventing deployment
3. **Warnings**: Non-blocking concerns
4. **Recommendation**: Go / No-Go / Go with conditions
5. **Post-deployment verification**: What to check after deploy

## Deployment Commands

```bash
# Pre-deployment
[commands to run before deploying]

# Deployment
[deployment command]

# Verification
[commands to verify success]

# Rollback (if needed)
[rollback command]
```

## Target

$ARGUMENTS

Optionally specify:
- Environment (staging, production)
- Specific concerns to check
- Previous deployment issues
