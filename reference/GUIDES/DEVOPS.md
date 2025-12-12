# Claude Code Guide for DevOps Engineers

> *"Automate infrastructure, debug production, ship reliably."*

This guide covers Claude Code workflows tailored for DevOps, SRE, and Platform Engineering.

---

## Your DevOps Toolkit

| Task | Command/Approach | When to Use |
|------|------------------|-------------|
| Write IaC | Just ask | Terraform, Pulumi, CloudFormation |
| Debug incidents | `/debug` | Production issues |
| Create runbooks | `/runbook` | New services |
| Post-incident review | `/postmortem` | After incidents |
| Security audit | `/security-audit` | Infrastructure review |
| CI/CD pipelines | Just ask | GitHub Actions, GitLab CI, Jenkins |
| Kubernetes manifests | Just ask | Deployments, services, configs |
| Script automation | Just ask | Bash, Python automation |

---

## Workflow 1: Infrastructure as Code

### Writing Terraform

```
Create Terraform for an AWS EKS cluster with:
- 3 node groups (system, app, spot)
- VPC with private subnets
- ALB ingress controller
- Cluster autoscaler
- Use modules where appropriate
- Include outputs for cluster endpoint and kubeconfig
```

### Best Practice: Ask for Explanations

```
Explain each resource and why it's configured this way.
What are the security implications?
What would need to change for production vs staging?
```

### Reviewing Existing IaC

```
Review this Terraform for:
- Security issues
- Cost optimization opportunities
- Best practices violations
- Missing resources for production readiness

[PASTE TERRAFORM]
```

### Converting Between Formats

```
Convert this CloudFormation to Terraform:
[CLOUDFORMATION YAML]
```

---

## Workflow 2: Kubernetes

### Creating Manifests

```
Create Kubernetes manifests for a Node.js API:
- Deployment with 3 replicas
- HPA (min 3, max 10, target 70% CPU)
- Service (ClusterIP)
- Ingress with TLS
- ConfigMap for environment config
- Secret for API keys
- PodDisruptionBudget
- NetworkPolicy (allow only from ingress)
```

### Debugging Kubernetes Issues

```
My pod is in CrashLoopBackOff. Here's the describe output:

[KUBECTL DESCRIBE OUTPUT]

And the logs:

[KUBECTL LOGS OUTPUT]

Help me diagnose and fix this.
```

### Helm Charts

```
Create a Helm chart for this application with:
- Values for different environments (dev, staging, prod)
- Resource limits configurable
- Ingress optional
- Include NOTES.txt with useful commands
```

### Reviewing Kubernetes Security

```
Review these Kubernetes manifests for security issues:
- Pod security context
- Network policies
- Resource limits
- Secret handling
- RBAC permissions

[PASTE MANIFESTS]
```

---

## Workflow 3: CI/CD Pipelines

### GitHub Actions

```
Create a GitHub Actions workflow for a Node.js monorepo that:
- Runs on push to main and PRs
- Detects which packages changed
- Runs tests only for changed packages
- Builds Docker images with proper tagging
- Pushes to ECR
- Deploys to EKS staging on main
- Requires approval for production
- Includes Slack notifications
```

### GitLab CI

```
Create a GitLab CI pipeline for a Python application:
- Stages: lint, test, build, deploy
- Uses Docker-in-Docker for builds
- Caches pip dependencies
- Runs security scanning (SAST, container scanning)
- Deploys to Kubernetes
- Environment-specific variables
```

### Pipeline Debugging

```
This CI pipeline is failing with:

[ERROR OUTPUT]

The pipeline file is:

[PIPELINE YAML]

Help me fix it.
```

---

## Workflow 4: Incident Response

### During an Incident

```
/debug

Production is down. Symptoms:
- API returning 502 errors
- Started 10 minutes ago
- No recent deployments
- Database connections look normal

Here's what I see in the logs:
[LOGS]

Help me systematically debug this.
```

### Quick Diagnostics Script

```
Write a bash script that quickly checks:
- Pod status across namespaces
- Recent events
- Node resource usage
- PVC status
- Recent deployments
- Ingress health
- Certificate expiry
```

### After the Incident

```
/postmortem

Incident: API outage for 45 minutes
Timeline:
- 14:00 - Alerts fired
- 14:05 - On-call engaged
- 14:15 - Root cause identified (OOM)
- 14:30 - Memory limits increased
- 14:45 - Service recovered

Help me write a blameless postmortem.
```

---

## Workflow 5: Runbooks

### Creating a Runbook

```
/runbook

Create a runbook for the payment-service:
- Health check endpoints
- Common failure modes
- Debugging commands
- Escalation path
- Recovery procedures
- Dependencies
```

### Runbook Template

```
Generate a runbook template for microservices that includes:
- Service overview
- Architecture diagram (mermaid)
- Health checks
- Metrics to watch
- Common issues and fixes
- Escalation contacts
- Deployment procedures
- Rollback procedures
```

---

## Workflow 6: Security & Compliance

### Infrastructure Security Audit

```
/security-audit

Review this infrastructure for security:
- AWS account structure
- IAM policies
- Network architecture
- Secrets management
- Logging and monitoring
- Compliance gaps

[DESCRIBE OR PASTE CONFIGS]
```

### Hardening Scripts

```
Create a security hardening script for Ubuntu servers:
- Disable root SSH
- Configure fail2ban
- Set up unattended upgrades
- Configure firewall (UFW)
- Harden SSH config
- Set up audit logging
- CIS benchmark compliance
```

### Policy as Code

```
Write OPA/Rego policies to enforce:
- All pods must have resource limits
- No containers running as root
- All images from approved registries
- All deployments must have PodDisruptionBudget
- No hostPath mounts allowed
```

---

## Workflow 7: Monitoring & Observability

### Prometheus/Grafana

```
Create Prometheus alerting rules for a web service:
- High error rate (>1% 5xx for 5 minutes)
- High latency (p99 > 500ms for 5 minutes)
- Pod restarts
- High memory usage (>80%)
- Certificate expiring soon
- Database connection pool exhaustion
```

```
Create a Grafana dashboard JSON for a Node.js API showing:
- Request rate
- Error rate
- Latency percentiles
- Active connections
- Memory/CPU usage
- Database query times
```

### Log Analysis

```
Analyze these logs and identify:
- Error patterns
- Performance issues
- Security concerns
- Anomalies

[PASTE LOGS]
```

---

## Workflow 8: Database Operations

### Migration Scripts

```
Create a zero-downtime PostgreSQL migration to:
- Add a new column with default
- Backfill data
- Add index concurrently
- Include rollback steps
```

### Backup/Restore Procedures

```
Create backup and restore procedures for PostgreSQL on Kubernetes:
- Automated daily backups to S3
- Point-in-time recovery
- Cross-region replication
- Restore testing script
- Include runbook documentation
```

### Performance Analysis

```
Analyze this slow query explain plan and suggest optimizations:

[EXPLAIN ANALYZE OUTPUT]

Table schema:
[SCHEMA]
```

---

## Workflow 9: Automation Scripts

### Bash Automation

```
Write a bash script that:
- Rotates logs older than 7 days
- Compresses before archiving
- Uploads to S3
- Cleans up local copies
- Sends Slack notification on failure
- Is idempotent and safe to run multiple times
```

### Python Automation

```
Write a Python script to:
- Query AWS for unused EBS volumes
- Calculate cost savings
- Generate report
- Optionally delete with dry-run mode
- Send to Slack/email
```

### Cross-Platform Tools

```
Create a CLI tool (Python/Click) for our team that:
- Lists all deployments across clusters
- Shows recent releases
- Triggers rollbacks
- Follows logs
- Opens shell in pods
```

---

## Common DevOps Tasks - Quick Reference

### Generate SSL Certificate Commands

```
Generate commands to create a self-signed certificate for development
and a Let's Encrypt certificate for production using certbot.
```

### DNS Debugging

```
Create a DNS debugging checklist and commands for troubleshooting
resolution issues in Kubernetes.
```

### Load Testing

```
Create a k6 load test script for an API that:
- Ramps up to 1000 users
- Tests main endpoints
- Checks for errors and latency
- Outputs results in a report
```

### Cost Optimization

```
Review this AWS bill breakdown and suggest cost optimizations:
[COST DATA]
```

---

## MCP Servers for DevOps

### Essential Stack

```bash
# Memory - remember incidents, runbooks, learnings
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'

# GitHub - manage repos, PRs, actions
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Context7 - up-to-date docs for tools
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

### DevOps-Specific

```bash
# Sentry - error monitoring
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# Database - query production (read-only!)
claude mcp add db -- npx -y @bytebase/dbhub --dsn "postgresql://readonly:pass@host:5432/db"
```

---

## Security Reminders for DevOps

| Never Share | Why |
|-------------|-----|
| AWS credentials | Breach risk |
| Kubeconfig files | Cluster access |
| SSH private keys | Server access |
| Database passwords | Data breach |
| API tokens | Service access |
| TLS private keys | MITM risk |

### Safe Ways to Get Help

```
# BAD
Here's my AWS credentials, debug this

# GOOD
I'm getting AccessDenied on s3:GetObject. Here's the IAM policy (secrets redacted):
[POLICY WITH ARNS REDACTED]
```

---

## Capture DevOps Knowledge

### After Resolving an Incident

```
/learn

Incident: Redis cluster failover
Root cause: Memory pressure from large keys
Solution: Identified and split large keys
Prevention: Added memory alerts, key size monitoring
```

### After Building New Infrastructure

```
/learn

Built multi-region EKS setup
Key decisions:
- Used Karpenter over Cluster Autoscaler for faster scaling
- Global Accelerator for traffic routing
- Crossplane for multi-cluster resources
```

### After Finding a Better Tool/Approach

```
/learn

Replaced custom deployment script with ArgoCD
Benefits:
- GitOps workflow
- Automatic sync
- Better rollback
- UI for visibility
```

---

## DevOps Daily Habits

| Morning | During Work | End of Day |
|---------|-------------|------------|
| Check alerts/dashboards | Document as you go | `/retro-capture` |
| Review overnight incidents | `/runbook` for new services | Update runbooks |
| `/search-knowledge` for context | `/postmortem` after incidents | Share learnings |

---

*"Automate yourself out of toil, not out of a job. Use Claude to handle the repetitive, so you can focus on the impactful."*
