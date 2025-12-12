# Claude Code Monthly Satisfaction Survey

> 2-minute survey to track team satisfaction and gather feedback

---

## Survey Questions

### Question 1: Overall Satisfaction
**How satisfied are you with Claude Code this month?**

Scale: 1-10 (1 = Very Dissatisfied, 10 = Very Satisfied)

```
[ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5  [ ] 6  [ ] 7  [ ] 8  [ ] 9  [ ] 10
```

---

### Question 2: Time Savings
**How many hours per week does Claude Code save you?**

- [ ] 0 hours (no time savings)
- [ ] 1-2 hours
- [ ] 2-4 hours
- [ ] 4-6 hours
- [ ] 6+ hours

---

### Question 3: Most Valuable Feature
**What's the MOST valuable thing Claude Code helps you with?**

- [ ] Code generation / writing new code
- [ ] Bug fixing and debugging
- [ ] Code review assistance
- [ ] Learning from patterns / documentation
- [ ] Test writing
- [ ] Refactoring
- [ ] Other: _______________

---

### Question 4: Biggest Frustration
**What's your biggest frustration with Claude Code?** (Optional)

```
[Open text field]
```

---

### Question 5: Net Promoter Score (NPS)
**How likely are you to recommend Claude Code to a colleague?**

Scale: 0-10 (0 = Not at all likely, 10 = Extremely likely)

```
[ ] 0  [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5  [ ] 6  [ ] 7  [ ] 8  [ ] 9  [ ] 10
```

---

### Question 6: Knowledge Flywheel
**Did you use any of these features this month?** (Select all that apply)

- [ ] `/learn` - Captured a learning
- [ ] `/search-knowledge` - Searched existing knowledge
- [ ] Referenced a pattern from `.claude/patterns/`
- [ ] `/promote` - Promoted a learning to pattern
- [ ] None of the above

---

### Question 7: Improvement Suggestions
**What ONE thing would make Claude Code more useful for you?** (Optional)

```
[Open text field]
```

---

## Implementation Notes

### Google Forms Setup

1. Create new Google Form
2. Add questions above with appropriate types:
   - Q1, Q5: Linear scale
   - Q2, Q3: Multiple choice
   - Q4, Q7: Short answer (optional)
   - Q6: Checkboxes
3. Set form to collect email addresses (for tracking)
4. Schedule monthly reminder via Google Calendar

### Survey Distribution

**When:** First Monday of each month
**Who:** All developers with Claude Code access
**Reminder:** Mid-month if <70% response rate

### Response Analysis

Calculate:
- **Average Satisfaction**: Mean of Q1
- **NPS Score**: (% Promoters - % Detractors) × 100
  - Promoters: 9-10
  - Passives: 7-8
  - Detractors: 0-6
- **Time Savings**: Distribution and median
- **Feature Usage**: % using each feature
- **Flywheel Engagement**: % using knowledge features

### Tracking Template

```markdown
| Month | Responses | Avg Satisfaction | NPS | Avg Hours Saved | Flywheel Usage |
|-------|-----------|------------------|-----|-----------------|----------------|
| Oct   | 41/50     | 7.4              | 58  | 2-4 hrs         | 45%            |
| Nov   | 44/50     | 7.8              | 65  | 2-4 hrs         | 52%            |
| Dec   | 46/50     | 8.2              | 72  | 4-6 hrs         | 61%            |
```

---

## Automated Survey Link

For easy distribution, use this template email:

```
Subject: [2 min] Claude Code Monthly Check-in

Hi team,

Quick monthly survey on Claude Code - helps us improve the tools you use every day.

🔗 [Survey Link]

Takes 2 minutes. Your feedback directly shapes our tooling decisions.

Thanks!
[Your Name]
```

---

## Analyzing Results

### Monthly Report Template

```markdown
## Survey Results - [Month Year]

**Response Rate:** X/50 (X%)

### Satisfaction
- Average: X.X/10 (↑/↓ X.X from last month)
- NPS: XX (↑/↓ XX from last month)

### Time Savings
- Median: X-X hours/week
- XX% report 4+ hours saved

### Top Features
1. [Feature] - XX%
2. [Feature] - XX%
3. [Feature] - XX%

### Flywheel Engagement
- XX% used at least one knowledge feature
- XX% captured new learnings

### Top Frustrations
1. [Issue] - mentioned X times
2. [Issue] - mentioned X times

### Action Items
- [ ] Address [frustration 1]
- [ ] Promote [underused feature]
- [ ] Schedule training for [topic]
```

---

*Survey designed for minimal friction, maximum signal.*
