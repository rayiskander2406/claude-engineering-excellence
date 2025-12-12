# Command Reference

---

## Essential Commands (Always Available)

These are installed by default and cover 90% of daily needs.

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/code-review` | Reviews staged changes | **Before every commit** |
| `/explain [file]` | Explains code clearly | When confused by code |
| `/help` | Shows available commands | When stuck |

---

## Power Commands (Install When Needed)

These are in the `advanced-commands/` directory. Copy to `.claude/commands/` when needed.

### Development

| Command | What It Does |
|---------|--------------|
| `/test-gen [file]` | Generates tests for code |
| `/refactor [file]` | Suggests refactoring improvements |
| `/debug` | Helps debug issues systematically |

### Security & Quality

| Command | What It Does |
|---------|--------------|
| `/security-audit [path]` | Deep security analysis |
| `/perf-audit [file]` | Performance analysis |
| `/tech-debt` | Identifies technical debt |

### Documentation

| Command | What It Does |
|---------|--------------|
| `/doc-gen [file]` | Generates documentation |
| `/adr [title]` | Creates Architecture Decision Record |
| `/changelog` | Generates changelog from commits |

### Git Workflow

| Command | What It Does |
|---------|--------------|
| `/pr-prep` | Prepares PR description |
| `/commit` | Drafts commit message |

### Team Knowledge (Passive Flywheel)

| Command | What It Does |
|---------|--------------|
| `/capture` | Saves insight from current session |
| `/patterns` | Shows team patterns |
| `/review-sessions` | Reviews recent session logs |

---

## Installing Advanced Commands

```bash
# Option 1: Copy individual command
cp advanced-commands/test-gen.md .claude/commands/

# Option 2: Copy all advanced commands
cp advanced-commands/*.md .claude/commands/
```

---

## Creating Custom Commands

Create a file in `.claude/commands/your-command.md`:

```markdown
---
description: What this command does
---

Your prompt here.

Use $ARGUMENTS for user input.
```

Then use it: `claude "/your-command some input"`
