---
name: debugging
description: Use when investigating a bug, test failure, incident, performance regression, or unexpected behavior; require reproduction, evidence, a testable hypothesis, isolation, a minimal correction, and regression validation. Keep diagnosis separate from implementation and bound conclusions when an external dependency is unavailable.
---

# Debugging

Use this skill to turn an observable failure into an evidence-backed root-cause finding and, only after that, a narrowly scoped correction. It is a diagnostic discipline, not permission to change code speculatively.

## Non-negotiable invariant

> Do not implement a correction before investigating the root cause, and do not present diagnosis as implementation.

A plausible symptom patch, a guessed external cause, or a test written after an unverified change is not a completed debugging cycle.

## When to use

Use for:

- bugs, regressions, failed tests, build or integration failures, and unexpected behavior;
- production or staging incidents where an observable symptom and safe evidence source exist;
- intermittent, performance, concurrency, data, or third-party integration failures;
- a request to explain a failure before deciding whether a code change is justified.

Do not use to invent a feature from an ambiguous request, to replace a missing acceptance criterion, or to justify changing unrelated code. If there is no observable symptom, first clarify the expected behavior and the boundary of the investigation.

## Required separation

### Diagnosis

The diagnosis must establish:

1. the expected behavior and the actual behavior;
2. a reproduction or a precise explanation of why reproduction is unavailable;
3. sanitized evidence from the relevant execution path;
4. a hypothesis that predicts an observation and a controlled test of that hypothesis;
5. the smallest confirmed root cause and its confidence, scope, and limits.

If the request is diagnosis-only, stop after reporting this information. Do not silently implement the proposed fix.

### Implementation

Implementation starts only when a correction is requested or otherwise explicitly in scope and the diagnosis justifies it. The implementation must:

- change the smallest coherent surface that addresses the confirmed cause;
- preserve existing behavior outside the affected path;
- avoid unrelated cleanup, refactoring, dependency upgrades, or production changes;
- include focused regression evidence for the original symptom.

## Operating procedure

### 1. Establish the boundary

Record the issue, expected result, actual result, affected scope, and the decision that the investigation must support. Inspect the current worktree or diff before editing so existing work is not mistaken for the cause or overwritten.

Mark each statement as FACT, INFERENCE, HYPOTHESIS, or UNKNOWN. Do not turn an inference into a root-cause claim merely because it is familiar.

### 2. Reproduce before correcting

Attempt the smallest safe reproduction before changing the implementation:

- preserve the exact input, preconditions, command or request shape, environment class, version, and timing that matter;
- run the reproduction more than once when the symptom may be intermittent;
- compare a known-good case with the failing case when possible;
- reduce the case until one boundary or transition explains the failure;
- capture the original failure before applying any change.

If the issue cannot be reproduced, report `NOT_REPRODUCED` or the applicable validation status and remain in diagnosis. A non-reproduced issue may justify a narrowly scoped observation or instrumentation change only when that action is explicitly authorized; it does not justify a speculative fix.

### 3. Gather sanitized evidence

Inspect the named execution path and collect only evidence needed to distinguish hypotheses:

- error text, stack or trace shape, status code, timing, state transition, and relevant version or configuration names;
- focused logs, metrics, request metadata, test output, and the current diff;
- boundary evidence showing whether the failure occurs before, inside, or after the component under investigation;
- a minimal data sample or a redacted identifier when data shape matters.

Never print, copy, persist, or paste secrets, tokens, cookies, private keys, credentials, or unnecessary personal data into logs or reports. Redact values and use classifications, hashes, or stable placeholders when correlation is required.

### 4. State and test one hypothesis

Write a falsifiable hypothesis in this form:

> If cause X is responsible under condition Y, observation Z should occur; if X is not responsible, observation Z should not occur.

Prefer one variable per experiment. Use a focused test, controlled fixture, safe stub, comparison against a known-good path, targeted trace, or binary search across a boundary. Record what the experiment actually proved and what it did not prove.

### 5. Isolate the failing boundary

Separate application logic from inputs, persistence, network calls, authentication, queues, caches, clocks, and other dependencies. Use a minimal fixture or a controlled substitute when that makes the boundary observable.

Isolation is not a license to weaken security or behavior. Do not disable authorization, validation, tenant checks, TLS, rate limits, or error handling merely to make the failure easier to trigger. A mock can establish an application-side contract; it cannot prove that the real dependency is healthy.

### 6. Apply the minimal correction

After the hypothesis is confirmed:

1. state the root cause and the evidence that confirms it;
2. identify the smallest correction and the behavior it must preserve;
3. make one coherent change at a time;
4. re-run the original reproduction before adding unrelated improvements.

If the hypothesis is not confirmed, do not keep the patch because it appears to help. Revert the speculative change in the working set and form the next testable hypothesis, while preserving unrelated worker changes.

### 7. Prove regression behavior

Add or update a focused regression check that demonstrates the original failure and the intended behavior. When practical, verify the check fails against the pre-correction behavior and passes after the correction. Also run the narrowest relevant static check or neighboring test that could catch an accidental break.

If a regression check cannot run because of an unavailable environment, dependency, credential, or service, report `NOT_RUN` or `BLOCKED_EXTERNAL` with the exact boundary and do not call the correction proven.

### 8. Report the result

A useful debugging report contains:

- symptom, expected behavior, actual behavior, and reproduction status;
- evidence with FACT/INFERENCE/HYPOTHESIS/UNKNOWN labels;
- hypothesis, experiment, observed result, and confirmed root cause;
- files or boundaries changed, if implementation was in scope;
- focused regression and static validation results;
- external limits, unexecuted checks, residual risk, and recommended next action.

## External failure boundaries

An external timeout, outage, quota, invalid remote response, unavailable authenticated session, or network restriction is evidence about the boundary, not automatic proof of an application defect.

| External observation | Safe conclusion | Required limit |
| --- | --- | --- |
| Timeout, connection failure, or remote 5xx | The dependency was not successfully observed | Do not claim the local fix is proven; use a controlled stub or authorized sandbox if appropriate |
| Remote 401, 403, or unavailable credentials | The attempted access was not validated | Do not create, expose, or bypass credentials; record the blocked auth boundary |
| Rate limit, quota, or provider outage | The experiment was constrained | Do not disable limits or retry without bound; report the external dependency as a limitation |
| Production-only data, configuration, or telemetry is unavailable | Local or static evidence may still be collected | Do not infer production behavior or claim a production incident is fixed |
| A third-party result differs from a local stub | The contract boundary may be involved | Test the contract and record the real dependency as unverified |

When an external condition prevents an acceptance-relevant experiment, use `BLOCKED_EXTERNAL` in the validation report. Do not relabel it PASS because the code looks plausible.

## Red flags: stop and return to diagnosis

- a proposed patch exists before a reproduction or evidence record;
- the explanation is only “it works locally” or “the provider is obviously broken”;
- several unrelated files are changed before the hypothesis is tested;
- a log statement would include a token, cookie, secret, or private payload;
- a test is being written to match an already-applied speculative fix;
- authorization, validation, tenant isolation, TLS, or rate limiting is being disabled to reproduce the issue;
- a fix is being claimed while the original symptom or required external boundary was never re-tested.

## Reusable checklist

- [ ] Expected and actual behavior are explicit.
- [ ] Existing worktree changes and the relevant execution path were inspected.
- [ ] The original symptom was reproduced, or the inability to reproduce is documented.
- [ ] Evidence is sanitized and separated from inference.
- [ ] A falsifiable hypothesis and controlled experiment were recorded.
- [ ] The failing boundary was isolated without weakening security controls.
- [ ] The correction is minimal and tied to a confirmed cause.
- [ ] A focused regression check covers the original symptom.
- [ ] External failures and unrun checks are labeled instead of guessed away.
- [ ] Diagnosis and implementation are reported as separate stages.
