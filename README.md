# Claude Code for Teams

> One habit. Zero friction. Continuous improvement.

---

## For Individuals (30 seconds)

```bash
npm install -g @anthropic-ai/claude-code && claude auth
```

Then in any project: `claude "What does this codebase do?"`

**The ONE habit**: `claude "/code-review"` before every commit.

---

## For Teams (60 seconds)

```bash
curl -sSL https://raw.githubusercontent.com/edutone/claude-engineering-excellence/main/STARTER_KIT/setup.sh | bash
```

The setup will:
- Check prerequisites (Node, git, Claude Code)
- Ask your stack (Java, React, .NET, Vue, Python)
- Ask about compliance needs (EdTech/FERPA)
- Install only what you need
- Give you your first magic moment

---

## What You Get

```
.claude/
├── CLAUDE.md              # Project rules
├── commands/
│   ├── code-review.md     # THE essential command
│   ├── explain.md         # Understand any code
│   ├── help.md            # Quick reference
│   ├── capture.md         # Save insights (flywheel)
│   └── review-sessions.md # Weekly review (flywheel)
├── patterns/              # Your stack's patterns
└── sessions/
    └── captures.md        # Your team's knowledge

.hooks/
└── pre-commit             # Blocks secrets automatically
```

---

## The Five Commands

| Command | When |
|---------|------|
| `/code-review` | **Before every commit** |
| `/explain [file]` | When confused by code |
| `/help` | Show available commands |
| `/capture` | Save something that worked |
| `/review-sessions` | Weekly 5-min review |

---

## The Passive Flywheel

```
Work → Something works → /capture (30 sec) → captures.md
                                                   ↓
                              Weekly: /review-sessions (5 min)
                                                   ↓
                                          Team patterns emerge
```

No rituals. No process. Just capture when useful, review weekly.

---

## Documentation

| Doc | Purpose |
|-----|---------|
| **[QUICKSTART.md](./QUICKSTART.md)** | Everything essential (1 page) |
| **[CHEAT_SHEET.md](./CHEAT_SHEET.md)** | Print this |
| `reference/` | Deep docs when you need them |
| `advanced-commands/` | 29 power commands (opt-in) |

---

## CI/CD & Automation

```bash
# Non-interactive mode
curl -sSL ... | bash -s -- --stack=react --edtech
```

---

## Philosophy

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   One habit beats twenty best practices.        │
│                                                 │
│   /code-review before every commit.             │
│   Everything else is optional.                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

*Built for teams who ship.*
