---
name: supervised-dev-dispatch
description: Coordinate an explicitly requested multi-lane or continuous development campaign with isolated workers, a lead-owned ledger, review-debt control, and human approval gates.
---

# Supervised Dev Dispatch

Use only after the user explicitly requests parallel, continuous, multi-lane, or supervised dispatch. The current user-facing task is the lead unless the user explicitly requests a separate dispatcher.

## Campaign Invariants

- The lead owns scope, user communication, queue decisions, integration, verification, and ledger writes.
- Workers receive one bounded task in an isolated branch or worktree and never edit the primary checkout.
- Do not use nested dispatch unless the user explicitly authorizes it.
- Keep at most three useful active lanes by default and prefer disjoint work.
- Pause new implementers when more than one completed code branch awaits lead review; read-only lanes may continue.
- External-model peer review is manual-only and requires the user's current explicit request.
- Global `AGENTS.md` controls model routing, effort, Git delivery, hard stops, and review tier. Do not duplicate or override it here.
- A run decision cannot create standing authorization. The active command-center registry's `DECISIONS.md` is the sole source for standing exceptions.

## Durable Ledger

Before dispatch, create `.delegate/supervised-runs/YYYY-MM-DD-slug/` and use [the ledger templates](references/ledger-templates.md).

Required files:

- `RUN.md`
- `TASK_QUEUE.md`
- `ACTIVE_WORKERS.md`
- `BRIEFS/Txxx.md`
- `OUTCOMES.md`

Add `QUESTIONS.md` and `DECISIONS.md` when user decisions exist, `PR_REVIEW.md` for code branches or PRs, `CLEANUP.md` for run-owned cleanup, and `LESSON_CANDIDATES.md` for reusable lessons.

The lead writes the ledger. Workers return evidence through their task or thread unless a brief grants a narrow report path. When connected to command center, resolve `.delegate/command-center/CURRENT` before relying on authority and update `HANDOFF.md` plus its track ledger together whenever the global contract requires it.

## Before Launch

- Inspect repo instructions, branch, status, HEAD, worktrees, and relevant PRs.
- Record the primary checkout and target base SHA.
- Verify the absolute ledger root and exact brief path.
- Create or verify the isolated worktree and branch.
- Record the worker execution mode and identifier.

Every worker brief includes:

- absolute cwd, branch, and base SHA
- primary checkout as forbidden
- allowed and forbidden paths and actions
- one scoped goal
- required verification and one primary verifier
- applicable skills and return format
- an anti-cheating clause: do not weaken tests, narrow the done-when, hide failures, or substitute mocks or stubs to manufacture a pass

The worker verifies cwd, branch, and clean starting state before writing.

## Operate

Use these states: `candidate`, `queued`, `planning`, `running`, `blocked-question`, `ready-review`, `needs-fix`, `pr-open`, `completed`, `completed-noop`, `merged`, `cleaned`, and `abandoned`.

A returned worker stops counting as active only after the lead updates task, worker, outcome, and review state. Do that before launching a replacement. Keep discovering useful work from the user's focus, repo truth, tests, issues or PRs, and worker findings.

Relay every hard stop to the user immediately; one blocked lane does not stop unrelated safe lanes. Never infer authority for merges or shared-branch pushes, deployments or production changes, live mutation, protected dependency or lockfile or CI changes, secrets, money, destructive Git, or destructive cleanup.

Stop when no safe useful candidate remains, the user stops the run, the environment prevents progress, or every remaining lane is approval-blocked.

## Accept And Close

The lead independently reads each final diff and reruns the strongest relevant verification. Follow global draft, ready, and internal-review rules. External review runs only when the user explicitly requests it.

Clean only run-owned artifacts after containment is proven. Finish with every lane completed, open, queued, blocked, or abandoned, and record the operator-facing result in `OUTCOMES.md`.
