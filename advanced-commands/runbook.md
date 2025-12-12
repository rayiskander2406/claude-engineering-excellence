---
description: Create operational runbook for a service
---

# Runbook Generator

Create an operational runbook for a service or component.

## Runbook Template

```markdown
# Runbook: [Service Name]

## Overview

**Service**: [Name]
**Owner**: [Team/Person]
**On-Call**: [Rotation/Contact]
**Repository**: [Link]
**Dashboard**: [Link]

### Purpose
What does this service do?

### Dependencies
- Upstream: Services this depends on
- Downstream: Services that depend on this

## Health Checks

### Endpoints
| Endpoint | Expected Response | Timeout |
|----------|-------------------|---------|
| /health | 200 OK | 5s |
| /ready | 200 OK | 5s |

### Key Metrics
| Metric | Normal Range | Alert Threshold |
|--------|--------------|-----------------|
| Response time | < 200ms | > 500ms |
| Error rate | < 0.1% | > 1% |
| CPU usage | < 60% | > 80% |

## Common Issues

### Issue: [High Latency]

**Symptoms**:
- Response time > 500ms
- Timeout errors in logs

**Diagnosis**:
1. Check database connection pool: [command]
2. Check recent deployments: [command]
3. Check external dependencies: [command]

**Resolution**:
1. If connection pool exhausted: [steps]
2. If recent deployment: [steps]
3. If external dependency: [steps]

**Escalation**:
- L1: On-call engineer
- L2: Service owner
- L3: Platform team

### Issue: [Service Unavailable]

**Symptoms**:
- 5xx errors
- Health check failures

**Diagnosis**:
1. Check pod/instance status: [command]
2. Check logs for errors: [command]
3. Check resource usage: [command]

**Resolution**:
1. Restart pods: [command]
2. Scale up: [command]
3. Rollback: [command]

## Operational Procedures

### Deployment
[Steps to deploy a new version]

### Rollback
[Steps to rollback to previous version]

### Scaling
[Steps to scale the service]

### Data Recovery
[Steps to recover from data issues]

## Contacts

| Role | Name | Contact |
|------|------|---------|
| Service Owner | | |
| Tech Lead | | |
| On-Call | | |

## Revision History

| Date | Author | Changes |
|------|--------|---------|
```

## Runbook Best Practices

1. **Assume stress**: Write for someone at 3am during an incident
2. **Be specific**: Include exact commands, not general guidance
3. **Test procedures**: Run through them before you need them
4. **Keep updated**: Review after every incident
5. **Include links**: Dashboards, logs, documentation

## Output

Create a runbook with:
1. All template sections filled in
2. Service-specific commands and checks
3. Common issues based on code analysis
4. Appropriate escalation paths

## Target

$ARGUMENTS

Specify the service or component to create a runbook for.
