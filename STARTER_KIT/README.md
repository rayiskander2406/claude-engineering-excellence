# Claude Code Starter Kit

> *One command to add Claude Code superpowers to any project.*

This starter kit configures your project with:
- EdTech compliance rules (FERPA, COPPA, GDPR, SOC 2, ISO 27001)
- Self-learning flywheel (knowledge capture)
- Stack-specific patterns (Java, React, .NET, Vue)
- Pre-commit security hooks
- Architecture Decision Records

---

## Quick Start

```bash
# From your project root
curl -sSL https://raw.githubusercontent.com/edutone/claude-engineering-excellence/main/STARTER_KIT/setup.sh | bash
```

Or manually:

```bash
# Clone and copy
git clone https://github.com/edutone/claude-engineering-excellence.git /tmp/cee
cp -r /tmp/cee/STARTER_KIT/.claude .
cp -r /tmp/cee/STARTER_KIT/.hooks .
cp -r /tmp/cee/STARTER_KIT/docs .
rm -rf /tmp/cee

# Install hooks
chmod +x .hooks/*
git config core.hooksPath .hooks
```

---

## What's Included

```
your-project/
├── .claude/
│   ├── CLAUDE.md                # Project instructions with EdTech compliance
│   ├── commands/                # Self-learning flywheel commands
│   │   ├── learn.md
│   │   ├── promote.md
│   │   ├── search-knowledge.md
│   │   └── retro-capture.md
│   ├── learnings/               # Team discoveries
│   │   └── .gitkeep
│   ├── patterns/                # Proven solutions
│   │   ├── .gitkeep
│   │   ├── TEMPLATE.md
│   │   ├── java-patterns.md
│   │   ├── react-patterns.md
│   │   ├── dotnet-patterns.md
│   │   └── vue-patterns.md
│   └── failures/                # What NOT to do
│       ├── .gitkeep
│       └── TEMPLATE.md
├── .hooks/
│   ├── pre-commit               # Block secrets, enforce standards
│   └── commit-msg               # Enforce conventional commits
└── docs/
    └── adr/
        ├── TEMPLATE.md
        └── 0001-use-claude-code.md
```

---

## After Setup

### 1. Customize CLAUDE.md

Edit `.claude/CLAUDE.md` and fill in:
- `[PROJECT_NAME]` - Your project name
- `[TECH_STACK]` - Your technologies
- `[TEAM_CHANNEL]` - Your Slack/Teams channel
- Any project-specific rules

### 2. Install MCP Servers

```bash
# Essential stack (everyone)
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
claude mcp add github -- npx -y @modelcontextprotocol/server-github
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

### 3. Select Your Stack Pattern

The starter kit includes patterns for:
- **Java** - Spring Boot, JPA, security
- **React** - Hooks, state management, testing
- **.NET** - ASP.NET Core, Entity Framework
- **Vue** - Composition API, Pinia, testing

Delete the patterns you don't need, keep the ones you do.

### 4. First Commit

```bash
git add .claude docs .hooks
git commit -m "chore: Add Claude Code starter kit with EdTech compliance"
```

---

## EdTech Compliance Built-In

The CLAUDE.md includes mandatory rules for:

| Regulation | What It Covers |
|------------|----------------|
| **FERPA** | Student education records |
| **COPPA** | Children under 13 |
| **SOPIPA** | California student data |
| **NY Ed Law 2-d** | New York student data |
| **GDPR** | EU residents |
| **SOC 2** | Security controls |
| **ISO 27001** | Information security |

Claude will be reminded of these requirements on every session.

---

## Pre-Commit Hooks

The `.hooks/pre-commit` script blocks:
- API keys and secrets
- AWS credentials
- Private keys
- Database connection strings with passwords
- Student PII patterns

To bypass (use sparingly):
```bash
git commit --no-verify -m "message"
```

---

## Customization

### Adding Project-Specific Rules

Edit `.claude/CLAUDE.md`:

```markdown
## Project-Specific Rules

- All API endpoints must require authentication
- Use [YOUR LOGGING LIBRARY] for all logging
- Database queries must use parameterized statements
```

### Adding Custom Patterns

Create `.claude/patterns/your-pattern.md`:

```markdown
# Pattern: [NAME]

## Problem
What problem does this solve?

## Solution
The recommended approach.

## When to Use
- Scenario 1
- Scenario 2

## Examples
[Code examples]
```

### Adding Custom Slash Commands

Create `.claude/commands/your-command.md`:

```markdown
---
description: What this command does
---

Your prompt template here.

$ARGUMENTS
```

---

## Team Adoption

1. **Tech Lead**: Run setup, customize CLAUDE.md, commit
2. **Team**: Pull, install MCP servers, start using
3. **Everyone**: Capture learnings with `/learn`
4. **Weekly**: Review learnings, promote patterns

---

## Support

- **Documentation**: https://github.com/edutone/claude-engineering-excellence
- **FAQ**: See FAQ.md in the main repo
- **Issues**: Open a GitHub issue

---

*"Start every project with the wisdom of the team."*
