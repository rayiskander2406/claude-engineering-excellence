# Super Prompts Collection

> Battle-tested prompt templates that produce exceptional results with Claude Code

---

## Why This Matters

Research shows that well-structured prompts can improve output quality by **39%** (Anthropic internal testing). The prompts in this collection have been curated from:

- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library/library) (Official)
- [awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts) (3.3k+ stars)
- Coursera prompt engineering courses
- Real-world production usage patterns

---

## Quick Reference: Prompt Engineering Principles

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   1. BE SPECIFIC      - Vague prompts = vague results                   │
│   2. GIVE CONTEXT     - Claude can't read your mind                     │
│   3. USE STRUCTURE    - XML tags improve parsing by 39%                 │
│   4. SHOW EXAMPLES    - One good example beats paragraphs of rules      │
│   5. ITERATE          - First response is a starting point              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Table of Contents

1. [Universal Patterns](#universal-patterns)
2. [Developer Prompts](#developer-prompts)
3. [DevOps / SRE Prompts](#devops--sre-prompts)
4. [QA / SDET Prompts](#qa--sdet-prompts)
5. [Tech Lead / Architect Prompts](#tech-lead--architect-prompts)
6. [Prompt Chaining Patterns](#prompt-chaining-patterns)

---

## Universal Patterns

### The XML Structure Pattern

**Why it works:** Claude parses XML tags with high precision. Structure your complex prompts with clear sections.

```xml
<context>
I'm working on [project type] using [tech stack].
The codebase follows [patterns/conventions].
</context>

<task>
[Clear description of what you need]
</task>

<constraints>
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]
</constraints>

<output_format>
[How you want the response structured]
</output_format>
```

### The Chain-of-Thought Pattern

**Why it works:** Asking Claude to reason step-by-step produces more accurate results for complex problems.

```
Before providing your solution, please:
1. Analyze the problem and identify key challenges
2. Consider 2-3 possible approaches
3. Evaluate trade-offs of each approach
4. Recommend the best approach with justification
5. Then implement the solution
```

### The Expert Role Pattern

**Why it works:** Setting context for Claude's expertise level improves relevance and depth.

```
You are a senior [role] with 15+ years of experience in [domain].
You're known for writing [quality: clean/performant/secure] code
that follows [standard: SOLID/clean architecture/etc.] principles.

Review this code with that expertise:
[code]
```

### The Iterative Refinement Pattern

**Why it works:** Multi-turn conversations produce better results than single prompts.

```
Turn 1: "Explain what this code does at a high level"
Turn 2: "Now explain the [specific part] in more detail"
Turn 3: "What are the potential issues with this approach?"
Turn 4: "Generate an improved version addressing those issues"
```

---

## Developer Prompts

### Code Explanation (Multi-Level)

```
Explain this code at three levels:

1. **Executive Summary** (1-2 sentences for non-technical stakeholders)
2. **Technical Overview** (for developers unfamiliar with this codebase)
3. **Deep Dive** (implementation details, edge cases, gotchas)

Code:
[paste code]
```

### Debugging: The Rubber Duck++

```
I'm debugging an issue where [symptom].

<context>
- This happens when [conditions]
- I've tried [what you've attempted]
- The error message is: [error]
- Relevant code is in [file/function]
</context>

<investigation_request>
1. What are the most likely root causes? (ranked by probability)
2. What diagnostic steps should I take to isolate the cause?
3. For each potential cause, what would the fix look like?
</investigation_request>
```

### Code Review: Security-Focused

```
Review this code with a security-first mindset:

<code>
[paste code]
</code>

<review_checklist>
- [ ] Injection vulnerabilities (SQL, XSS, command)
- [ ] Authentication/authorization gaps
- [ ] Sensitive data exposure
- [ ] Input validation issues
- [ ] Error handling that leaks information
- [ ] Insecure dependencies
- [ ] OWASP Top 10 violations
</review_checklist>

For each issue found:
1. Severity (Critical/High/Medium/Low)
2. Line number and description
3. Specific fix with code example
```

### Code Review: Performance-Focused

```
Analyze this code for performance issues:

<code>
[paste code]
</code>

<analysis_areas>
- Time complexity (Big O)
- Space complexity
- Database query efficiency (N+1, missing indexes)
- Memory leaks or excessive allocation
- Unnecessary computation or redundant operations
- Caching opportunities
- Async/parallel execution opportunities
</analysis_areas>

For each issue:
1. Current performance impact
2. Recommended optimization
3. Expected improvement
4. Trade-offs of the optimization
```

### Refactoring: Extract Pattern

```
This code works but has grown complex. Help me refactor it:

<code>
[paste code]
</code>

<goals>
- Improve readability
- Enable easier testing
- Maintain identical external behavior
- Follow [SOLID/Clean Code/team convention]
</goals>

<constraints>
- Don't change the public API
- Minimize the number of files changed
- Each step should be a safe, atomic refactoring
</constraints>

Provide:
1. Analysis of current issues
2. Step-by-step refactoring plan
3. Refactored code
4. Tests to verify behavior is preserved
```

### Feature Implementation: Greenfield

```
I need to implement [feature description].

<requirements>
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
</requirements>

<existing_patterns>
Our codebase uses:
- [Framework/pattern for this type of feature]
- [Relevant existing code in path/to/similar/feature]
- [Team conventions from .claude/patterns/]
</existing_patterns>

<deliverables>
1. High-level design (before coding)
2. Implementation following our patterns
3. Unit tests with edge cases
4. Integration points with existing code
</deliverables>
```

### Bug Fix: Systematic

```
Bug report: [title]

<reproduction>
1. [Step 1]
2. [Step 2]
3. [Expected vs actual behavior]
</reproduction>

<investigation>
I've traced the issue to [file/function].
The relevant code path is:
[paste code or describe flow]
</investigation>

<request>
1. Confirm my understanding of the root cause
2. Propose a fix that doesn't introduce regressions
3. Suggest tests to prevent this bug from recurring
4. Identify if similar bugs might exist elsewhere
</request>
```

### API Design

```
I need to design an API for [functionality].

<context>
- Consumers: [who will use this API]
- Scale: [expected load/volume]
- Existing APIs: [link to similar APIs in codebase]
</context>

<requirements>
- [Functional requirement 1]
- [Functional requirement 2]
- [Non-functional: latency, availability, etc.]
</requirements>

Design the API including:
1. Endpoint structure (REST/GraphQL/gRPC)
2. Request/response schemas
3. Error handling strategy
4. Authentication/authorization approach
5. Versioning strategy
6. Rate limiting considerations
```

### Test Generation: Comprehensive

```
Generate comprehensive tests for this code:

<code>
[paste code]
</code>

<test_requirements>
- Framework: [Jest/pytest/xUnit/etc.]
- Coverage target: [80%/90%/etc.]
- Include: unit tests, edge cases, error scenarios
- Mock strategy: [what to mock]
</test_requirements>

<edge_cases_to_consider>
- Empty/null inputs
- Boundary values
- Concurrent access (if applicable)
- Error conditions
- [Domain-specific edge cases]
</edge_cases_to_consider>

For each test:
- Clear test name describing scenario
- Arrange/Act/Assert structure
- Comments explaining non-obvious assertions
```

---

## DevOps / SRE Prompts

### Incident Response: RCA Template

```
We had an incident. Help me write the RCA:

<incident>
- Service: [affected service]
- Duration: [start to resolution]
- Impact: [users affected, revenue impact]
- Severity: [P1/P2/P3]
</incident>

<timeline>
[Paste timeline of events]
</timeline>

<resolution>
[What fixed it]
</resolution>

Generate an RCA document with:
1. Executive Summary (2-3 sentences)
2. Timeline (formatted table)
3. Root Cause Analysis (5 Whys)
4. Contributing Factors
5. Action Items (with owners and deadlines)
6. Lessons Learned
7. Metrics to track improvement
```

### Infrastructure as Code Review

```
Review this IaC for production readiness:

<code>
[paste Terraform/CloudFormation/Pulumi]
</code>

<review_areas>
- Security (IAM, network, encryption)
- Cost optimization
- High availability / disaster recovery
- Scalability
- Monitoring and alerting
- Compliance ([SOC 2/HIPAA/GDPR/etc.])
- Tagging and organization
</review_areas>

For each finding:
1. Risk level
2. Current state
3. Recommended change with code
```

### Runbook Generation

```
Create a runbook for [operation/scenario]:

<context>
- Service: [service name]
- Environment: [prod/staging/etc.]
- On-call team: [team name]
</context>

<scenario>
[Describe the scenario this runbook addresses]
</scenario>

Generate a runbook with:
1. Overview and scope
2. Prerequisites and access required
3. Step-by-step procedure (with exact commands)
4. Verification steps after each action
5. Rollback procedure
6. Escalation path
7. Post-operation checklist
```

### Alert Tuning

```
Help me tune this alert:

<current_alert>
Name: [alert name]
Condition: [current threshold/condition]
Current behavior: [fires X times per week, Y% are actionable]
</current_alert>

<goal>
Reduce noise while catching real issues.
Target: [X actionable alerts per week]
</goal>

Suggest:
1. Refined threshold/condition
2. Additional context to include in alert
3. Runbook link content
4. Suggested grouping/deduplication
5. Escalation rules
```

### Dockerfile Optimization

```
Optimize this Dockerfile for production:

<dockerfile>
[paste Dockerfile]
</dockerfile>

<goals>
- Minimize image size
- Reduce build time
- Improve security
- Enable better caching
- Follow best practices
</goals>

<constraints>
- Base image preference: [alpine/debian/distroless/etc.]
- Must run as non-root
- Multi-stage build if beneficial
</constraints>

Provide:
1. Analysis of current issues
2. Optimized Dockerfile
3. Explanation of each improvement
4. Expected size/build time improvement
```

### CI/CD Pipeline Design

```
Design a CI/CD pipeline for [project type]:

<context>
- Language: [language/framework]
- Deployment target: [K8s/Lambda/ECS/etc.]
- Current process: [describe or "greenfield"]
</context>

<requirements>
- [ ] Automated testing (unit, integration, e2e)
- [ ] Security scanning (SAST, dependency scan)
- [ ] Build and push artifacts
- [ ] Environment promotion (dev → staging → prod)
- [ ] Rollback capability
- [ ] Notifications
</requirements>

<platform>
[GitHub Actions/GitLab CI/Jenkins/etc.]
</platform>

Provide:
1. Pipeline architecture diagram (ASCII)
2. Stage-by-stage breakdown
3. YAML configuration
4. Secrets management approach
5. Monitoring and observability
```

---

## QA / SDET Prompts

### Test Strategy Design

```
Design a test strategy for [feature/project]:

<feature>
[Description of what's being tested]
</feature>

<scope>
- Components involved: [list]
- Integrations: [external systems]
- User types: [personas]
</scope>

<constraints>
- Timeline: [release date]
- Resources: [team size, environments]
- Risk tolerance: [high/medium/low for different areas]
</constraints>

Generate:
1. Test pyramid breakdown (unit/integration/e2e percentages)
2. Critical path test cases
3. Risk-based prioritization
4. Environment requirements
5. Data requirements
6. Automation candidates
7. Manual testing needs
8. Performance testing approach
```

### Test Case Generation: BDD

```
Generate BDD test cases for this user story:

<user_story>
As a [role]
I want to [action]
So that [benefit]
</user_story>

<acceptance_criteria>
- [AC 1]
- [AC 2]
- [AC 3]
</acceptance_criteria>

Generate Gherkin scenarios covering:
1. Happy path
2. Alternative flows
3. Error conditions
4. Edge cases
5. Security scenarios (if applicable)

Format:
```gherkin
Feature: [feature name]

  Scenario: [scenario name]
    Given [context]
    When [action]
    Then [expected outcome]
```
```

### Bug Report Enhancement

```
Improve this bug report for clarity and actionability:

<original_report>
[paste bug report]
</original_report>

<template>
Enhance to include:
1. Clear, searchable title
2. Environment details
3. Precise reproduction steps (numbered)
4. Expected vs actual behavior
5. Severity/priority recommendation
6. Screenshots/logs (placeholder)
7. Possible root cause (if known)
8. Related issues (if any)
</template>
```

### Exploratory Testing Charter

```
Create an exploratory testing charter for [feature]:

<feature>
[Description]
</feature>

<focus_areas>
- [Area 1]
- [Area 2]
</focus_areas>

Generate a charter with:
1. Mission statement
2. Time box recommendation
3. Risk areas to explore
4. User personas to emulate
5. Data variations to try
6. Environment configurations
7. Heuristics to apply (SFDPOT, etc.)
8. Note-taking template
```

### API Test Suite Generation

```
Generate an API test suite for this endpoint:

<api_spec>
[OpenAPI/Swagger spec or description]
</api_spec>

<test_framework>
[Postman/REST Assured/pytest/etc.]
</test_framework>

Generate tests for:
1. Happy path (valid request → expected response)
2. Input validation (missing fields, invalid types, boundary values)
3. Authentication/authorization scenarios
4. Error responses (4xx, 5xx)
5. Performance baseline
6. Contract validation (schema adherence)

Include:
- Test data setup
- Assertions for status, headers, body
- Cleanup/teardown
```

### Regression Test Selection

```
Help me select regression tests for this change:

<change_description>
[What changed and why]
</change_description>

<files_modified>
[List of changed files]
</files_modified>

<test_suite>
[Description of existing test suite or link]
</test_suite>

Recommend:
1. Must-run tests (directly affected)
2. Should-run tests (potentially affected)
3. Smoke test subset for quick validation
4. Tests that can be skipped (with justification)
5. New tests needed (if any)
```

---

## Tech Lead / Architect Prompts

### Architecture Decision Record (ADR)

```
Help me write an ADR for [decision]:

<context>
- Problem: [what we're solving]
- Current state: [how it works today]
- Constraints: [technical, business, timeline]
</context>

<options_considered>
1. [Option A]
2. [Option B]
3. [Option C]
</options_considered>

<decision>
[Which option and why]
</decision>

Generate an ADR with:
1. Title (ADR-XXX: Decision Title)
2. Status (Proposed/Accepted/Deprecated)
3. Context (expanded)
4. Decision (with rationale)
5. Consequences (positive and negative)
6. Alternatives considered (with trade-offs)
7. References
```

### Technical Design Document

```
Create a technical design document for [feature/system]:

<overview>
[High-level description]
</overview>

<requirements>
Functional:
- [FR1]
- [FR2]

Non-functional:
- [NFR1: latency, availability, etc.]
- [NFR2]
</requirements>

<constraints>
- [Technical constraints]
- [Business constraints]
- [Timeline]
</constraints>

Generate:
1. Executive Summary
2. Goals and Non-Goals
3. System Architecture (with ASCII diagram)
4. API Design
5. Data Model
6. Security Considerations
7. Scalability Analysis
8. Monitoring and Alerting
9. Rollout Plan
10. Open Questions
```

### Code Architecture Review

```
Review this codebase architecture:

<codebase>
[Link or description of structure]
Key directories:
- [dir1]: [purpose]
- [dir2]: [purpose]
</codebase>

<concerns>
[Specific areas of concern or "general health check"]
</concerns>

Analyze:
1. Overall architecture pattern (monolith, microservices, modular monolith)
2. Separation of concerns
3. Dependency management
4. Testability
5. Scalability readiness
6. Technical debt indicators
7. Recommendations with priority

For each recommendation:
- Current state
- Target state
- Migration path
- Effort estimate (S/M/L)
```

### Migration Planning

```
Plan a migration from [current] to [target]:

<current_state>
- Technology: [current tech]
- Scale: [data volume, traffic]
- Dependencies: [what depends on this]
</current_state>

<target_state>
- Technology: [target tech]
- Requirements: [why migrating]
</target_state>

<constraints>
- Zero/minimal downtime required
- Timeline: [deadline]
- Resources: [team capacity]
</constraints>

Generate:
1. Migration strategy (big bang, strangler fig, parallel run)
2. Phase breakdown
3. Risk assessment
4. Rollback plan for each phase
5. Success metrics
6. Communication plan
7. Testing strategy
```

### Tech Debt Prioritization

```
Help me prioritize this tech debt:

<debt_items>
1. [Item 1: description, estimated effort]
2. [Item 2: description, estimated effort]
3. [Item 3: description, estimated effort]
[...]
</debt_items>

<context>
- Team capacity: [available time]
- Upcoming features: [what's on the roadmap]
- Pain points: [what's causing the most friction]
</context>

For each item, evaluate:
1. Impact (team productivity, reliability, security)
2. Urgency (getting worse? blocking features?)
3. Effort (S/M/L/XL)
4. Dependencies (must do X before Y?)

Provide:
1. Prioritized list with rationale
2. Quick wins (high impact, low effort)
3. Strategic investments (high impact, high effort)
4. Recommended quarterly plan
```

### Estimation (No Time, Just Complexity)

```
Help me estimate this work:

<work_item>
[Description of feature/project]
</work_item>

<context>
- Codebase familiarity: [high/medium/low]
- Similar past work: [reference if any]
- Team size: [number of developers]
</context>

Provide:
1. Complexity breakdown (what makes this hard)
2. Component list with relative sizing (S/M/L/XL)
3. Dependencies and sequencing
4. Risk factors that could increase scope
5. Unknowns requiring investigation
6. Confidence level in estimate

Do NOT provide time estimates - only relative complexity.
```

---

## Prompt Chaining Patterns

### Pattern 1: Understand → Plan → Execute

```
Chain for complex implementations:

Prompt 1 (Understand):
"Analyze this codebase and explain how [feature area] currently works.
Focus on: data flow, key abstractions, existing patterns."

Prompt 2 (Plan):
"Given your understanding, design an approach to [new requirement].
Provide 2-3 options with trade-offs."

Prompt 3 (Execute):
"Implement Option [N] following the patterns you identified.
Include tests."
```

### Pattern 2: Generate → Critique → Refine

```
Chain for high-quality output:

Prompt 1 (Generate):
"Write [code/document/design] for [requirement]."

Prompt 2 (Critique):
"Now review what you just created as if you were a senior [role].
Be critical. What could be improved?"

Prompt 3 (Refine):
"Address the issues you identified and provide an improved version."
```

### Pattern 3: Breadth → Depth

```
Chain for exploration:

Prompt 1 (Breadth):
"What are all the possible approaches to [problem]?
List at least 5 with one-sentence descriptions."

Prompt 2 (Evaluate):
"Evaluate each approach against these criteria: [criteria].
Rank them."

Prompt 3 (Depth):
"Deep dive on the top-ranked approach.
Provide full implementation."
```

### Pattern 4: Red Team → Blue Team

```
Chain for security:

Prompt 1 (Red Team):
"You're an attacker. How would you exploit this code?
Find all vulnerabilities."

Prompt 2 (Blue Team):
"You're a defender. For each vulnerability identified,
provide a fix and detection method."

Prompt 3 (Verify):
"Review the fixes. Are there any bypasses or edge cases
still exploitable?"
```

---

## Anti-Patterns to Avoid

| Don't Do This | Do This Instead |
|---------------|-----------------|
| "Fix this code" | "Fix the null pointer exception on line 23 when user.name is undefined" |
| "Make it better" | "Refactor to improve readability, specifically extracting the validation logic" |
| "Write tests" | "Write unit tests for the calculateDiscount function covering: normal case, zero cart, expired coupon" |
| "Is this secure?" | "Review this code for SQL injection and XSS vulnerabilities specifically" |
| Single huge prompt | Chain of focused prompts |
| Accepting first response | Iterating with follow-ups |

---

## Quick Prompt Templates

### One-Liner Quick Tasks

```
# Explain
"Explain [file:function] focusing on [aspect]"

# Fix
"Fix [error] in [file:line] - the issue is [symptom]"

# Test
"Add test for [function] covering [scenario]"

# Refactor
"Refactor [function] to [goal] while keeping behavior identical"

# Document
"Add JSDoc/docstring to [function] explaining parameters and return value"
```

---

## Measuring Prompt Effectiveness

Track these when using prompts:

| Metric | Good | Needs Improvement |
|--------|------|-------------------|
| Iterations needed | 1-2 | 4+ |
| Code accepted as-is | >70% | <50% |
| Review time for output | <5 min | >15 min |
| Bugs introduced | 0 | Any |

---

## Contributing

Found a prompt that works exceptionally well? Share it!

1. Test it multiple times
2. Document when/why to use it
3. Add it to this collection
4. Share with the team

---

## Resources

- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library/library)
- [awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Learn Prompting](https://learnprompting.org/)

---

*"A good prompt is worth a thousand iterations."*

