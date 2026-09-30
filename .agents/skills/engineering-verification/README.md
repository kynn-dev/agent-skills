# Engineering verification

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`engineering-verification` is the evidence gate between “a change exists” and “the change is complete.” It helps an agent translate acceptance criteria into fresh, proportionate checks and report exactly what those checks prove.

The skill is intentionally skeptical of vague completion language. A clean diff, a passing lint command, a worker saying “done,” or a successful local test may each be useful evidence, but none automatically proves every runtime, security, compatibility, or production claim around the change.

## Why it exists

Software agents are very good at producing plausible completion narratives. Verification needs the opposite instinct: reduce claims to observable behavior, select the narrowest useful check, execute it after the final edit, and preserve the scope of the evidence.

This avoids two common failure modes:

- **under-verification**, where one green command is stretched into a much larger claim;
- **ritual verification**, where agents run a huge generic suite without asking whether it actually proves the requested behavior.

## When to use it

Use it after code, configuration, migration, documentation, dependency, or infrastructure-boundary changes; when a worker reports completion; or when a review needs explicit evidence and limitations.

It is especially useful when the user cares about phrases such as “working,” “safe,” “responsive,” “production-ready,” “fixed,” or “verified,” because those words need a defined scope.

## How it works

1. Translate the request into observable acceptance claims.
2. Inspect the baseline and exact final diff.
3. Choose focused checks proportional to the changed surface and risk.
4. Execute the selected checks freshly after the final edit.
5. Record the command/evidence source, scope, result state, and limitation.
6. Re-inspect the worktree because tests/builds can modify generated files.
7. Make a completion claim only as broad as the evidence supports.

The four package-standard states are:

- `PASS` — the check ran and supports the named claim within its scope;
- `FAIL` — the check ran and found an unmet criterion or regression;
- `NOT_RUN` — the check was relevant/requested but was not executed;
- `BLOCKED_EXTERNAL` — the check could not run because of an external dependency, identity, permission, or environment boundary.

## Expected inputs

A good verification task provides or establishes:

- the user request and acceptance criteria;
- the exact changed files/diff;
- the project’s real test/build/lint/type tooling;
- the risk and dependency surface;
- environment boundaries such as local, staging, remote authenticated, or production;
- any known external blockers.

## Expected results

A successful verification produces a compact evidence map rather than a confidence paragraph. Each acceptance-relevant claim should have:

- the command, inspection, or runtime observation used;
- the environment/scope in which it ran;
- a `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED_EXTERNAL` state;
- a concise statement of what the evidence proves and what it does not.

The final result should also note changed files, preserved unrelated changes, checks not run, external blockers, and residual risk.

## Example

Suppose a user asks whether an authentication fix is complete. A linter can support syntax/style claims, and a focused unit test can support specific token-handling behavior. Neither proves that a real ordinary user is authorized correctly in production. If the remote authenticated environment is unavailable, that check remains `BLOCKED_EXTERNAL`; the skill does not silently promote local evidence into production proof.

## Specific design choices

The workflow separates evidence classes because they answer different questions:

- static inspection can show structure but not runtime correctness;
- focused tests prove only the exercised behavior and fixtures;
- local runtime proves that local environment and path;
- staging proves the exact authorized staging path tested;
- production evidence proves only the explicitly authorized production path exercised.

The skill also requires re-checking the final diff after validation so the state being claimed as verified is actually the state that was tested.

## Works well with

- [`debugging`](../debugging/README.md) after a root cause has been corrected;
- [`orchestrated-delivery`](../orchestrated-delivery/README.md) as the evidence gate before independent review/release;
- [`security-review`](../security-review/README.md) for negative authorization and boundary checks;
- [`frontend-design`](../frontend-design/README.md) where code checks must be complemented by rendered/interaction evidence.

## Limitations

No validation plan can prove every possible behavior. Tests are samples of behavior, environments can differ, and external dependencies may be unavailable.

The skill’s job is not to manufacture certainty; it is to make the evidence boundary explicit so the completion claim cannot exceed it.

## Agent contract

For exact status semantics, evidence-scope rules, proportional-check guidance, safe verification boundaries, and the evidence-report template, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
