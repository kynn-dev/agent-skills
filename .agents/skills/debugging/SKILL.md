---
name: debugging
description: Use when investigating a bug, test failure, incident, performance regression, or unexpected behavior; require reproduction, evidence, a testable hypothesis, isolation, a minimal correction, and regression validation. Do not use for speculative feature work or unrelated cleanup.
---

# Debugging

Turn an observable failure into an evidence-backed root-cause finding and, only after that, a narrowly scoped correction.

## Non-negotiable invariant

> Do not implement a correction before investigating the root cause, and do not present diagnosis as implementation.

## When to use

Use for bugs, regressions, failed tests, build/integration failures, performance or concurrency failures, incidents with a safe evidence source, and requests to explain a failure before deciding whether code should change.

Do not use to invent a feature from an ambiguous request, replace a missing acceptance criterion, or justify changing unrelated code.

## Required separation

### Diagnosis

Establish:

1. expected behavior and actual behavior;
2. a reproduction, or why reproduction is unavailable;
3. sanitized evidence from the relevant execution path;
4. a falsifiable hypothesis and controlled test;
5. the smallest confirmed root cause, with confidence and limits.

If the request is diagnosis-only, stop there.

### Implementation

Only after diagnosis justifies a correction:

- change the smallest coherent surface tied to the cause;
- preserve behavior outside the affected path;
- avoid unrelated cleanup, upgrades, or production changes;
- include focused regression evidence for the original symptom.

## Workflow

### 1. Establish the boundary

Record issue, expected result, actual result, affected scope, environment class, and the decision the investigation must support. Inspect the current worktree/diff before editing.

Label important statements as `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`.

### 2. Reproduce before correcting

Attempt the smallest safe reproduction before changing implementation. Preserve relevant input, preconditions, command/request shape, version, and timing. Compare a known-good case when possible and capture the original failure.

If the issue cannot be reproduced, remain in diagnosis. A non-reproduced issue does not justify a speculative fix.

### 3. Gather sanitized evidence

Collect only evidence needed to distinguish hypotheses: error text, trace shape, status, timing, state transition, focused logs/metrics, test output, diff, and boundary evidence.

Never print or persist secrets, tokens, cookies, private keys, credentials, or unnecessary personal data.

### 4. Test one hypothesis

Use a falsifiable form:

> If cause X is responsible under condition Y, observation Z should occur; if X is not responsible, Z should not occur.

Prefer one variable per experiment. Record what the experiment proved and what it did not prove.

### 5. Isolate the failing boundary

Separate application logic from inputs, persistence, network calls, authentication, queues, caches, clocks, and external dependencies.

Do not disable authorization, validation, tenant checks, TLS, rate limits, or error handling to make reproduction easier. A mock can establish a local contract; it cannot prove the real dependency is healthy.

### 6. Apply the minimal correction

State the confirmed root cause, identify the smallest correction, make one coherent change at a time, then re-run the original reproduction.

If the hypothesis was not confirmed, do not keep a patch merely because it appears to help.

### 7. Prove regression behavior

Add or update a focused regression check. When practical, show that it fails against the pre-correction behavior and passes after the correction. Run the narrowest neighboring/static check needed to catch accidental breakage.

If required validation cannot run because of an unavailable environment, credential, service, or dependency, report `NOT_RUN` or `BLOCKED_EXTERNAL` rather than calling the correction proven.

## External failure boundaries

Timeouts, outages, quotas, remote 5xx, unavailable authenticated sessions, and network restrictions are evidence about a boundary, not automatic proof of an application defect.

A local stub can validate local contract handling; it cannot prove remote provider health. A 401/403 can prove access was not granted; it cannot justify bypassing authentication.

## Handoff

Report:

- symptom and reproduction status;
- evidence with FACT/INFERENCE/HYPOTHESIS/UNKNOWN labels;
- hypothesis, experiment, result, and confirmed root cause;
- files/boundaries changed if implementation was in scope;
- regression and static validation results;
- external limits, unexecuted checks, residual risk, and next action.

## Checklist

- [ ] Expected and actual behavior are explicit.
- [ ] Existing worktree changes were inspected and preserved.
- [ ] Original symptom was reproduced or inability to reproduce is documented.
- [ ] Evidence is sanitized and separated from inference.
- [ ] A falsifiable hypothesis and controlled experiment were recorded.
- [ ] The failing boundary was isolated without weakening controls.
- [ ] The correction is minimal and tied to a confirmed cause.
- [ ] A focused regression check covers the original symptom.
- [ ] External failures and unrun checks are labeled honestly.
- [ ] Diagnosis and implementation are reported separately.
