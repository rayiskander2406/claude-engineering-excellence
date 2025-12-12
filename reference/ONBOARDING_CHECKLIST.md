# Claude Code Onboarding Checklist

> Your structured path from zero to productive in 5 days

---

## Overview

This checklist guides you through adopting Claude Code step-by-step. Each day builds on the previous, ensuring you develop solid habits from the start.

**Time commitment:** ~30-45 minutes per day for 5 days

---

## Before You Start

### Prerequisites

- [ ] You have a terminal/command line you're comfortable with
- [ ] You have Node.js 18+ installed (`node --version`)
- [ ] You have git configured with your identity
- [ ] You have access to your team's repositories

### Get Your Bearings

- [ ] Read the [USAGE_POLICY.md](./USAGE_POLICY.md) - understand what you CAN and MUST NOT do
- [ ] Know who to contact for help: _________________ (fill in)
- [ ] Bookmark this checklist - you'll return to it daily

---

## Day 1: Installation & First Conversation

**Goal:** Get Claude Code running and have your first successful interaction

### Installation (15 min)

- [ ] Install Claude Code:
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```

- [ ] Verify installation:
  ```bash
  claude --version
  ```

- [ ] Authenticate:
  ```bash
  claude auth
  ```

- [ ] Navigate to a project you're working on:
  ```bash
  cd /path/to/your/project
  ```

- [ ] Start Claude Code:
  ```bash
  claude
  ```

### First Interaction (15 min)

- [ ] Ask Claude to explain a file you're familiar with:
  ```
  Explain what src/[some-file-you-know].ts does
  ```

- [ ] Verify the explanation is accurate (you know this code!)

- [ ] Ask a follow-up question about the same file

- [ ] Try a simple task:
  ```
  Add a comment explaining the main function in [file]
  ```

- [ ] Review what Claude generated - don't accept blindly!

### Reflection

- [ ] Write down one thing that surprised you (good or bad)
- [ ] Write down one question you have

**Day 1 Complete!** You've installed Claude Code and had your first conversation.

---

## Day 2: Core Workflow & Safety

**Goal:** Learn the review-before-commit workflow and safety practices

### The Golden Rule (10 min)

Read and internalize:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Claude generates  →  YOU review  →  YOU commit           │
│                              ↑                              │
│                    YOU are responsible                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

- [ ] I understand that I own all code I commit, regardless of who/what generated it
- [ ] I will review every line before committing
- [ ] I will not commit code I don't understand

### Practice Safe Prompting (15 min)

**What you CAN share:**
- [ ] Your team's source code
- [ ] Error messages (sanitized)
- [ ] Stack traces (sanitized)
- [ ] Architecture questions

**What you MUST NOT share:**
- [ ] API keys, passwords, tokens
- [ ] Customer data or PII
- [ ] Production database contents
- [ ] Contents of `.env` files

- [ ] Practice: Take a log snippet with an email in it, sanitize it, then share with Claude

### Real Task (20 min)

- [ ] Pick a small bug or task from your backlog

- [ ] Describe the problem to Claude:
  ```
  I'm seeing [error] when [action]. The relevant code is in [file].
  Can you help me understand what's causing this?
  ```

- [ ] Review Claude's analysis

- [ ] If Claude suggests a fix, review it carefully:
  - [ ] Does it make sense?
  - [ ] Are there edge cases?
  - [ ] Does it follow team conventions?

- [ ] Make the fix (with modifications if needed)

- [ ] Test locally before committing

**Day 2 Complete!** You understand the safety workflow.

---

## Day 3: Power Features

**Goal:** Learn slash commands and productivity boosters

### Essential Slash Commands (20 min)

Try each of these:

- [ ] `/help` - See all available commands
  ```
  /help
  ```

- [ ] Code review before committing:
  ```
  /code-review
  ```
  Review Claude's feedback on your staged changes

- [ ] Prepare a PR description:
  ```
  /pr-prep
  ```

- [ ] Security check:
  ```
  /security-audit src/auth/
  ```

### MCP Servers (15 min)

Install the essential MCP servers:

- [ ] Memory server (persistent context):
  ```bash
  claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
  ```

- [ ] Verify it's working:
  ```bash
  claude mcp list
  ```

- [ ] Test memory by asking Claude to remember something:
  ```
  Remember that our team's deployment day is Thursday
  ```

- [ ] In a new session, ask:
  ```
  What day does our team deploy?
  ```

### Keyboard Shortcuts (5 min)

- [ ] `Ctrl+C` - Cancel current generation
- [ ] `Ctrl+D` - Exit Claude Code
- [ ] `Tab` - Accept suggestion
- [ ] Up arrow - Previous prompt

**Day 3 Complete!** You know the power features.

---

## Day 4: Team Knowledge & Patterns

**Goal:** Connect to team knowledge and start contributing

### Explore Team Patterns (15 min)

- [ ] Browse `.claude/patterns/` in your project:
  ```bash
  ls -la .claude/patterns/
  ```

- [ ] Read at least 2 patterns relevant to your work

- [ ] Try using a pattern:
  ```
  I need to add a new API endpoint. Show me how following our
  team's patterns in .claude/patterns/
  ```

### Search Existing Knowledge (10 min)

- [ ] Use the search command:
  ```
  /search-knowledge authentication
  ```

- [ ] Try another search relevant to your current work

### Capture Your First Learning (15 min)

As you work today, when you discover something useful:

- [ ] Use `/learn` to capture it:
  ```
  /learn
  ```

- [ ] Follow the prompts to document:
  - What you learned
  - Why it matters
  - Example code (if applicable)

- [ ] Verify your learning was saved:
  ```bash
  ls -la .claude/learnings/
  ```

### Review the Flywheel (5 min)

Understand how knowledge compounds:

```
Work → Capture (/learn) → Patterns (/promote) → Reuse → Faster Work
        ↑                                                    │
        └────────────────────────────────────────────────────┘
```

- [ ] I understand that capturing learnings helps the whole team
- [ ] I will use `/learn` when I discover something useful

**Day 4 Complete!** You're connected to team knowledge.

---

## Day 5: Advanced Usage & Independence

**Goal:** Handle complex tasks and know where to get help

### Complex Task Practice (25 min)

- [ ] Pick a larger task (feature, refactor, or investigation)

- [ ] Break it down with Claude:
  ```
  I need to [describe task]. Help me break this into steps.
  ```

- [ ] Work through the steps, using Claude as a collaborator

- [ ] Practice saying "no" to Claude:
  - If a suggestion doesn't fit, explain why and ask for alternatives
  - If code doesn't follow conventions, point it out

- [ ] Complete the task with your judgment guiding Claude's assistance

### Debugging Session (10 min)

- [ ] Find or create a bug

- [ ] Practice the debugging workflow:
  ```
  I'm getting [error]. Here's the stack trace: [sanitized trace]
  The relevant code is in [file]. What might cause this?
  ```

- [ ] Follow Claude's debugging suggestions

- [ ] Fix the issue

### Know Your Limits (5 min)

Claude Code is NOT good for:
- [ ] Security decisions (always get human review)
- [ ] Legal/compliance decisions
- [ ] Architecture decisions (use as input, not oracle)
- [ ] Anything requiring real-time data

When stuck:
- [ ] I know to ask in [TEAM_CHANNEL]
- [ ] I know to check FAQ.md
- [ ] I know to escalate security concerns to [SECURITY_CONTACT]

### Graduation Checklist

- [ ] I can install and configure Claude Code
- [ ] I understand the review-before-commit workflow
- [ ] I know what data is safe to share (and what isn't)
- [ ] I can use slash commands effectively
- [ ] I know how to access and contribute to team knowledge
- [ ] I know where to get help when stuck

**Day 5 Complete!** You're ready for independent use.

---

## Post-Onboarding

### First Week After Onboarding

- [ ] Capture at least 2 learnings with `/learn`
- [ ] Use `/code-review` on every PR
- [ ] Attend the team workshop (if scheduled)
- [ ] Ask at least one question in [TEAM_CHANNEL]

### First Month Goals

- [ ] Comfortable using Claude Code daily
- [ ] Captured 5+ learnings
- [ ] Helped a teammate get started
- [ ] Provided feedback on what's working/not working

### Ongoing Habits

| Daily | Weekly | Monthly |
|-------|--------|---------|
| Use `/code-review` | Capture learnings | Review satisfaction survey |
| Review before commit | Search for patterns | Share feedback |
| Stay within policy | Help teammates | Suggest improvements |

---

## Quick Reference

### Commands You'll Use Most

| Command | When to Use |
|---------|-------------|
| `/code-review` | Before every commit |
| `/pr-prep` | When creating PRs |
| `/learn` | When you discover something useful |
| `/search-knowledge` | Before starting new work |
| `/security-audit` | On auth/security code |

### Getting Help

| Question Type | Where to Go |
|---------------|-------------|
| How do I...? | FAQ.md, then [TEAM_CHANNEL] |
| Is this allowed? | USAGE_POLICY.md |
| Security concern | [SECURITY_CONTACT] immediately |
| Bug in Claude Code | [TEAM_CHANNEL] |

---

## Sign-Off

**I have completed the Claude Code onboarding checklist.**

Name: _______________________

Date: _______________________

Manager/Buddy: _______________________

---

*"The goal isn't to use Claude Code a lot. It's to use it well."*
