---
name: engineering-verification
description: Use when verifying an engineering change or review to choose proportional validation, inspect the exact diff, run focused tests and relevant static checks, and report PASS, FAIL, NOT_RUN, or BLOCKED_EXTERNAL with fresh evidence. Do not impose a universal test command or claim completion from inspection alone.
---

# Engineering verification

Use this skill as the evidence gate between a change and a completion claim. Validation is proportional to the affected surface: a documentation-only change needs structural and link checks, while a security-sensitive runtime change may require focused tests, static analysis, and an authorized runtime check. The goal is a defensible result, not a ritual command.

## Operational contract

### Objective

Map every acceptance-relevant completion claim to fresh evidence that is strong enough for that claim and no stronger. Choose proportional checks from the repository's real tooling, inspect the exact final diff, and preserve the distinction between static, local runtime, remote, and production evidence.

### Expected inputs

The workflow expects the original request and acceptance criteria, baseline/worktree state, exact changed paths or diff, repository tooling and test commands, affected risk surface, relevant environment/identity boundaries, and any requested or mandatory checks.

### Required outputs

Return a claim-to-evidence matrix with the exact command or evidence source, evidence scope, one of `PASS`/`FAIL`/`NOT_RUN`/`BLOCKED_EXTERNAL`, concise result details, inspected files/diff scope, preserved unrelated changes, external blockers, residual risk, and the next action when the evidence is incomplete.

### Definition of done

Verification is complete only when every acceptance-relevant claim is covered by fresh evidence or an explicit limiting state, the final tested state matches the final diff, no required failure/blocker is hidden, and the overall completion statement stays within the scope actually proven.

## Non-negotiable invariant

> No completion claim without fresh evidence for the acceptance criteria and an inspected diff.

“Looks correct,” “the worker said it passed,” a previous run, or one successful command cannot substitute for the check that proves the specific claim. Static evidence, local runtime evidence, staging evidence, and production evidence are different scopes and must be reported as such.

## When to use

Use after:

- a code, configuration, migration, documentation, skill, dependency, or infrastructure-boundary change;
- a bounded worker reports that work is complete;
- a review needs explicit evidence and limitations rather than a general confidence statement;
- a failure or blocked environment requires an honest status and next action.

Do not run a full suite merely because this skill was invoked. First identify the changed surface, the project’s actual tooling, and the acceptance criteria.

## Status vocabulary

Every planned or acceptance-relevant check receives exactly one of these statuses:

- `PASS` — the check was executed, completed successfully, and its evidence supports the stated claim within the named scope.
- `FAIL` — the check was executed and found a failure, regression, unresolved finding, or unmet acceptance criterion.
- `NOT_RUN` — the check was relevant or requested but was not executed; state why.
- `BLOCKED_EXTERNAL` — the check could not be executed because an external dependency, remote environment, authenticated session, required service, or permission boundary was unavailable.

Do not use PASS for a check that was skipped, inferred, partially executed, or blocked. A report may contain several statuses; the overall result is PASS only when every acceptance-relevant check supports the claim and no required limitation is hidden.

## Proportional verification workflow

### 1. Translate the request into checkable claims

Write the acceptance criteria as observable claims. For each claim, identify:

- changed surface and risk;
- narrowest command, test, inspection, or runtime observation that can prove it;
- preconditions, expected output, and evidence to retain;
- whether the check is local/static, controlled runtime, staging, remote, or production.

Do not silently expand a bounded task into unrelated quality work. Do not shrink a security, data, or deployment claim to a cosmetic inspection.

### 2. Inspect baseline and exact diff

Before and after validation:

- inspect worktree status and the exact diff for the requested paths;
- confirm that no unrelated worker changes were reverted or overwritten;
- check file names, generated artifacts, formatting, added dependencies, and configuration boundaries;
- run a whitespace or syntax-aware diff check when the project provides one.

Diff inspection is part of verification, not a replacement for tests. A clean diff does not prove behavior.

### 3. Choose focused checks

Start with the narrowest relevant checks and expand only when risk or acceptance criteria justify it:

- documentation or skill text: frontmatter parsing, required headings/fields, Markdown structure, local-link resolution, and repository-specific content checks;
- TypeScript/JavaScript: focused tests, relevant linter/formatter checks, type checking for the affected project, and a build only when the changed boundary warrants it;
- Python, Flutter, SQL, or another ecosystem: use the project’s configured focused tests and static checks rather than assuming Node tooling;
- auth, tenant, data, or security changes: include negative authorization cases, boundary checks, dependency/config review, and an authorized runtime check when required;
- deployment or infrastructure configuration: validate syntax and the affected target boundary; do not deploy merely to obtain evidence.

Use the package manager and scripts actually declared by the repository. A missing or inappropriate command is a reason to choose another relevant check, not a reason to declare success.

### 4. Execute and read the complete result

Run each selected check freshly after the final edit. Record the exact command, working directory, exit code or test summary, and the scope it covers. Read the complete output relevant to the result, including warnings, skipped tests, and generated-file changes.

Do not claim that a test, build, route, browser flow, remote service, authenticated path, or deployment passed unless that exact check ran and its output supports the claim.

### 5. Classify scope and limitations

| Evidence scope | Can support | Cannot support by itself |
| --- | --- | --- |
| Static inspection or linter | Syntax, selected rules, obvious structural properties | Runtime correctness, authorization in production, external health |
| Focused test | The exercised behavior and fixtures | Untested paths, real provider behavior, all deployment environments |
| Local or controlled runtime | The observed flow in that environment | Production parity, real traffic, remote credentials, operational health |
| Staging or remote authenticated check | The named remote flow and identity/data scope | All tenants, all roles, future deployments, untested paths |
| Production check | Only the explicitly authorized and exercised production path | Broad system health or safety outside that path |

If an acceptance-relevant external check cannot run, classify it `BLOCKED_EXTERNAL`. If it was simply omitted, classify it `NOT_RUN`.

### 6. Re-inspect after checks

Tests and tools can generate or modify files. Re-check the exact diff, status, and relevant artifacts after validation. Confirm that the final state is the state that was tested. Preserve pre-existing changes and do not clean or reset unrelated work.

## Completion gate

Before saying done:

1. re-read the request and map every acceptance criterion to evidence;
2. inspect the final diff and file scope;
3. run selected focused tests and static checks freshly;
4. classify each as PASS, FAIL, NOT_RUN, or BLOCKED_EXTERNAL;
5. state untested scope, external limits, and residual risk;
6. if any required check is not PASS, report the limiting status and next action instead of claiming full completion.

## Evidence report template

| Claim or check | Command or evidence source | Scope | Status | Result and limits |
| --- | --- | --- | --- | --- |
| Acceptance criterion | Exact command or inspection | Local, static, staging, or production | PASS/FAIL/NOT_RUN/BLOCKED_EXTERNAL | Sanitized output and what remains unproved |

Then report:

- files inspected and exact files changed;
- existing unrelated changes observed and preserved;
- focused checks executed, with exit codes or summaries;
- checks not run and why;
- external blockers and the minimum next action;
- whether the result is complete within the requested scope or remains limited.

## Safe verification boundaries

- Never read or print secret values, credentials, tokens, cookies, private keys, or unnecessary personal data to obtain evidence.
- Never bypass authentication, authorization, row-level security, tenant isolation, validation, TLS, rate limits, or deployment controls to make a check pass.
- Never use a service-role or administrator path as proof that an ordinary user path is authorized.
- Never use an unauthenticated probe as proof of an authenticated or production behavior.
- Never deploy, mutate production data, rotate secrets, or publish artifacts merely because a check would be easier there.
- If the required permission or remote session is unavailable, classify the check honestly and request the smallest safe unblock.

## Reusable checklist

- [ ] Acceptance claims are explicit and scoped.
- [ ] The exact final diff was inspected before and after checks.
- [ ] Existing unrelated changes were preserved.
- [ ] Checks are proportional and use the repository’s configured tooling.
- [ ] Focused tests and relevant static checks ran freshly.
- [ ] Each check has exactly one status: PASS, FAIL, NOT_RUN, or BLOCKED_EXTERNAL.
- [ ] Static, local, remote, and production evidence are not conflated.
- [ ] Secrets and permission boundaries were protected.
- [ ] No completion claim exceeds the evidence.
