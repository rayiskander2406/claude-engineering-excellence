# Claude Code Guide for Tech Leads

> *"Multiply your impact. Elevate your team. Ship quality at scale."*

This guide covers Claude Code workflows for Tech Leads, Engineering Managers, and Architects who need to balance hands-on work with team leadership.

---

## Your Leadership Toolkit

| Task | Command/Approach | When to Use |
|------|------------------|-------------|
| Architecture decisions | `/adr` | Major technical decisions |
| Code review | `/code-review` | PR reviews |
| Onboarding docs | `/onboard` | New team members |
| Technical research | `/research` | Evaluating technologies |
| Incident review | `/postmortem` | After incidents |
| Sprint planning | Just ask | Estimation, planning |
| 1:1 prep | Just ask | Team meetings |
| Documentation | `/doc-gen` | Technical docs |

---

## Workflow 1: Architecture Decisions

### Creating ADRs

```
/adr

We need to decide on a message queue for our event-driven architecture.

Context:
- 50,000 events/day currently, growing to 500,000
- Need at-least-once delivery
- Events must be ordered within a partition
- Team has AWS experience
- Budget: $500/month

Options considered:
- AWS SQS + SNS
- Apache Kafka (MSK)
- RabbitMQ
- Redis Streams

Help me create an ADR.
```

### Reviewing Architecture Proposals

```
Review this architecture proposal for:
- Scalability concerns
- Single points of failure
- Operational complexity
- Cost implications
- Team capability match
- Security considerations

[PROPOSAL]
```

### System Design Sessions

```
I'm designing a notification system that needs to:
- Support email, SMS, push, in-app
- Handle 1M notifications/day
- Allow user preferences
- Support templating
- Provide delivery tracking

Help me think through the architecture. Ask me questions to understand requirements better.
```

---

## Workflow 2: Code Review at Scale

### Reviewing PRs Efficiently

```
Review this PR focusing on:
- Security vulnerabilities
- Performance implications
- Breaking changes
- Test coverage gaps
- Architecture alignment

[DIFF]
```

### Training Others on Code Review

```
Generate a code review checklist for my team that covers:
- Security
- Performance
- Maintainability
- Testing
- Documentation
- Accessibility

Format it as a PR template.
```

### Pattern Recognition Across PRs

```
I've noticed these recurring issues in code reviews:
- Missing error handling
- Inconsistent naming
- No input validation

Help me:
1. Create a document explaining the standards
2. Add rules to our CLAUDE.md
3. Create a pre-commit check
```

---

## Workflow 3: Team Onboarding

### Creating Onboarding Materials

```
/onboard

Create an onboarding guide for new developers joining our team.

Tech stack:
- TypeScript/Node.js backend
- React frontend
- PostgreSQL
- Kubernetes on AWS

Key systems:
- User service
- Payment service
- Notification service

Include:
- Environment setup
- Architecture overview
- Key workflows
- Who to ask for what
```

### Onboarding Checklist

```
Generate a first-month onboarding checklist:
- Week 1: Setup and orientation
- Week 2: First bug fix
- Week 3: First feature
- Week 4: First code review

Include checkpoints and success criteria.
```

### Knowledge Transfer

```
I'm leaving the team in 4 weeks. Help me create a knowledge transfer plan:

I own:
- Payment integration
- CI/CD pipelines
- Database migrations

Include:
- Documentation needed
- Pairing sessions
- Handoff timeline
```

---

## Workflow 4: Technical Research

### Technology Evaluation

```
/research

Evaluate state management options for our React application.

Current state:
- 50 components
- 20 developers
- Mix of REST and GraphQL
- Need offline support

Options:
- Redux Toolkit
- Zustand
- Jotai
- React Query + Context

Compare on: Learning curve, performance, bundle size, team fit.
```

### Build vs Buy

```
We need a feature flagging system. Help me evaluate:
- Build custom solution
- LaunchDarkly
- Split.io
- Unleash (self-hosted)
- Flagsmith

Requirements:
- 100 flags
- User targeting
- A/B testing
- Audit log
- SSO
```

### Migration Planning

```
We need to migrate from Express to Fastify.

Help me create a migration plan:
- Risk assessment
- Incremental approach
- Testing strategy
- Rollback plan
- Timeline considerations
```

---

## Workflow 5: Team Productivity

### Improving Development Velocity

```
Analyze our development workflow for bottlenecks:

Current flow:
1. Pick up JIRA ticket
2. Create branch
3. Develop locally
4. Push, CI runs (15 min)
5. Code review (avg 2 days)
6. Merge to main
7. Deploy to staging (manual)
8. QA verification
9. Deploy to prod (manual)

Where are the opportunities?
```

### Standardizing Practices

```
Help me create standards for our team:

1. PR size guidelines
2. Commit message format
3. Branch naming
4. Documentation requirements
5. Test coverage expectations

Make them practical and enforceable.
```

### Claude Code Rollout Strategy

```
I'm rolling out Claude Code to a team of 20 developers.

Help me create:
1. Phased rollout plan
2. Training curriculum
3. Success metrics
4. Support structure
5. Feedback collection
```

---

## Workflow 6: Incident Management

### During Incidents

```
We have a P1 incident:
- API latency spiked 10x
- 30% of requests failing
- Started 20 minutes ago
- Recent deployment 2 hours ago

Help me structure the incident response:
- Immediate actions
- Communication plan
- Investigation priorities
- Rollback decision criteria
```

### Post-Incident Review

```
/postmortem

Create a blameless postmortem:

Incident: Payment processing down for 45 minutes
Impact: $50K in failed transactions, 500 affected users
Root cause: Database connection pool exhaustion
Resolution: Increased pool size, added circuit breaker

Include:
- Timeline
- Root cause analysis
- What went well
- What to improve
- Action items
```

### Incident Pattern Analysis

```
Review our last 10 incidents:

[LIST INCIDENTS]

Identify:
- Common themes
- Systemic issues
- Process gaps
- Investment priorities
```

---

## Workflow 7: Technical Documentation

### Architecture Documentation

```
Generate architecture documentation for our system:

Components:
- API Gateway
- User Service
- Order Service
- Notification Service
- PostgreSQL
- Redis
- Kafka

Include:
- System context diagram (Mermaid)
- Component diagram
- Data flow
- Key decisions and rationale
```

### API Documentation

```
Generate API documentation for this service:

[OPENAPI SPEC OR CODE]

Include:
- Overview
- Authentication
- Endpoints
- Error codes
- Rate limits
- Examples
```

### Runbooks for On-Call

```
/runbook

Create runbooks for the team covering:
- Service health checks
- Common failure modes
- Debugging procedures
- Escalation paths
- Recovery procedures
```

---

## Workflow 8: Team Communication

### Technical Writing

```
Help me write a technical proposal for:

Moving from monolith to microservices

Audience: Engineering leadership
Goal: Get buy-in and budget

Include:
- Problem statement
- Proposed solution
- Benefits
- Risks and mitigations
- Resource requirements
- Timeline
```

### Status Updates

```
Generate a weekly status update from:

Completed:
- [LIST]

In progress:
- [LIST]

Blocked:
- [LIST]

Risks:
- [LIST]

Format for: Executive audience
```

### RFC Writing

```
Help me write an RFC for:

Implementing a new caching layer

Include:
- Background
- Problem statement
- Proposed solution
- Alternatives considered
- Open questions
- Timeline
```

---

## Workflow 9: Mentoring & Growth

### Code Review Feedback

```
Turn this code review feedback into a learning opportunity:

Issue: Nested callbacks causing callback hell
Code: [CODE]

Generate:
1. Constructive feedback for the PR
2. A short explainer on the better pattern
3. A team-wide tip (without calling out individual)
```

### Career Development

```
Help me prepare for a 1:1 with a senior engineer who wants to grow into tech lead.

Their strengths:
- Strong coding skills
- Good system design
- Quiet in meetings

Areas to develop:
- Communication
- Influence without authority
- Mentoring

Generate discussion topics and growth actions.
```

### Knowledge Sharing

```
Create a "lunch and learn" presentation outline on:

Topic: Database indexing strategies
Audience: Mid-level developers
Duration: 30 minutes

Include:
- Key concepts
- Common mistakes
- Hands-on examples
- Discussion questions
```

---

## Multiplier Practices

### Capture and Scale Knowledge

```
I just helped a developer solve a complex problem.

Problem: [DESCRIBE]
Solution: [DESCRIBE]

Help me turn this into:
1. A learning entry for our knowledge base
2. A pattern if it's reusable
3. An update to our CLAUDE.md if it's a guideline
```

### Create Reusable Tools

```
I keep helping the team with database migrations.

Create:
1. A checklist for safe migrations
2. A slash command for Claude to help with migrations
3. Documentation for the team
```

### Improve Team CLAUDE.md

```
Based on the code review feedback I've given this month:

[LIST OF COMMON FEEDBACK]

Update our project's CLAUDE.md to:
1. Prevent these issues proactively
2. Add patterns to follow
3. Add anti-patterns to avoid
```

---

## Strategic Thinking Prompts

### Technical Strategy

```
Help me think through our technical strategy for next year.

Current state:
- Monolith with some services
- Manual deployments
- Basic monitoring
- 15 developers

Goals:
- Scale to 100 developers
- 10x traffic growth
- 99.9% availability

What should we prioritize?
```

### Tech Debt Assessment

```
/tech-debt

Assess our technical debt:

[DESCRIBE SYSTEM]

Prioritize by:
- Impact on velocity
- Risk to reliability
- Cost to fix
- Strategic importance
```

### Team Structure

```
We're growing from 15 to 30 engineers.

Current: 2 teams (backend, frontend)

Help me think through:
- Team topology options
- Ownership boundaries
- Communication patterns
- Tooling needs
```

---

## Lead by Example

### Model Good Claude Usage

```
# Do this in PRs:
"Claude helped me identify this edge case, but I verified with [evidence]"

# Share prompts that worked:
"Here's a useful prompt for database optimization: ..."

# Capture learnings publicly:
/learn (and share with team)
```

### Establish Team Norms

| Norm | Why | How to Enforce |
|------|-----|----------------|
| Review all Claude code | Ownership | PR checklist |
| No secrets in prompts | Security | Training |
| Capture learnings | Growth | Sprint ritual |
| Share useful prompts | Efficiency | Slack channel |

---

## Tech Lead Daily Habits

| Morning | During Work | End of Week |
|---------|-------------|-------------|
| Review PRs queue | `/code-review` critical PRs | `/retro-capture` |
| Check team blockers | Architecture decisions | Update documentation |
| `/search-knowledge` for context | Mentor through Claude examples | Share learnings |

---

*"Your job is to make your team successful. Use Claude to do more of what only you can do: decisions, mentorship, strategy."*
