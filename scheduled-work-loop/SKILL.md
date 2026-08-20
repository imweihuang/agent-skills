---
name: scheduled-work-loop
description: Create or update recurring Codex tasks, monitors, reminders, or thread follow-ups. Use when the user explicitly asks for scheduled or repeated work.
---

# Scheduled Work Loop

Choose the scheduler object from where durable state lives:

| Kind | Use when |
| --- | --- |
| `cron` | A fresh run can reconstruct state from files, repos, web, inboxes, databases, or another durable source. |
| `heartbeat` | The next check must continue this task's unresolved conversation state. |

Prefer durable external state plus `cron` for ongoing monitors. Do not create a cron substitute for a thread-dependent follow-up.

## Create Or Update

1. Search for and use `automation_update`; never emit raw scheduler directives.
2. Inspect existing automations when this may be an update and avoid duplicates.
3. Infer the action, timing, report threshold, and stop condition from the request. Ask only for missing information that changes cost, risk, or behavior.
4. Use concrete local dates and times in the user's timezone.
5. Create or update only after material fields are known. Use the tool's suggested or review mode when required.
6. Claim success only after the tool confirms it.

## Prompt Contract

Keep each prompt short and self-contained. Include:

- action and durable sources
- exact repo, path, query, or URL when known
- timezone and recurrence
- what delta is worth reporting
- stop condition
- when user input is required

Avoid relative references such as “today,” “tomorrow,” or “above,” except when a heartbeat intentionally continues this task.

For unattended work, explicitly fail closed on secrets, production or deployments, live data or migrations, money or trading, destructive cleanup or Git, merges or shared-branch pushes, dependencies or lockfiles or CI, external messages, and shared infrastructure.

“Wrap the day” or “end the day” is not scheduling authorization. Require explicit scheduling language.

Report the resulting kind, local-time schedule, work performed, reporting threshold, stop condition, and approval gates.
