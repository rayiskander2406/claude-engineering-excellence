# Developer Onboarding Guide

> *"Get productive in hours, not weeks."*

Welcome to the team! This guide will get you set up with our engineering practices, Claude Code integration, and the Self-Learning Flywheel that makes our team smarter every day.

---

## Quick Start Checklist

```
[ ] 1. Install Claude Code
[ ] 2. Install MCP Stack (Memory + GitHub + Context7)
[ ] 3. Clone the project
[ ] 4. Initialize your local knowledge graph
[ ] 5. Explore existing team knowledge
[ ] 6. Complete your first task with /retro-capture
```

---

## Step 1: Install Claude Code

If you haven't already:

```bash
# macOS/Linux
npm install -g @anthropic-ai/claude-code

# Or with Homebrew
brew install claude-code
```

Verify installation:
```bash
claude --version
```

---

## Step 2: Install MCP Stack

MCP servers give Claude superpowers. Install the essential stack:

```bash
# Memory - Persistent knowledge across sessions (CRITICAL)
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'

# GitHub - PRs, issues, CI/CD integration
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Context7 - Real-time library documentation
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

**What this gives you:**
- **Memory:** Claude remembers learnings, patterns, and decisions across sessions
- **GitHub:** Create PRs, manage issues, trigger CI/CD without leaving Claude
- **Context7:** Real-time, version-specific documentation for 1000+ libraries

**Verify it's working:**
```bash
claude
# Then in Claude Code:
> mcp__memory__read_graph
# Should return {} or existing entities
```

**Want more?** See [MCP_STACK.md](./MCP_STACK.md) for the complete guide including:
- Database integration (PostgreSQL, MySQL)
- Error monitoring (Sentry)
- E2E testing (Playwright)
- Project management (Linear, Jira)

---

## Step 3: Clone the Project

```bash
git clone <your-project-repo>
cd <project-name>
```

This gives you access to all shared team knowledge:
```
.claude/
├── learnings/      # Team discoveries (git-tracked)
├── patterns/       # Proven solutions (git-tracked)
├── failures/       # What NOT to do (git-tracked)
├── decisions/      # Architecture Decision Records
└── commands/       # Custom slash commands
```

---

## Step 4: Initialize Your Local Knowledge Graph

Start Claude Code in your project and run:

```bash
claude
```

Then initialize your personal knowledge graph with project context:

```
/search-knowledge project overview
```

This indexes the shared team knowledge into your local MCP server for fast queries.

**Optional:** Seed with project-specific entities:

```javascript
// Claude will do this automatically, but you can manually add:
mcp__memory__create_entities([{
  name: "Project: [YOUR PROJECT NAME]",
  entityType: "project",
  observations: [
    "Joined team: [DATE]",
    "Primary focus: [YOUR AREA]"
  ]
}])
```

---

## Step 5: Explore Existing Team Knowledge

Before writing any code, explore what the team has already learned:

### Search for Relevant Knowledge
```
/search-knowledge [topic you'll be working on]
```

### Review Proven Patterns
```bash
# In your terminal
ls .claude/patterns/

# Or in Claude Code
> Show me all patterns in .claude/patterns/
```

### Check Known Failures
```bash
# Don't repeat past mistakes!
cat .claude/failures/what-not-to-do.md
```

### Review Recent Learnings
```bash
# See what the team discovered recently
ls -la .claude/learnings/
```

---

## Step 6: Your First Task with /retro-capture

After completing your first meaningful task:

```
/retro-capture
```

This captures what you learned and adds it to the team's collective intelligence.

**What to capture:**
- Anything that surprised you
- Gotchas you discovered
- Better approaches you found
- Questions that remain

---

## How the Self-Learning Flywheel Works

```
┌─────────────────────────────────────────────────────────────┐
│                    The Flywheel                             │
│                                                             │
│    YOU do work                                              │
│         ↓                                                   │
│    YOU capture learnings (/learn)                           │
│         ↓                                                   │
│    Learnings become patterns (/promote)                     │
│         ↓                                                   │
│    NEXT PERSON starts faster (/search-knowledge)            │
│         ↓                                                   │
│    NEXT PERSON captures more learnings                      │
│         ↓                                                   │
│    Quality compounds exponentially                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Your Responsibilities

| When | Action | Command |
|------|--------|---------|
| Before starting work | Search for existing knowledge | `/search-knowledge` |
| During work | Note discoveries | `/learn` |
| After completing work | Harvest learnings | `/retro-capture` |
| When pattern emerges | Promote to team pattern | `/promote` |

---

## Key Slash Commands to Know

### Daily Use
| Command | Purpose |
|---------|---------|
| `/search-knowledge` | Find what the team already knows |
| `/learn` | Capture a discovery |
| `/retro-capture` | Harvest learnings after completing work |
| `/explain` | Understand unfamiliar code |

### Code Quality
| Command | Purpose |
|---------|---------|
| `/code-review` | Review code before PR |
| `/security-audit` | Check for vulnerabilities |
| `/test-gen` | Generate test cases |

### Collaboration
| Command | Purpose |
|---------|---------|
| `/pr-prep` | Prepare a pull request |
| `/commit` | Generate commit message |
| `/debug` | Systematic debugging |

---

## Project-Specific Context

<!--
CUSTOMIZE THIS SECTION FOR YOUR PROJECT
Replace the placeholders below with your project's specific information
-->

### Architecture Overview
[Link to architecture diagram or description]

### Key Technologies
- **Backend:** [e.g., Java Spring Boot, Node.js]
- **Frontend:** [e.g., React, Vue]
- **Database:** [e.g., PostgreSQL, MongoDB]
- **Infrastructure:** [e.g., AWS, GCP, Kubernetes]

### Important Files
| File | Purpose |
|------|---------|
| `CLAUDE.md` | Project-specific Claude Code instructions |
| `.claude/patterns/` | Proven solutions for this project |
| `docs/adr/` | Architecture Decision Records |

### Team Contacts
| Area | Contact |
|------|---------|
| Architecture questions | [Name/Slack] |
| DevOps/Infrastructure | [Name/Slack] |
| Security | [Name/Slack] |

### Development Workflow
1. Pick up a task from [Task Board Link]
2. Create a feature branch: `git checkout -b feature/[task-id]-description`
3. Develop with Claude Code assistance
4. Run `/code-review` before committing
5. Run `/pr-prep` to prepare your PR
6. Run `/retro-capture` after PR is merged

---

## Common Gotchas

<!--
ADD YOUR PROJECT-SPECIFIC GOTCHAS HERE
These are things that commonly trip up new developers
-->

### 1. [Gotcha Title]
**Problem:** [What goes wrong]
**Solution:** [How to fix/avoid it]

### 2. [Gotcha Title]
**Problem:** [What goes wrong]
**Solution:** [How to fix/avoid it]

---

## Troubleshooting

### MCP Server Not Working

```bash
# Check if MCP is configured
claude mcp list

# Re-add if missing
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
```

### Slash Commands Not Found

```bash
# Ensure commands are in the right place
ls .claude/commands/

# Or check global commands
ls ~/.claude/commands/
```

### Knowledge Graph Empty

```bash
# In Claude Code, initialize with project context
> /search-knowledge initialize project knowledge
```

---

## Getting Help

1. **Search first:** `/search-knowledge [your question]`
2. **Check patterns:** `ls .claude/patterns/`
3. **Ask Claude:** Describe your problem in Claude Code
4. **Ask the team:** [Team Slack Channel]

---

## Your First Week Goals

- [ ] Complete this onboarding guide
- [ ] Successfully run `/search-knowledge` and find relevant knowledge
- [ ] Complete one task end-to-end
- [ ] Capture at least one learning with `/learn`
- [ ] Run `/retro-capture` after your first completed task
- [ ] Ask one question in the team channel (we want to hear from you!)

---

## Welcome to the Team!

Remember: Every learning you capture makes the next person faster. You're not just writing code - you're building institutional knowledge that compounds over time.

*"The best time to capture a learning is when you discover it. The second best time is now."*

---

## Appendix: Full MCP Memory Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `mcp__memory__create_entities` | Add new knowledge | Store a learning or pattern |
| `mcp__memory__create_relations` | Link concepts | Connect related learnings |
| `mcp__memory__search_nodes` | Find knowledge | Query by topic |
| `mcp__memory__read_graph` | See all knowledge | Full graph view |
| `mcp__memory__delete_entity` | Remove outdated info | Clean up |
| `mcp__memory__delete_relation` | Remove connections | Update relationships |

These are used internally by the slash commands, but you can also use them directly in Claude Code for advanced knowledge management.
