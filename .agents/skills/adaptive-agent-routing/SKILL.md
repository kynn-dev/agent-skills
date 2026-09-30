---
name: adaptive-agent-routing
description: Use when a large or heterogeneous software goal should be decomposed across subagents and worker capability, reasoning effort, context packet, parallelism, and review strength should vary by task difficulty and risk; do not use for a small local edit, a single bounded worker task, or release authorization itself.
---

# Adaptive agent routing

Route heterogeneous work to the cheapest capable worker with the minimum sufficient context, while a broad-context primary captain retains ownership of architecture, integration, evidence, and overrides. Use a fast structured decision model for closed-set routing judgments; use the captain for semantic decomposition and final routing authority.

This skill complements `orchestrated-delivery`: use adaptive routing to choose workers and context for DAG nodes, then use the delivery skill's validation, independent review, and release gates for integration and publication.

## Operating model

Use four layers:

1. **Primary captain** — retains the broad goal, repository state, architecture, acceptance criteria, dirty-worktree state, and integration responsibility.
2. **Decision router** — receives a compact task descriptor and returns closed-set routing attributes. A cheap structured router such as Jev is a strong fit when available because routing questions are bounded and auditable. The router never receives secrets and never becomes factual authority.
3. **Workers** — receive one bounded work order, the minimum sufficient context, exact acceptance checks, and prohibited side effects. Workers do not inherit the captain's full conversation by default.
4. **Reviewers** — are selected after deterministic validation according to residual risk, blast radius, and ambiguity. Strong reviewers are not a substitute for tests and are not assigned merely because they are available.

The primary captain may override any router recommendation. Log the recommendation, the final route, and the reason for override when one occurs.

## Core routing principle

Prefer the least expensive model/effort expected to complete the bounded node reliably, then rely on deterministic validation and targeted review.

Do not assign a stronger model solely because:

- the task is part of a large goal;
- the repository is large;
- the strongest model is currently available;
- the parent captain uses high effort;
- the task produces many lines of code.

Route by semantic difficulty, ambiguity, blast radius, reversibility, specialist depth, and validation quality. A five-line migration that can corrupt data may deserve stronger handling than a 500-line isolated component.

## Required workflow

### 1. Decompose before routing

The captain first converts the user goal into a DAG of bounded nodes. Each node must identify:

- objective;
- acceptance criteria;
- likely owning files/interfaces;
- dependencies;
- known invariants;
- prohibited side effects;
- whether the node can run in parallel;
- whether another node owns a shared contract.

Do not ask the router to invent the project plan from raw repository context. Routing begins after the captain has a meaningful task descriptor.

### 2. Ask the router closed-set questions

For each node, obtain structured decisions covering at least:

- task class;
- difficulty;
- risk;
- blast radius;
- reversibility;
- semantic depth;
- specialist role;
- context scope;
- context budget class;
- recommended worker class and effort;
- parallelizability;
- deterministic-validation expectation;
- independent-review requirement and strength.

Use the canonical decision vocabulary in [references/routing-contract.md](references/routing-contract.md). Preserve probabilities/confidence where the router provides them. Do not collapse uncertain routing into false certainty.

### 3. Captain validates the route

Before spawning a worker, the captain checks the recommendation against repository reality.

Override when, for example:

- the router missed a data, auth, migration, billing, infrastructure, or compatibility boundary;
- the task touches shared files owned by another node;
- the suggested context is too narrow to preserve a required contract;
- the suggested model is disproportionately strong for a mechanical task;
- a specialist capability is genuinely required;
- the task is already deterministic and should be handled by code rather than a model.

A route is a recommendation, not authorization.

### 4. Build the minimum sufficient context packet

The router chooses a context policy; the captain chooses the actual files and excerpts.

Never ask a lightweight router to materialize repository context by itself. It may say `target_files`, `module_plus_dependencies`, or `include_tests`; the captain resolves those labels to real inputs.

Use [references/context-packet.md](references/context-packet.md) to construct the worker packet. Context is a budget, not a convenience. Prefer summaries, exact files, interfaces, tests, and acceptance criteria over dumping the parent goal or whole repository.

Do not include secrets, unrelated user history, unrelated files, or the full parent conversation unless the bounded node truly requires them.

### 5. Spawn the worker

Every worker receives a self-contained contract containing:

- role;
- objective;
- acceptance criteria;
- allowed files/interfaces;
- selected relevant context;
- invariants;
- tests/checks to run;
- prohibited side effects;
- required output/evidence;
- whether delegation is allowed.

Workers should normally not delegate further unless the captain explicitly created a sub-captain node.

### 6. Validate deterministically first

Before routing independent review, run the narrowest useful deterministic checks available:

- unit/integration tests;
- type checking;
- lint/static analysis;
- schema validation;
- diff/path-scope checks;
- invariant checks;
- data reconciliation;
- build or targeted runtime checks.

Do not spend a stronger reviewer on failures a deterministic check can identify first.

### 7. Route the review separately

Worker routing and reviewer routing are separate decisions.

A task may use a cheap worker but require a strong reviewer because it is risky or hard to reverse. A difficult but isolated task may use a strong worker and need only a light review if deterministic evidence is comprehensive.

Ask the router to classify residual review need after validation using the same risk/blast-radius/reversibility information plus actual check results.

Typical defaults:

- trivial mechanical change + strong deterministic checks → no independent model review;
- bounded low-risk business logic → light independent review or captain integration review;
- auth, security, migrations, schema, financial logic, data integrity, infrastructure, cross-system contracts → strong independent review;
- specialized graphics/3D, mathematically difficult work, deep architecture, or unusually ambiguous failure analysis → stronger specialist worker/reviewer when justified;
- the strongest available tier is exceptional and must have a recorded reason.

Treat these as capability tiers, not fixed provider/model policy. Map them to whatever models are actually available.

### 8. Integrate and learn from outcomes

The captain owns integration. After each node record:

- router recommendation;
- captain route/override;
- worker outcome;
- deterministic validation result;
- reviewer findings;
- rework required;
- approximate latency/cost when available.

Use the calibration procedure in [references/calibration.md](references/calibration.md) to identify systematic over-routing, under-routing, context bloat, and reviewer waste. Do not hardcode thresholds from a tiny sample.

## Capability-tier mapping

Keep routing semantics separate from provider/model names:

- `deterministic_tool` → code/script/query rather than a model;
- `light_worker` → inexpensive model/effort for mechanical or well-bounded work;
- `general_worker` → capable general implementation model;
- `captain_worker` → broad-context/high-reasoning model responsible for planning and integration;
- `strong_worker_*` → stronger specialist/reasoning tiers when task complexity genuinely requires them;
- `strong_reviewer_*` → independent review tiers selected from residual risk after deterministic validation.

See [references/openai-jev-example.md](references/openai-jev-example.md) for one concrete mapping. If those models are unavailable, choose the nearest capability-equivalent option and record the substitution. Do not silently escalate to a more expensive tier.

## Parallelism rules

Parallelize only nodes whose write sets and assumptions are sufficiently independent.

The captain must keep ownership of:

- shared schemas/contracts;
- migrations with interacting dependencies;
- final conflict resolution;
- global manifests;
- integration gates;
- release/apply authorization.

Use many cheap workers for truly independent work rather than one strong model for everything. Do not create subagents merely to maximize concurrency; each spawn must have a bounded useful node.

## Stop and escalation conditions

Escalate to the captain or a stronger worker/reviewer when:

- task scope cannot be bounded confidently;
- router confidence is low across multiple critical dimensions;
- the node crosses auth, security, billing, legal/compliance, irreversible data, migration, or production boundaries;
- deterministic evidence conflicts with the worker conclusion;
- repeated rework indicates the assigned worker tier is insufficient;
- repository context needed exceeds the packet safely available to the worker;
- a specialist discipline is material to correctness.

Do not automatically escalate merely because a worker asks for more intelligence. The captain verifies the reason.

## Result states

Use the package-standard states:

- `PASS`
- `FAIL`
- `NOT_RUN`
- `BLOCKED_EXTERNAL`

For routing, additionally record:

- `ROUTE_ACCEPTED`
- `ROUTE_OVERRIDDEN`
- `ESCALATED`

These describe scheduling decisions, not implementation correctness or release approval.

## Handoff contract

For a routed goal, maintain an auditable routing ledger containing at least:

```text
NODE_ID
TASK_CLASS
DIFFICULTY
RISK
BLAST_RADIUS
REVERSIBILITY
CONTEXT_SCOPE
CONTEXT_BUDGET
ROUTER_RECOMMENDATION
ROUTER_CONFIDENCE
CAPTAIN_ROUTE
ROUTE_STATE
WORKER
VALIDATION
REVIEW_ROUTE
REVIEW_RESULT
REWORK
NOTES
```

End the goal with aggregate routing metrics when useful: worker count by tier, reviewer count by tier, override rate, escalation rate, rework rate, context classes used, deterministic-only nodes, and known calibration gaps.
