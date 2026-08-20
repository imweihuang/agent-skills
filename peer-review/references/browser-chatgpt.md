# Browser ChatGPT Review

Use only when the user explicitly requests ChatGPT through the browser.

1. Curate context with `python3 "${CODEX_HOME:-$HOME/.codex}/skills/peer-review/scripts/build_review_context.py" --list <selected paths>`; never include secrets, `.env*`, credentials, private keys, databases, runtime logs, caches, or uninspected untracked files.
2. Use the Chrome control path and the user's logged-in session at `https://chatgpt.com/`; do not use the in-app browser.
3. Before filling or submitting the composer, verify that the account is logged in, the visible model selector is readable, and it matches the model or tier the user requested.
4. Never silently substitute a lower or different model. If the user requested only “ChatGPT Pro,” require a visible Pro or Extended Pro selector and report its exact displayed label.
5. If login, CAPTCHA, a missing selector, a model mismatch, or another user action blocks the run, do not submit. Report one of: `unavailable_browser`, `login_required`, `captcha_required`, `model_not_selected`, or `manual_action_required`.
6. After submission, a visible Stop-answering, Stop-generating, or Stop-streaming control means generation is incomplete. Poll in short calls rather than one long browser call. The default maximum wait is 45 minutes, overridable with `CHATGPT_PRO_BROWSER_TIMEOUT_SECONDS`.
7. On timeout, leave the tab available, report `manual_action_required`, and provide the conversation URL.
8. Report the exact observed selector, URL, completion status, and participant label. Treat findings as advisory and validate material claims locally before acting.
