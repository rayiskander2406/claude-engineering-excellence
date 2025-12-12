# Frequently Asked Questions

> *Quick answers to common Claude Code questions*

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Daily Usage](#daily-usage)
3. [MCP Servers](#mcp-servers)
4. [Security & Privacy](#security--privacy)
5. [Troubleshooting](#troubleshooting)
6. [Best Practices](#best-practices)
7. [Team Collaboration](#team-collaboration)

---

## Getting Started

### How do I install Claude Code?

```bash
# macOS/Linux
npm install -g @anthropic-ai/claude-code

# Or with Homebrew
brew install claude-code

# Verify installation
claude --version
```

### How do I start Claude Code?

```bash
# Navigate to your project
cd your-project

# Start Claude Code
claude
```

### What's the first thing I should do after installing?

1. Install the essential MCP stack:
```bash
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
claude mcp add github -- npx -y @modelcontextprotocol/server-github
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

2. Read `ONBOARDING.md` for the complete setup guide.

### Do I need an API key?

Yes, you need an Anthropic API key. Set it up:
```bash
# Claude Code will prompt you on first run, or:
export ANTHROPIC_API_KEY=your-key-here
```

Contact your team lead if you don't have access to an API key.

---

## Daily Usage

### What are slash commands?

Slash commands are shortcuts that trigger predefined prompts. Type `/` in Claude Code to see available commands.

**Most useful commands:**
| Command | Purpose |
|---------|---------|
| `/code-review` | Review code for issues |
| `/explain` | Understand unfamiliar code |
| `/debug` | Systematic debugging |
| `/commit` | Generate commit message |
| `/pr-prep` | Prepare pull request |

### How do I review code before committing?

```
/code-review
```

This runs a multi-dimensional review covering security, performance, and maintainability.

### How do I get Claude to explain code I don't understand?

```
/explain path/to/file.js
```

Or just ask: "Explain what this function does and why it's structured this way."

### Can Claude write tests for me?

Yes! Use:
```
/test-gen path/to/file.js
```

Or ask: "Write unit tests for the UserService class covering happy path and error cases."

### How do I generate a commit message?

```
/commit
```

This analyzes your staged changes and generates a conventional commit message.

### Can Claude create pull requests?

Yes, if you have the GitHub MCP server installed:
```
/pr-prep
```

Or ask: "Create a PR for my current branch with a summary of changes."

---

## MCP Servers

### What are MCP servers?

MCP (Model Context Protocol) servers give Claude access to external tools and data. They transform Claude from a code generator into a productivity powerhouse.

### Which MCP servers should I install?

**Essential (everyone):**
```bash
# Memory - persistent knowledge
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'

# GitHub - PRs, issues, CI/CD
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Context7 - real-time documentation
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

See `MCP_STACK.md` for the complete guide.

### How do I check which MCP servers are installed?

```bash
claude mcp list
```

### How do I remove an MCP server?

```bash
claude mcp remove <server-name>
```

### Does MCP data count against my context window?

**No!** MCP data is stored externally and only loaded when queried. This is one of its key advantages.

### The GitHub MCP server isn't working. What do I do?

1. Check that `GITHUB_TOKEN` is set:
```bash
echo $GITHUB_TOKEN
```

2. Ensure the token has the required scopes (repo, read:org)

3. Try removing and re-adding:
```bash
claude mcp remove github
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Security & Privacy

### What should I NEVER paste into Claude?

| Never Share | Examples |
|-------------|----------|
| Credentials | API keys, passwords, tokens |
| Customer data | Names, emails, addresses |
| Production data | Real user records |
| Financial data | Credit cards, bank accounts |

See `USAGE_POLICY.md` for complete guidelines.

### Is my code sent to Anthropic's servers?

Yes, your prompts are sent to Anthropic's API for processing. Review `USAGE_POLICY.md` for data handling guidelines.

### Can I use Claude with proprietary code?

Yes, you can use Claude with your company's source code. This is the primary use case.

**Do NOT use Claude with:**
- Competitor's proprietary code
- Code you don't have rights to

### What if I accidentally paste a secret?

1. Don't panic
2. Rotate the secret immediately
3. Report to your security team
4. Document what happened

See `USAGE_POLICY.md` Section 9 for full incident response.

### How do I sanitize logs before sharing?

```bash
# Before (BAD):
DATABASE_URL=postgres://admin:password123@prod.db.com/users

# After (GOOD):
DATABASE_URL=postgres://[USER]:[PASSWORD]@[HOST]/[DATABASE]
```

Replace all credentials, emails, and personal data with placeholders.

---

## Troubleshooting

### Claude Code won't start

1. Check your API key:
```bash
echo $ANTHROPIC_API_KEY
```

2. Verify installation:
```bash
claude --version
```

3. Try reinstalling:
```bash
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code
```

### Claude is giving outdated code examples

Install Context7 for real-time documentation:
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

Then ask: "Using the latest React Query v5 docs, show me how to use useQuery."

### Claude forgets what we discussed yesterday

Install the Memory MCP server:
```bash
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
```

Then use `/learn` to capture important discoveries.

### Slash commands aren't working

1. Check that command files exist:
```bash
ls .claude/commands/
# or
ls ~/.claude/commands/
```

2. Verify the command has the correct frontmatter:
```markdown
---
description: Your command description
---
```

### Claude is too slow

1. Check your internet connection
2. Try a simpler prompt
3. Break large tasks into smaller ones
4. Use `/compact` if context is getting large

### Context window is full

```
/clear
```

This starts a fresh conversation. Your MCP memory persists.

For less aggressive cleanup:
```
/compact
```

This summarizes the conversation to free up space.

### MCP server keeps crashing

```bash
# Check logs
claude mcp logs <server-name>

# Remove and re-add
claude mcp remove <server-name>
claude mcp add <server-name> -- <command>
```

---

## Best Practices

### How do I get better results from Claude?

1. **Be specific**: "Add input validation to the login form" > "Make the form better"
2. **Provide context**: Share relevant code, error messages, requirements
3. **Use slash commands**: They're optimized for common tasks
4. **Review everything**: Never commit without reviewing

### Should I let Claude write entire features?

For complex features:
1. Ask Claude to plan first: "How would you approach implementing X?"
2. Review the plan
3. Implement incrementally
4. Review each piece

### How do I learn from Claude?

- Use `/explain` to understand unfamiliar code
- Ask "why" questions: "Why did you choose this approach?"
- Request alternatives: "What are other ways to solve this?"
- Capture learnings: `/learn`

### When should I NOT use Claude?

| Situation | Why |
|-----------|-----|
| You don't understand the problem | Understand first, then use Claude |
| Security-critical code (alone) | Get security team review |
| You can't review the output | Never commit unreviewed code |
| Highly regulated code | May need compliance review |

### How do I capture team learnings?

```
/learn
```

Describe what you discovered. It gets added to the knowledge graph.

When a learning is proven (3+ successful uses):
```
/promote
```

This elevates it to a team pattern.

---

## Team Collaboration

### How do we share knowledge across the team?

The Self-Learning Flywheel:

1. **Learnings** are stored in `.claude/learnings/` (git-tracked)
2. **Patterns** are stored in `.claude/patterns/` (git-tracked)
3. **Everyone** can search with `/search-knowledge`

See `SELF_LEARNING_FLYWHEEL.md` for the complete guide.

### How do new team members get up to speed?

1. Follow `ONBOARDING.md`
2. Run `/search-knowledge project overview`
3. Review `.claude/patterns/` for team conventions
4. Pair with an experienced team member

### Can multiple people use Claude on the same codebase?

Yes! Each person has their own Claude Code session. Knowledge sharing happens through:
- Git-tracked `.claude/` directories
- Each person's MCP Memory server indexes shared knowledge

### How do I share a useful prompt with the team?

Create a slash command:

1. Create `.claude/commands/your-command.md`:
```markdown
---
description: What this command does
---

Your prompt template here.

$ARGUMENTS
```

2. Commit and push
3. Team members get it on `git pull`

### Who reviews Claude-generated code?

**You do, first.** Then normal code review process.

Claude-generated code follows the same review process as human-written code:
1. Author reviews (you)
2. Automated checks (CI)
3. Peer review
4. Merge

---

## Still Have Questions?

- **Check the docs**: Start with `README.md` and linked files
- **Search knowledge**: `/search-knowledge your question`
- **Ask in Slack**: [YOUR CHANNEL]
- **Ask Claude**: "How do I..." often works

---

*"The only dumb question is the one you didn't ask and then broke production."*
