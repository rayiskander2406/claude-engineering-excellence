---
description: Generate developer onboarding guide
---

# Developer Onboarding Guide Generator

Create a comprehensive onboarding guide for new team members.

## Onboarding Guide Template

```markdown
# Developer Onboarding Guide

Welcome to [Project Name]! This guide will help you get productive quickly.

## Quick Start (30 minutes)

### 1. Clone and Setup
\`\`\`bash
# Clone the repository
git clone [repo-url]
cd [project-name]

# Install dependencies
[install command]

# Setup environment
cp .env.example .env
# Edit .env with your values
\`\`\`

### 2. Run Locally
\`\`\`bash
[run command]
\`\`\`

### 3. Verify Setup
- [ ] Application starts without errors
- [ ] Can access [URL]
- [ ] Tests pass: [test command]

## Architecture Overview

[Mermaid diagram of system architecture]

### Key Components
| Component | Purpose | Location |
|-----------|---------|----------|
| | | |

### Tech Stack
- **Language**:
- **Framework**:
- **Database**:
- **Cache**:
- **Queue**:

## Codebase Navigation

### Directory Structure
\`\`\`
src/
├── [dir]/          # [purpose]
├── [dir]/          # [purpose]
└── [dir]/          # [purpose]
\`\`\`

### Key Files
| File | Purpose |
|------|---------|
| | |

### Important Patterns
[Explain key patterns used in the codebase]

## Development Workflow

### Daily Development
1. Pull latest: `git pull origin main`
2. Create branch: `git checkout -b feature/[name]`
3. Make changes
4. Run tests: [command]
5. Create PR

### Code Style
- [Linting rules]
- [Formatting standards]
- [Naming conventions]

### Testing
- Unit tests: [command]
- Integration tests: [command]
- E2E tests: [command]

## Common Tasks

### Adding a New Feature
[Step-by-step guide]

### Fixing a Bug
[Step-by-step guide]

### Deploying
[Step-by-step guide]

## Troubleshooting

### Common Issues

**Issue**: [Description]
**Solution**: [Steps]

## Resources

### Documentation
- [Link to docs]

### Communication
- Slack: [channel]
- Meetings: [schedule]

### People to Know
| Role | Name | Contact |
|------|------|---------|
| Tech Lead | | |
| Product Owner | | |

## First Week Checklist

- [ ] Complete environment setup
- [ ] Read architecture documentation
- [ ] Complete first small task
- [ ] Attend team standup
- [ ] Set up 1:1 with mentor
- [ ] Review recent PRs to understand code style
```

## Output

Generate an onboarding guide that:
1. Is specific to this codebase
2. Includes actual commands and paths
3. Has working diagrams
4. Covers common tasks
5. Lists real contacts/resources

## Target

$ARGUMENTS

Optionally specify focus areas or role-specific onboarding needs.
