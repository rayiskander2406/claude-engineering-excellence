# Claude Code Cheat Sheet

> Print this. Keep it visible. Reference it daily.

---

## Quick Start

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Authenticate
claude auth

# Start (in your project directory)
claude
```

---

## Essential Commands

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/help` | Show all commands | When lost |
| `/code-review` | Review staged changes | Before every commit |
| `/pr-prep` | Generate PR description | Creating pull requests |
| `/security-audit [path]` | Security analysis | Auth code, sensitive areas |
| `/learn` | Capture a discovery | When you learn something useful |
| `/search-knowledge [topic]` | Search team knowledge | Before starting new work |
| `/explain [file]` | Explain code | Understanding unfamiliar code |
| `/test-gen [file]` | Generate tests | Adding test coverage |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current generation |
| `Ctrl+D` | Exit Claude Code |
| `Tab` | Accept suggestion |
| `↑` / `↓` | Navigate prompt history |
| `Esc` | Clear current input |

---

## The Golden Rule

```
┌────────────────────────────────────────────┐
│                                            │
│   Claude generates → YOU review → YOU own  │
│                                            │
│   Never commit code you don't understand   │
│                                            │
└────────────────────────────────────────────┘
```

---

## Safe to Share

| YES | NO |
|-----|-----|
| Your source code | API keys, passwords, tokens |
| Error messages (sanitized) | Customer data / PII |
| Stack traces (sanitized) | Contents of `.env` files |
| Architecture questions | Production database data |
| Open source code | Competitor code |

---

## Prompt Patterns That Work

### Explain Code
```
Explain what [file/function] does, focusing on [aspect]
```

### Debug
```
I'm getting [error] when [action].
The relevant code is in [file].
What might cause this?
```

### Generate Code
```
Create a [thing] that [requirements].
Follow the patterns in .claude/patterns/
```

### Review
```
Review this code for [security/performance/readability].
Focus especially on [concern].
```

### Refactor
```
Refactor [file/function] to [goal].
Keep the same behavior but improve [aspect].
```

---

## Before Every Commit

```
[ ] I reviewed every line
[ ] I understand what it does
[ ] I tested it locally
[ ] No hardcoded secrets
[ ] No security issues
[ ] Follows team conventions
```

---

## MCP Servers

```bash
# Memory (persistent context)
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'

# GitHub integration
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# List installed
claude mcp list
```

---

## When Things Go Wrong

| Problem | Solution |
|---------|----------|
| Claude is wrong | Say so! Ask for alternatives |
| Claude is stuck | Rephrase, add context, break down task |
| Generation too long | `Ctrl+C` to cancel |
| Need to start fresh | `/clear` or restart session |
| Security concern | Stop. Report to security team. |
| Accidentally shared secret | Report immediately. Rotate credential. |

---

## Getting Help

| Need | Where |
|------|-------|
| How-to questions | FAQ.md → Team channel |
| Policy questions | USAGE_POLICY.md |
| Security issues | Security team (immediate) |
| Bug reports | Team channel |

---

## Daily Habits

| Do | Don't |
|----|-------|
| `/code-review` before commits | Blindly accept generated code |
| Capture learnings with `/learn` | Share secrets or PII |
| Search patterns before new work | Commit code you don't understand |
| Review, test, then commit | Skip the review step |

---

## File Locations

```
.claude/
├── CLAUDE.md          # Project rules (Claude reads this)
├── commands/          # Slash command definitions
├── patterns/          # Team-approved solutions
├── learnings/         # Captured discoveries
└── failures/          # What NOT to do
```

---

## Emergency Contacts

| Situation | Contact |
|-----------|---------|
| Security incident | [SECURITY_CONTACT] |
| Policy question | [POLICY_CONTACT] |
| Technical help | [TEAM_CHANNEL] |

---

*Questions? Start with `/help` or ask in your team channel.*
