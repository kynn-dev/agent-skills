# Debugging

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`debugging` is a root-cause workflow for bugs, failed tests, regressions, incidents, performance problems, and other unexpected behavior.

Its defining rule is simple: investigate before correcting. The skill separates diagnosis from implementation so an agent cannot quietly jump from “this might be the cause” to “I changed the code” without first building evidence.

## Why it exists

LLM debugging often fails in a predictable way: the model sees an error, recognizes a familiar pattern, and patches the first plausible location. Sometimes that works. When it does not, the patch can hide the symptom, introduce a second bug, or leave the actual failing boundary untouched.

This skill forces a narrower sequence: reproduce, collect sanitized evidence, state a falsifiable hypothesis, isolate the boundary, then apply the smallest correction that the evidence actually supports.

## When to use it

Use it for:

- reproducible application bugs;
- failing unit/integration tests;
- build or integration failures;
- performance or concurrency regressions;
- incidents with an authorized evidence source;
- unexpected behavior where the user wants a diagnosis before deciding whether code should change.

Do not use it to invent product requirements, perform speculative feature work, or justify unrelated cleanup while touching a bug.

## How it works

1. Define expected behavior, actual behavior, affected scope, and environment.
2. Attempt the smallest safe reproduction before editing.
3. Collect only the evidence needed to distinguish plausible causes.
4. Label statements as `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN` where that distinction matters.
5. Form a falsifiable hypothesis: if cause X is responsible, observation Z should occur.
6. Change one variable or boundary at a time to test it.
7. Once the root cause is confirmed, apply the smallest coherent correction.
8. Re-run the original reproduction and add a focused regression check when practical.

## Expected inputs

Useful debugging inputs include:

- a concrete symptom or failed command;
- expected versus actual behavior;
- relevant environment/version information;
- a safe way to reproduce or inspect the failure;
- sanitized logs, traces, test output, or code paths when available;
- the scope of whether diagnosis only or diagnosis + implementation is authorized.

Secrets, credentials, private user data, or destructive production experimentation are not valid debugging shortcuts.

## Expected results

A successful run should produce:

- reproduction status;
- evidence separated from inference;
- one or more explicit hypotheses;
- the experiment used to distinguish them;
- a confirmed root cause with confidence and limits;
- the smallest correction, if implementation was requested;
- evidence that the original symptom no longer reproduces;
- a regression check when practical;
- remaining `NOT_RUN` or `BLOCKED_EXTERNAL` validation clearly identified.

If the issue cannot be reproduced and the evidence does not isolate a cause, an honest diagnosis-only result is better than a speculative patch.

## Example

Imagine an API starts returning intermittent 500s after a dependency update. A weak debugging flow might immediately pin the old dependency. This skill would first reproduce the failure, compare a known-good request, inspect the relevant trace, test whether the dependency boundary actually changes the failure, and only then decide whether the dependency is the root cause or merely correlated with it.

## Specific design choices

The workflow deliberately prevents several common shortcuts:

- a plausible stack trace interpretation is not yet a root cause;
- a mock can prove local contract behavior but not remote provider health;
- a 401/403 proves access was denied, not that auth should be bypassed;
- a timeout or remote 5xx is evidence about an external boundary, not automatically an application bug;
- a patch that “seems to help” is not kept when the original hypothesis was not confirmed;
- unrelated refactoring is not smuggled into a bug fix.

## Works well with

- [`engineering-verification`](../engineering-verification/README.md) to prove the final correction and surrounding behavior;
- [`security-review`](../security-review/README.md) when the failure involves auth, tenant isolation, secrets, or untrusted input;
- [`orchestrated-delivery`](../orchestrated-delivery/README.md) when a debugging result feeds a larger implementation/release workflow.

## Limitations

Not every issue can be reproduced locally. External outages, race conditions, timing-sensitive incidents, missing telemetry, or unavailable authenticated environments may keep part of the diagnosis uncertain.

The skill does not turn missing evidence into certainty. When the minimum safe experiment is unavailable, the expected result is a documented boundary and next diagnostic action.

## Agent contract

For the exact diagnosis/implementation separation, hypothesis format, safe evidence rules, regression requirements, and handoff fields, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
