# Multi-Agent GitHub Coordination and Rate-Safety Policy

**Effective date:** 2026-11-08  
**Repository:** `metsam-mastem/HAA-D-3`  
**Status:** Proposed operating policy; adopt across sibling repositories after owner review.

## Purpose

More than one ChatGPT account/model may work on the same GitHub account and repositories. This policy minimizes conflicting writes, duplicate work, excessive API traffic, and accidental rate-limit escalation. It cannot guarantee that GitHub will never impose a limit; GitHub's secondary limits are partly undisclosed and may change.

## 1. Coordination model

### Single-writer rule
- Assign one active writer/agent per repository for mutative operations during a work window.
- For a given path, only one agent may edit at a time. Read-only audits may be shared, but a writer must re-fetch the file/branch head immediately before mutation.
- Use distinct, descriptive agent branches. Never force-push, reset, or move a shared branch.
- Do not write directly to `main` while another agent's branch or PR is actively changing the same scope. Prefer a branch and PR for review.
- Reserve issue numbers or work packages before creating issues. Search existing open/closed issues to avoid duplicates.
- A change should be small, coherent, and have one owner. Do not batch unrelated documentation rewrites.

### Work reservation note
Before a work session, leave a brief coordination note (issue/PR comment or shared log) with:
- agent label/account (no secrets),
- repository, branch, paths and issue/work-package IDs,
- intent and expected finish,
- status (active / paused / done).
Release the reservation when complete. If no common communication channel exists, avoid overlapping files and work only on a uniquely named branch/path.

## 2. Conservative API pacing

GitHub documents primary authenticated REST limits (often 5,000 requests/hour per user credential) plus secondary limits, including concurrent requests, endpoint point budgets, and content-creation limits. These budgets may be shared across credentials/actions associated with the same user, and secondary limits are not fully disclosed.

For this project, use a conservative local policy:
- **Serial requests:** no fan-out of simultaneous GitHub calls. Queue requests and process one at a time.
- **Read sparsely:** prefer one repository inventory/tree request and fetch only files relevant to the task; do not repeatedly poll status or reread unchanged files.
- **Write pacing:** wait at least 1 second between content-generating/mutative calls; aim for no more than 10 mutations in a minute during shared work, and fewer when another agent is active. This is a local safety target, not a GitHub-guaranteed threshold.
- **Avoid polling:** check workflow/PR status once after a meaningful wait or use event-driven updates when available. Do not poll every few seconds.
- **Cache:** retain relevant response details (commit SHA, file blob SHA, branch, PR/run URL) in the work log and reuse them instead of refetching.
- **Conditional reads:** use ETag/If-None-Match or Last-Modified when the client supports it. If the connector does not expose conditional headers, minimize duplicate reads.
- **Respect server guidance:** obey `Retry-After`, `X-RateLimit-Reset`, and `X-RateLimit-Remaining` response headers if exposed.
- **On 403/429/secondary-limit response:** immediately stop writes and retries. Wait at least the server-specified interval; otherwise wait at least one minute. If failure persists, use exponential backoff (e.g. 1, 2, 4, 8 minutes) and stop rather than repeatedly probing. Never continue rapid retries.
- **Content generation:** do not create a burst of issues, comments, files, releases, or commits. Group a coherent deliverable into a small number of writes, with pacing.
- **No unauthorized workarounds:** do not rotate credentials, accounts, IPs, or tokens to evade a limit. Reduce traffic and respect the limit.

## 3. Branch and file safety

- Branch naming: `agent/<scope>-<date>` or `audit/<scope>-<date>`.
- Before a write: fetch target branch HEAD and current file SHA; verify expected base.
- Use optimistic concurrency via file SHA/expected SHA where supported.
- If SHA mismatch, stop and reconcile; do not blindly retry with the new SHA.
- Do not delete, overwrite, merge, or close another agent's work without explicit coordination.
- Do not merge a PR merely because CI passes; require review of the diff, acceptance criteria and overlapping work.
- Protect `main`; prefer PRs and branch protection.
- Ensure every generated artifact is attributable to a commit and documented source/configuration.

## 4. Security and secret handling

- Never put PATs, OAuth tokens, app secrets, private keys, cookies, or authorization headers in chat, issues, commits, logs, artifacts, or this policy.
- Use least-privilege credentials and the supported GitHub connector / GitHub Actions `GITHUB_TOKEN` as appropriate.
- Restrict Actions permissions (read-only by default; grant write only to the job that needs it).
- Do not create new credentials or change account security settings as part of an audit.
- If a secret is exposed, stop, notify the owner, revoke/rotate it, and remove it from history using the approved process.

## 5. Minimal operating checklist

- [ ] Identify whether another model/agent is currently editing the repository.
- [ ] Read latest branch/PR/work-package state with a sparse, serial request.
- [ ] Reserve a unique branch and paths.
- [ ] Check for duplicate issues and existing deliverables.
- [ ] Make only scoped, sequential changes.
- [ ] Run the relevant CI once; avoid repeated polling.
- [ ] Report exact branch, commit, PR, tests, remaining gaps and any blocked state.
- [ ] Release the reservation and update the continuity/handoff record.

## 6. Limits and non-guarantees

This policy reduces risk but cannot guarantee zero rate limiting or bans. GitHub's documented thresholds are subject to change and secondary limits may be triggered for reasons not fully published. The authoritative operational response is to stop when rate-limited, honor headers, and back off. See the linked official references in the repository's source list or GitHub documentation:
- REST API rate limits
- REST API best practices
- REST API troubleshooting
