# Ledger Templates

Use only the files the run needs. Keep them concise, secret-free, and lead-owned.

## RUN.md

```markdown
# Supervised Run: <slug>

Date: <YYYY-MM-DD>
Repo: <absolute path>
Lead task: <id or link>
Lead mode: <single | split when explicitly requested>
Ledger root: <absolute path>
Ledger root guard: verified; writes must not land in the primary checkout
Active command-center registry: <resolved path or none>
Standing authorization source: active registry DECISIONS.md only
Central decision refs: <IDs or none>
Primary checkout: <absolute path; forbidden to workers>
Primary branch and start SHA: <branch> @ <sha>
Target branch and base SHA: <branch> @ <sha>
Worker limit: <default 3>
Review-debt limit: <default 1 completed code branch>
Stop condition: <condition>
```

## TASK_QUEUE.md

```markdown
# Task Queue

| ID | Priority | Status | Lane | Branch | Scope | Risk | Source | Blocked By | Hold Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T001 | P1 | queued | implementer | codex/<branch> | <scope> | <risk> | <source> | none | none |
```

## ACTIVE_WORKERS.md

```markdown
# Active Workers

| Task | Worker or Thread | Execution Mode | Worktree | Branch | Base SHA | State | Last Check | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T001 | <id> | <mode> | <absolute path> | <branch> | <sha> | running | <time> | <next> |

Review debt: <count>
```

## BRIEFS/T001.md

```markdown
# Worker Brief T001

Worker or thread: <id after launch>
Execution mode: <mode>
Assigned cwd: <absolute worktree path>
Branch: <branch>
Base SHA: <sha>
Primary checkout forbidden path: <absolute path>
Report path: <task/thread or narrow file>

## Goal
- <one bounded outcome>

## Allowed Paths
- <paths>

## Forbidden Paths And Actions
- Do not edit the primary checkout.
- Do not spawn workers or broaden scope.
- Do not cross any global approval gate.

## Verification
- Primary verifier: <strongest check closest to the outcome>
- Supporting checks: <tests or inspection>

## Skills
- Required: <skills or none>
- Optional triggers: <skill and condition or none>
- Forbidden: nested dispatch and any unapproved external reviewer

## Integrity
- Do not weaken or skip tests, narrow the done-when, hide failures, or substitute mocks or stubs to manufacture a pass. Surface blockers and report exact verification evidence.

## Return
- completed yes or no
- branch or PR
- files changed
- commands and key results
- blockers and remaining risk
```

## OUTCOMES.md

```markdown
# Outcomes

Net result: <one sentence>
Current gate: <none | question | CI | review | merge | deploy>

| Task | Why It Mattered | Result | Evidence | Remaining Gate |
| --- | --- | --- | --- | --- |
| T001 | <value> | <status> | <tests, SHA, or PR> | <gate> |

## Timeline
- <time>: <outcome or material state change>

## Next Actions
1. <next>
```

## QUESTIONS.md And DECISIONS.md

```markdown
# Questions

| ID | Task | Ask | Options | Blocking Scope | Status |
| --- | --- | --- | --- | --- | --- |
| Q001 | T001 | <one-reply ask> | <options> | <lane or run> | open |
```

```markdown
# Decisions

Run decisions are run-scoped. Standing authorization comes from the active command-center registry's DECISIONS.md only.

| ID | Time | Decision | Scope | Source | Central Decision Ref |
| --- | --- | --- | --- | --- | --- |
| D001 | <time> | <decision> | <scope> | <user message> | <ID or none> |
```

## PR_REVIEW.md

```markdown
# PR Review

| Task | PR | Final Candidate SHA | Base Fresh | Diff Inspected | Primary Verification | Internal Review | External Review | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T001 | <url> | <sha> | yes | yes | <evidence> | <result> | <only if explicitly requested> | <status> |

Merge requires the applicable internal review, final-candidate diff inspection, verification evidence, authorization, and containment proof. External peer review is recorded only when the user explicitly requested it.
```

## CLEANUP.md And LESSON_CANDIDATES.md

```markdown
# Cleanup

| Artifact | Run Owned | Containment Evidence | Action | Result |
| --- | --- | --- | --- | --- |
| <worktree or branch> | yes | <target contains final SHA; no unique intended changes> | <kept or removed> | <result> |

Remote branch deletion or history rewrite requires explicit approval. Preserve unrelated or uncontained work.
```

```markdown
# Lesson Candidates

| Lesson | Evidence | Durable Destination | Status |
| --- | --- | --- | --- |
| <lesson> | <evidence> | <repo ledger or none> | candidate |
```
