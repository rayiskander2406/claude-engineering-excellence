# Developer Workshop: Mastering Claude Code

> 45-minute hands-on workshop for software developers

---

## Workshop Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 45 minutes |
| **Format** | Presentation + Live coding + Exercises |
| **Audience** | Software developers (all levels) |
| **Prerequisites** | Claude Code installed, access to a codebase |
| **Materials** | This deck, sample codebase, exercise files |

### Learning Objectives

By the end of this workshop, participants will be able to:

1. Use Claude Code effectively for daily development tasks
2. Apply the review-before-commit workflow consistently
3. Leverage slash commands for productivity
4. Contribute to the team knowledge flywheel
5. Avoid common pitfalls and anti-patterns

---

## Agenda

| Time | Section | Type |
|------|---------|------|
| 0:00 | Welcome & Mindset | Presentation |
| 0:05 | The Core Workflow | Presentation |
| 0:10 | Live Demo: Real Task | Demo |
| 0:20 | Exercise 1: Debug Together | Hands-on |
| 0:30 | Power Features | Presentation + Demo |
| 0:38 | Exercise 2: Code Review | Hands-on |
| 0:43 | Wrap-up & Resources | Discussion |

---

# SECTION 1: Welcome & Mindset
*5 minutes*

---

## Slide 1: What Claude Code Is (and Isn't)

### It IS:
- A powerful coding assistant
- A force multiplier for your skills
- A tool that learns your codebase

### It ISN'T:
- A replacement for your judgment
- An excuse to skip code review
- A security oracle
- Magic

**Speaker Notes:**
> Start by grounding expectations. Many developers either over-trust or under-trust AI tools. We want to find the productive middle ground. Claude Code amplifies your abilities—it doesn't replace them.

---

## Slide 2: The Mindset Shift

```
OLD: "Claude, write this feature for me"
     ↓
     Accept → Commit → Hope it works

NEW: "Claude, let's solve this together"
     ↓
     Collaborate → Review → Understand → Commit
```

**Speaker Notes:**
> The key insight is that Claude Code works best as a collaboration, not delegation. You're still the engineer. Claude is a very capable junior developer who works incredibly fast but needs your oversight.

---

## Slide 3: Your Responsibility

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   "I reviewed it. I understand it. I own it."               │
│                                                             │
│   This is your professional commitment for every line       │
│   of code you commit, regardless of who generated it.       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Speaker Notes:**
> This is non-negotiable. When code goes into production and causes a bug, the answer "Claude wrote it" is not acceptable. You reviewed it, you committed it, you own it. This isn't scary—it's empowering. You're in control.

---

# SECTION 2: The Core Workflow
*5 minutes*

---

## Slide 4: The Review-Before-Commit Workflow

```
        ┌─────────────┐
        │   PROMPT    │
        │  (You ask)  │
        └──────┬──────┘
               ↓
        ┌─────────────┐
        │  GENERATE   │
        │ (Claude     │
        │  creates)   │
        └──────┬──────┘
               ↓
   ┌───────────────────────┐
   │       REVIEW          │  ← YOU ARE HERE
   │                       │
   │  • Read every line    │
   │  • Understand logic   │
   │  • Check edge cases   │
   │  • Verify security    │
   │  • Test locally       │
   │                       │
   └───────────┬───────────┘
               ↓
        ┌─────────────┐
        │   COMMIT    │
        │  (You own)  │
        └─────────────┘
```

**Speaker Notes:**
> Walk through each step. Emphasize that the REVIEW step is where you add value. Claude is fast at generating; you're essential at judging quality, security, and fit.

---

## Slide 5: What "Review" Actually Means

### Minimum Review Checklist

```
[ ] I read every line of generated code
[ ] I understand what it does and why
[ ] I tested it locally
[ ] I checked for hardcoded values
[ ] I looked for security issues
[ ] It follows our team conventions
[ ] I would defend this code in a code review
```

**Speaker Notes:**
> Go through each item. "Read every line" means literally every line. "Understand" means you could explain it to a colleague. "Defend in code review" is the gut check—if you'd be embarrassed explaining this code, don't commit it.

---

## Slide 6: Safe Data Handling

| SAFE to Share | NEVER Share |
|---------------|-------------|
| Your source code | API keys, passwords, tokens |
| Error messages (sanitized) | Customer PII (names, emails) |
| Stack traces (sanitized) | Production data |
| Architecture questions | `.env` file contents |
| Open source code | Competitor code |

### Sanitization Example

```bash
# BAD
Error: User john.doe@company.com failed auth with token sk-abc123

# GOOD
Error: User [EMAIL] failed auth with token [REDACTED]
```

**Speaker Notes:**
> This is critical for compliance. We're in EdTech—FERPA and COPPA apply. Pause and ask: "Has anyone accidentally shared something sensitive with an AI tool before?" (Normalize the concern, then show the solution.)

---

# SECTION 3: Live Demo
*10 minutes*

---

## Slide 7: Live Demo - A Real Task

**Scenario:** We need to add input validation to an API endpoint

### Demo Steps:

1. Start Claude Code in our project
2. Explain the task naturally
3. Review Claude's suggestion critically
4. Ask for modifications
5. Test the result
6. Use `/code-review` before committing

**Speaker Notes:**
> This is the heart of the workshop. Do this live with a real codebase. Narrate your thinking:
> - "I'm going to describe what I need..."
> - "Hmm, this looks right, but let me check the edge cases..."
> - "Actually, I want to handle this differently. Let me tell Claude..."
> - "Now I'll review what we have..."
> Show that it's a conversation, not a one-shot prompt.

---

## Slide 8: Demo - The Conversation

```
YOU: I need to add validation to the createStudent endpoint in
     src/controllers/student.ts. We need to validate firstName,
     lastName, email, and gradeLevel. Use our existing validation
     patterns.

CLAUDE: [generates validation code]

YOU: This looks good, but we also need to sanitize the inputs
     to prevent XSS. Can you add that?

CLAUDE: [adds sanitization]

YOU: Let me review this more carefully...
     - Line 15: Why are we allowing grade -1?

CLAUDE: Grade -1 represents Pre-K in our system...

YOU: Got it, that makes sense. Let me run the tests.
```

**Speaker Notes:**
> Show that you're driving the conversation. Push back on Claude when needed. Ask clarifying questions. This demonstrates the collaborative mindset.

---

## Slide 9: Demo - Using /code-review

```bash
$ git add src/controllers/student.ts
$ claude
> /code-review

Claude: Reviewing staged changes...

## Summary
Added input validation to createStudent endpoint

## Potential Issues
1. Line 23: Email regex may reject valid emails with + character
2. Line 31: Consider rate limiting for validation errors

## Security
✓ XSS sanitization present
✓ No SQL injection vectors
⚠ Consider adding request size limits

## Suggestions
- Add unit tests for validation edge cases
- Document validation rules in API spec
```

**Speaker Notes:**
> Show how `/code-review` catches things you might miss. Emphasize this should happen BEFORE every commit. It takes 10 seconds and catches real issues.

---

# SECTION 4: Exercise 1 - Debug Together
*10 minutes*

---

## Slide 10: Exercise 1 - Debugging

### Scenario

You've been assigned this bug:

```
BUG-1234: Student grade calculation returns NaN for some students
```

The error appears in `src/services/gradeCalculator.ts`

### Your Task (10 minutes)

1. Open the exercise file
2. Ask Claude to help understand the bug
3. Work with Claude to identify the root cause
4. Propose a fix (don't just accept Claude's first suggestion!)
5. Be ready to explain your fix to the group

**Speaker Notes:**
> Distribute the exercise file or have it in a shared repo. Walk around and observe. Look for:
> - Are they reviewing Claude's suggestions?
> - Are they asking follow-up questions?
> - Are they testing their fixes?
> After 8 minutes, bring everyone back and ask 1-2 people to share their approach.

---

## Slide 11: Exercise 1 - Debrief

### Questions for Discussion

1. What was your first prompt to Claude?
2. Did Claude's first suggestion fully solve the problem?
3. What follow-up questions did you ask?
4. How did you verify the fix was correct?

### Key Takeaways

- Debugging with Claude is a conversation
- First suggestions are starting points, not final answers
- Your domain knowledge matters (you knew the context Claude didn't)

**Speaker Notes:**
> Facilitate a brief discussion. Highlight good practices you observed. If someone blindly accepted Claude's fix, use it as a teachable moment (kindly).

---

# SECTION 5: Power Features
*8 minutes*

---

## Slide 12: Essential Slash Commands

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/code-review` | Reviews staged changes | **Every commit** |
| `/pr-prep` | Generates PR description | Creating PRs |
| `/security-audit` | Security analysis | Auth code, APIs |
| `/test-gen` | Generates tests | Adding coverage |
| `/explain` | Explains code | Understanding unfamiliar code |
| `/learn` | Captures discovery | When you learn something |
| `/search-knowledge` | Searches team knowledge | Before starting work |

**Speaker Notes:**
> These are your daily tools. Emphasize `/code-review` as non-negotiable. Show that `/search-knowledge` prevents reinventing wheels.

---

## Slide 13: The Knowledge Flywheel

```
              ┌─────────────┐
         ┌────│    WORK     │←───┐
         │    │ (you code)  │    │
         │    └─────────────┘    │
         ↓                       │
   ┌───────────┐          ┌───────────┐
   │  CAPTURE  │          │   REUSE   │
   │  (/learn) │          │(patterns) │
   └─────┬─────┘          └─────┬─────┘
         │                      ↑
         ↓                      │
   ┌───────────┐          ┌───────────┐
   │  ENCODE   │─────────→│ COMPOUND  │
   │(/promote) │          │ (growth)  │
   └───────────┘          └───────────┘
```

**Speaker Notes:**
> This is how the team gets smarter over time. When you discover something useful, capture it with `/learn`. After it's validated 3+ times, promote it to a pattern. Then everyone benefits. Show `.claude/learnings/` and `.claude/patterns/` directories.

---

## Slide 14: Team Knowledge in Action

### Before Starting New Work:

```
> /search-knowledge authentication

Found 3 relevant learnings:
1. "JWT refresh token handling" - 2024-01-15
2. "SSO integration gotchas" - 2024-01-20
3. "Session timeout best practices" - 2024-02-01

Found 1 pattern:
- patterns/auth-middleware.md
```

### You just saved 2 hours of rediscovery

**Speaker Notes:**
> This is the payoff. Show a real example from your team's knowledge base if available. Emphasize that contributing to this helps everyone—including future you.

---

## Slide 15: Prompt Engineering Tips

### Be Specific

```
❌ "Fix this bug"
✓ "The calculateGrade function in gradeCalculator.ts returns NaN
    when a student has zero assignments. Help me understand why
    and suggest a fix that handles this edge case."
```

### Give Context

```
❌ "Add validation"
✓ "Add validation to the createStudent endpoint. We need to
    validate: firstName (required, max 100 chars), lastName
    (required, max 100 chars), email (valid format), gradeLevel
    (-1 to 12 where -1 is Pre-K). Follow our existing patterns
    in .claude/patterns/validation.md"
```

### Iterate

```
"This is close, but we also need to handle [case]. Can you modify?"
"I don't understand line 15. Can you explain the logic there?"
"Let's try a different approach using [technique] instead."
```

**Speaker Notes:**
> Good prompts get good results. Show the contrast between vague and specific prompts. Emphasize that iteration is normal—Claude rarely gets it perfect the first time.

---

# SECTION 6: Exercise 2 - Code Review
*5 minutes*

---

## Slide 16: Exercise 2 - Review This Code

### Scenario

A junior developer asks you to review their Claude-generated code:

```typescript
async function deleteStudent(studentId: string) {
  // Delete student from database
  await db.query(`DELETE FROM students WHERE id = '${studentId}'`);

  // Log the deletion
  console.log(`Deleted student: ${studentId}`);

  return { success: true };
}
```

### Your Task (5 minutes)

1. Review this code as if Claude generated it
2. Identify ALL issues (security, logging, error handling, etc.)
3. Write feedback as if responding to a PR

**Speaker Notes:**
> This tests their review skills. Issues include:
> 1. SQL injection (string concatenation)
> 2. No parameterized query
> 3. No authorization check
> 4. Logging might expose PII
> 5. No error handling
> 6. No soft delete (compliance issue)
>
> Ask participants to share findings. Use this to reinforce that Claude can generate insecure code, and review is essential.

---

## Slide 17: Exercise 2 - Debrief

### Issues in That Code

| Issue | Category | Why It Matters |
|-------|----------|----------------|
| SQL injection | Security | Attackers can delete arbitrary data |
| No auth check | Security | Anyone could delete any student |
| Console.log with ID | Compliance | PII in logs violates FERPA |
| No error handling | Reliability | Failures silently succeed |
| Hard delete | Compliance | May need audit trail |

### Key Takeaway

Claude generated this. A human committed it. **You are the last line of defense.**

**Speaker Notes:**
> Drive home that review is non-optional. This exact code pattern has caused real data breaches. Your review skills are what make Claude Code safe to use.

---

# SECTION 7: Wrap-up
*2 minutes*

---

## Slide 18: Key Takeaways

### 1. Mindset
Claude is a collaborator, not a replacement for your judgment.

### 2. Workflow
Prompt → Generate → **Review** → Commit. Never skip review.

### 3. Safety
Know what's safe to share. When in doubt, don't.

### 4. Productivity
Use slash commands daily. `/code-review` before every commit.

### 5. Team Knowledge
Capture learnings. Search before starting. Help the flywheel spin.

**Speaker Notes:**
> Quick recap. Ask if there are questions. Point to resources for continued learning.

---

## Slide 19: Resources & Next Steps

### Immediate
- [ ] Complete the Onboarding Checklist (Day 3-5 if started)
- [ ] Print the Cheat Sheet and keep it visible
- [ ] Use `/code-review` on your next commit

### This Week
- [ ] Capture at least one learning with `/learn`
- [ ] Search team knowledge before starting your next task

### Ongoing
- [ ] Join [TEAM_CHANNEL] for questions
- [ ] Check RESOURCES.md for external learning
- [ ] Attend office hours (if scheduled)

---

## Slide 20: Questions?

### Contact

- **Workshop questions:** [FACILITATOR]
- **Technical help:** [TEAM_CHANNEL]
- **Policy questions:** [POLICY_CONTACT]
- **Security concerns:** [SECURITY_CONTACT]

### Feedback

Help us improve this workshop: [FEEDBACK_LINK]

---

# Appendix

---

## Appendix A: Common Mistakes

| Mistake | Why It Happens | How to Avoid |
|---------|----------------|--------------|
| Committing without review | Time pressure | Make review a habit, not optional |
| Trusting security suggestions | Claude sounds confident | Always get human security review |
| Sharing PII | Copying from logs | Sanitize before pasting |
| Over-prompting | Trying to get perfect output | Iterate in conversation |
| Under-prompting | Being too vague | Give context and constraints |

---

## Appendix B: Exercise Solutions

### Exercise 1: Grade Calculator Bug

**Root Cause:** Division by zero when student has no assignments

**Fix:**
```typescript
function calculateGrade(assignments: Assignment[]): number {
  if (assignments.length === 0) {
    return 0; // or null, depending on business logic
  }
  const total = assignments.reduce((sum, a) => sum + a.score, 0);
  return total / assignments.length;
}
```

### Exercise 2: Delete Student Issues

**Secure Version:**
```typescript
async function deleteStudent(studentId: string, requestingUserId: string) {
  // Verify authorization
  const canDelete = await authService.canDeleteStudent(requestingUserId, studentId);
  if (!canDelete) {
    throw new ForbiddenError('Not authorized to delete this student');
  }

  // Soft delete with parameterized query
  await db.query(
    'UPDATE students SET deleted_at = NOW(), deleted_by = $1 WHERE id = $2',
    [requestingUserId, studentId]
  );

  // Audit log (no PII)
  auditService.log({
    action: 'STUDENT_DELETED',
    targetId: studentId,
    actorId: requestingUserId,
    timestamp: new Date()
  });

  return { success: true };
}
```

---

## Appendix C: Facilitator Notes

### Before the Workshop
- [ ] Test Claude Code installation on presentation machine
- [ ] Prepare sample codebase with exercise files
- [ ] Test all demos work
- [ ] Have backup slides in case of technical issues
- [ ] Print exercise handouts (optional)

### During the Workshop
- Watch for participants who seem stuck
- Encourage questions
- Use real examples from your codebase when possible
- Don't rush the exercises—learning happens there

### After the Workshop
- Send follow-up email with resources
- Collect feedback
- Update workshop based on feedback
- Schedule office hours for follow-up questions

---

*"The goal of this workshop is not to make you faster. It's to make you better."*
