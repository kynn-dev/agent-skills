# Context packet construction

Use this reference after the router selects a context scope/budget. The captain resolves abstract context policy into real repository material.

## Principle

A worker should receive enough information to execute its bounded node correctly, but not the captain's entire universe.

Context quality is measured by relevance and contract completeness, not raw token count.

## Required packet fields

Every worker packet should contain:

```text
ROLE
<bounded worker role>

OBJECTIVE
<one coherent node objective>

ACCEPTANCE_CRITERIA
<observable pass conditions>

ALLOWED_SCOPE
<files, directories, interfaces, or read/write boundaries>

RELEVANT_CONTEXT
<curated files/excerpts/summaries>

DEPENDENCIES
<upstream nodes/contracts this node relies on>

INVARIANTS
<behavior/data/security constraints that must remain true>

PROHIBITED_SIDE_EFFECTS
<what the worker must not mutate, deploy, publish, or infer>

VALIDATION
<narrow checks expected from this worker>

OUTPUT_CONTRACT
<patch/artifact/report shape and evidence required>
```

## Context scope mapping

### `single_file`
Use when one file is sufficient and external contracts are obvious. Include the exact target file, objective, acceptance criteria, and one short note for any non-obvious invariant.

### `target_files`
Use for a small coherent edit across a few directly related files. Include exact targets, nearby tests/types only when directly relevant, acceptance criteria, and the current diff when dirty-worktree state matters.

### `module`
Use when the worker must understand a local abstraction rather than individual files. Include owning module files, public interfaces/types, module tests, and a concise architecture summary.

### `module_plus_dependencies`
Use for schema, API contracts, shared libraries, and integration-sensitive changes. Include the owning module, direct dependency/consumer interfaces, relevant tests, and migration/compatibility invariants when applicable.

### `subsystem`
Use for work spanning a meaningful product subsystem. Include a subsystem architecture digest, key modules/interfaces, relevant data flow, representative tests, and accepted spec/ADR sections.

### `repository`
Reserve for architecture-wide work, repository-level migrations, or cross-cutting review where narrower context demonstrably fails. Still curate rather than dumping every file.

### `cross_system`
Use only when correctness depends on multiple repositories/services or an external contract. Explicitly name each system and why it is needed.

## Context budget classes

- `micro`: roughly 1–4k useful tokens.
- `small`: roughly 4–12k.
- `medium`: roughly 12–30k.
- `large`: roughly 30–80k.
- `broad`: captain-curated exceptional context when narrower packets are inadequate.

These are soft planning targets, not hard tokenizer limits.

If the packet exceeds the selected class because raw files are large, summarize stable background and include only the exact source sections required for the task.

## What not to include by default

Do not automatically forward:

- the full parent goal;
- the full conversation history;
- unrelated roadmap phases;
- secrets or `.env` values;
- unrelated architecture documents;
- every test file;
- every dependency implementation;
- outputs from sibling workers that are not dependencies;
- historical debug logs after the relevant conclusion is summarized.

## Dirty-worktree context

When a worker touches files already modified before its node started, include the baseline ownership note, current diff for only the overlapping files, and an explicit instruction to preserve pre-existing changes.

If ownership cannot be established, do not assign the write to a subagent; return it to the captain.

## Visual and specialist tasks

For visual UI, graphics, 3D, audio, or other specialist work, include the relevant visual/spec artifacts in addition to code: screenshots/references, dimensions or interaction constraints, performance target, device/browser constraints, and exact acceptance criteria.

Do not compensate for missing specialist inputs by sending unrelated repository context.

## Review packet

Reviewer packets should usually be smaller than implementation packets. Include objective and acceptance criteria, changed files/diff, relevant invariants, validation evidence, known gaps (`NOT_RUN` / `BLOCKED_EXTERNAL`), and only the source context required to judge the change.

Do not send the full repository or parent goal to a reviewer solely because the implementation task was large.
