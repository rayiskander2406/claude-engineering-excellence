---
description: Plan and execute migrations safely
---

# Migration Planning

Plan a safe, incremental migration with rollback strategies.

## Migration Types

### Code Migrations
- Framework upgrades
- Language version updates
- Library replacements
- API changes

### Database Migrations
- Schema changes
- Data transformations
- Database engine changes
- Sharding/partitioning

### Infrastructure Migrations
- Cloud provider changes
- Service restructuring
- Containerization
- Serverless transitions

## Migration Principles

### 1. Strangler Fig Pattern
- Build new alongside old
- Gradually redirect traffic
- Remove old after validation

### 2. Expand-Contract
- Add new (expand)
- Migrate consumers
- Remove old (contract)

### 3. Feature Flags
- Deploy dark
- Enable incrementally
- Quick rollback capability

### 4. Backward Compatibility
- New code reads old format
- Write both formats during transition
- Clean up after migration complete

## Migration Plan Template

```markdown
# Migration Plan: [Title]

## Overview
**From**: [Current state]
**To**: [Target state]
**Reason**: [Why migrate]

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | | | |

## Prerequisites
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

## Phases

### Phase 1: Preparation
- [ ] [Task]
- [ ] [Task]
**Rollback**: [How to undo]

### Phase 2: Parallel Operation
- [ ] [Task]
- [ ] [Task]
**Rollback**: [How to undo]

### Phase 3: Cutover
- [ ] [Task]
- [ ] [Task]
**Rollback**: [How to undo]

### Phase 4: Cleanup
- [ ] [Task]
- [ ] [Task]

## Validation
- [ ] [Check 1]
- [ ] [Check 2]

## Rollback Plan
[Detailed rollback steps for each phase]

## Communication Plan
- [ ] Stakeholder notification
- [ ] User communication
- [ ] Documentation updates
```

## Output Format

Generate a migration plan with:
1. Current state analysis
2. Target state definition
3. Gap analysis
4. Phased migration steps
5. Risk assessment
6. Rollback procedures
7. Validation checklist
8. Timeline (without dates)

## Target

$ARGUMENTS

Describe what needs to be migrated:
- From what to what
- Why the migration is needed
- Any constraints or requirements
