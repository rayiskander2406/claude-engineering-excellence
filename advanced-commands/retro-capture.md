---
description: Harvest learnings after completing significant work
---

# Retrospective Capture

After completing any significant task (PR, feature, bug fix), harvest knowledge before moving on.

## The Questions

Answer each question honestly:

### 1. What Worked Well?

- Any approaches worth reusing?
- Any tools or techniques that helped?
- Any patterns to promote?

### 2. What Was Harder Than Expected?

- Any unexpected complexity?
- Any gotchas to document?
- Any failures worth recording?

### 3. What Would You Do Differently?

- Any process improvements?
- Any better approaches you'd use next time?
- Any tools you wished you had?

### 4. What Questions Remain?

- Any unresolved mysteries?
- Any areas needing more research?
- Any technical debt created?

## Capture Process

For each valuable insight from your answers:

### If it's a SUCCESS worth sharing:

```javascript
// Create learning
mcp__memory__create_entities([{
  name: "Learning: [TITLE]",
  entityType: "learning",
  observations: ["[TYPE]: [INSIGHT]", "Source: [TASK/PR]"]
}])
```

Also add to `.claude/learnings/YYYY-MM-DD.md`

### If it's a FAILURE to prevent:

```javascript
// Create failure entity
mcp__memory__create_entities([{
  name: "Failure: [TITLE]",
  entityType: "failure",
  observations: ["What happened: [DESCRIPTION]", "How to avoid: [PREVENTION]"]
}])
```

Also add to `.claude/failures/what-not-to-do.md`:

```markdown
## [DATE] - [TITLE]

**What Happened**: [Description]
**Why It Failed**: [Root cause]
**How to Avoid**: [Prevention steps]
**Related**: [Links to code/PR]
```

### If it's a PATTERN emerging:

Flag for `/promote` if you've seen this work 3+ times:

```markdown
## Pattern Candidate: [NAME]

**Observation Count**: [N]
**Last Seen**: [DATE]
**Ready for Promotion**: [YES/NO]
```

### If it's a QUESTION to investigate:

Add to `.claude/learnings/questions.md`:

```markdown
## [DATE] - [QUESTION]

**Context**: [Why this matters]
**Suspected Answer**: [Hypothesis if any]
**Status**: OPEN / INVESTIGATING / RESOLVED
```

## Mandatory After

Run `/retro-capture` after:
- [ ] Merging a PR
- [ ] Completing a feature
- [ ] Fixing a significant bug
- [ ] Completing a spike/investigation
- [ ] Any work taking 4+ hours

## Output Format

Generate a summary:

```markdown
# Retro Capture: [TASK NAME]
**Date**: [YYYY-MM-DD]
**Duration**: [X hours]

## Learnings Captured
1. [Learning 1 title] - [Type]
2. [Learning 2 title] - [Type]

## Failures Documented
1. [Failure 1 if any]

## Pattern Candidates
1. [Pattern if emerging]

## Open Questions
1. [Question if any]

## Knowledge Graph Updates
- [N] entities created
- [N] relations added
```

## Target

$ARGUMENTS

What task did you just complete?
- Brief description of the work
- Any notable challenges or successes
- Anything that surprised you
