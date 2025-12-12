# Team Setup Guide

> For team leads setting up Claude Code for their team

---

## Quick Team Rollout (1 Week)

### Day 1-2: Pilot (3-5 developers)

```bash
# Each pilot user runs:
curl -sSL https://raw.githubusercontent.com/edutone/claude-engineering-excellence/main/STARTER_KIT/setup.sh | bash
```

Have them:
1. Try the magic moment: `claude "What does this codebase do?"`
2. Use `/code-review` before their next commit
3. Note any friction or questions

### Day 3-4: Gather Feedback

Ask pilots:
- What worked well?
- What was confusing?
- Would you recommend it to teammates?

### Day 5: Full Rollout

Share with entire team:
```
Team,

We're adopting Claude Code. Here's everything you need:

1. Run: curl -sSL [URL] | bash
2. Read: QUICKSTART.md (5 min)
3. Build ONE habit: /code-review before every commit

That's it. Questions → [TEAM_CHANNEL]
```

---

## Team Configuration

### Essential: Memory Server

For knowledge to persist across sessions:

```bash
claude mcp add-json "memory" '{"command":"npx","args":["-y","@modelcontextprotocol/server-memory"]}'
```

### Optional: GitHub Integration

For PR workflows:

```bash
export GITHUB_TOKEN=your_token
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Measuring Success

### What to Track (Keep It Simple)

| Question | How to Measure |
|----------|----------------|
| Are people using it? | Ask in standup: "Who used Claude Code this week?" |
| Is it helping? | Monthly: "On a scale 1-5, how helpful is Claude Code?" |
| Any incidents? | Track: Security issues, compliance violations (should be 0) |

### What NOT to Track

- Individual usage metrics
- "Productivity" scores
- Leaderboards of any kind

---

## Common Questions from Teams

**"Do I have to use it?"**
No, but try `/code-review` on your next commit. Most people find it catches things.

**"What if Claude is wrong?"**
You review everything before committing. You own what you commit.

**"Is my code being sent somewhere?"**
Claude Code sends prompts to Anthropic's API. Don't include secrets or customer data.

**"What about compliance?"**
If you selected EdTech mode during setup, FERPA/COPPA rules are built into your CLAUDE.md.

---

## Advanced Setup (When You're Ready)

| Want | Reference |
|------|-----------|
| More commands | [Advanced Commands](./COMMANDS.md) |
| Full policies | [Usage Policy](./USAGE_POLICY.md) |
| Metrics dashboard | [Metrics Guide](./METRICS.md) |
| External training | [Resources](./RESOURCES.md) |

---

## Support

- **Documentation**: This repo
- **Issues**: [GitHub Issues](https://github.com/edutone/claude-engineering-excellence/issues)
- **Team questions**: [TEAM_CHANNEL]
