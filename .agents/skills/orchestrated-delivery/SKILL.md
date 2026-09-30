---
name: orchestrated-delivery
description: Use when a bounded software change needs coordinated workers, independent review, and an evidence-backed release gate; do not use for a small local edit, architecture discovery, or an unauthorized production operation.
---

# Orchestrated delivery

Run a bounded change from repository audit through an explicit integration and publication decision. Keep the primary agent accountable for scope, architecture, integration, evidence, and authorization; use workers only for isolated, verifiable work units.

## Operational contract

### Objective

Coordinate a bounded engineering change from audit to integration without letting delegation blur ownership, evidence, or authorization. Workers may implement isolated nodes, but the primary agent owns the plan, exact diff, aggregate validation, review handoff, integration, and any decision to perform an external effect.

### Expected inputs

The workflow expects a concrete request with observable acceptance criteria, repository/worktree state, applicable instructions, known risk boundaries, allowed paths or interfaces, available validation tooling, and the user's authorization boundary for commit/push/merge/deploy/release or production mutation.

### Required outputs

Produce an audit record, bounded DAG/work orders, worker evidence, an integrated diff, proportional validation states, independent review when required, any review-driven delta and revalidation, and an explicit external-effects record. Preserve pre-existing work and distinguish it from task changes.

### Definition of done

The delivery is complete only when all required nodes are resolved, the exact final diff has been inspected, acceptance-relevant validation is explicit, required independent review is `APPROVE`, unresolved risks are surfaced, and no external effect exceeds the user's authorization. A worker's PASS or one green command is never the overall completion gate.

## Ownership and operating boundary

- **Primary owner:** establishes scope and acceptance criteria, reads repository instructions, owns the plan/DAG, assigns work, inspects every worker diff, integrates changes, runs aggregate checks, requests independent review, and makes the final release decision.
- **Worker:** owns one explicitly bounded node of the DAG. The work order names allowed paths, inputs, outputs, dependencies, acceptance checks, and prohibited side effects. A worker does not publish, deploy, or decide that the overall task is complete.
- **Independent reviewer:** receives a fresh review brief after integration and proportional validation. The reviewer checks the actual diff and evidence; it is not the implementer and must not be given a presumed conclusion.
- **User or release owner:** authorizes material external effects such as commit, push, merge, deploy, release, publication, or production mutation.

Preserve dirty worktrees. Capture the baseline before editing, distinguish pre-existing changes from task changes, and never use reset, clean, stash, checkout, or an equivalent overwrite merely to make a worktree convenient.

## Required result states

Use these exact labels in work orders, validation notes, and handoffs:

- `PASS`: the named check ran and satisfies the stated criterion.
- `FAIL`: the named check ran and found a defect, regression, or unmet criterion.
- `NOT_RUN`: the check was not executed. Do not infer a pass from static inspection or another check.
- `BLOCKED_EXTERNAL`: the check requires unavailable authority, credentials, service state, network access, or another external condition.

`APPROVE` is reserved for an independent review gate. It is not implied by a worker report, a green local command, or a successful tool call.

## Required delivery sequence

### 1. Audit

Before planning or delegation:

1. Read applicable repository instructions and acceptance criteria.
2. Confirm repository root, branch/worktree identity, target paths, and authorized side effects.
3. Record `git status` and the relevant diff without exposing secrets. Mark pre-existing changes and possible ownership collisions.
4. Map the named execution path far enough to identify owning files, tests, interfaces, and external boundaries.
5. Classify risk. Stop for an explicit decision when work would change authentication/authorization, tenant isolation, cryptography, billing, legal/compliance behavior, production infrastructure, irreversible data, destructive operations, or a public contract whose compatibility is unknown.

### 2. Plan the DAG

Convert the request into bounded nodes. For every node record:

- node id and accountable owner;
- exact allowed files or interfaces;
- inputs, outputs, acceptance checks, and evidence format;
- dependencies and why they exist;
- risk boundary and prohibited side effects;
- whether the primary agent must retain the change because it is shared, architectural, security-sensitive, or integration-heavy.

Run independent nodes in parallel only when write sets and assumptions do not overlap.

### 3. Assign workers

Give each worker a self-contained work order containing user intent, node boundary, relevant files, constraints, acceptance checks, and required report fields. Require the worker to:

- inspect the execution path before editing;
- make the smallest coherent change inside assigned paths;
- preserve unrelated dirty changes and repository conventions;
- add focused tests when appropriate;
- run the narrowest useful validation and report exact commands/outcomes;
- return `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED_EXTERNAL` with evidence, assumptions, deviations, risks, and blockers.

Do not treat a worker's status as proof. The primary agent independently inspects files and diff after every worker result.

### 4. Integrate in the primary worktree

Review each worker's actual changes against baseline and acceptance criteria. Check file scope, behavior, compatibility, tests, and accidental edits. Resolve conflicts deliberately and preserve unrelated work. Re-run relevant checks after combining nodes; a passing worker check does not cover integration behavior.

### 5. Validate proportionally

Start with the narrowest relevant test, lint, type, build, or static validation, then expand according to risk and dependency surface. Validate both the changed path and important neighboring contracts.

For every expected check, record command, scope, result state, and concise evidence. Mark unavailable authenticated, production, or external checks `NOT_RUN` or `BLOCKED_EXTERNAL`; never upgrade them through inference.

### 6. Request independent review

After integration and proportional validation, provide a fresh reviewer with:

- original request and acceptance criteria;
- audit boundary and relevant baseline;
- integrated diff or exact changed files;
- validation commands and result states;
- known unknowns and external checks that were not run.

Ask for an independent assessment of scope, regressions, security and permission boundaries, compatibility, tests, operational risk, and release readiness. The review returns `APPROVE` only when evidence supports it.

### 7. Apply the delta

Translate review findings into a minimal delta. Re-run affected validation after every correction. Any material delta invalidates the prior approval for that surface and requires fresh review.

### 8. Commit, push, merge, deploy

Only after required validation is `PASS` and required independent review is `APPROVE`:

1. synchronize relevant worktrees/branch state without overwriting dirty changes;
2. commit only exact requested files and only when commit authority was granted;
3. push only when push authority was granted;
4. treat merge, deploy, release, tag, production mutation, or public publication as separate external effects with their own authorization boundary.

If commit/push was not authorized, leave the reviewed diff intact and report the exact next action instead of assuming permission.

## Risk limits and stop conditions

Stop and return evidence rather than guessing when:

- a requested change crosses an auth, tenant-isolation, secret, cryptography, billing, legal, migration, destructive, or production boundary without authority;
- an external service, authenticated session, approval, or permission is unavailable;
- two workers modify overlapping files without a resolved owner;
- acceptance criteria conflict with repository instructions or another explicit constraint;
- a check fails and the smallest safe correction is unclear;
- worktree changes have unclear ownership.

Do not weaken tests, linting, type checks, security checks, or permission boundaries to obtain PASS.

## Handoff record

```text
OBJECTIVE
<bounded request and acceptance criteria>

OWNERSHIP
<primary, worker nodes, reviewer, authorization boundary>

AUDIT
<baseline, dirty-worktree preservation, scope, risks, unknowns>

DAG
<nodes, dependencies, write sets, completed/blocked nodes>

CHANGES
<integrated files and pre-existing changes preserved>

VALIDATION
<command | PASS/FAIL/NOT_RUN/BLOCKED_EXTERNAL | evidence>

REVIEW
<APPROVE or exact findings/state>

DELTA
<review-driven changes and revalidation>

EXTERNAL_EFFECTS
<what was authorized/performed; otherwise exact next action>

RISKS_AND_BLOCKERS
<unresolved risks, external blockers, deviations>
```
