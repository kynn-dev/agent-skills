# Skill authoring

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`skill-authoring` is a method for turning a repeated agent workflow into a small, routable, testable skill package instead of a giant prompt that activates everywhere.

It focuses on four things: clear trigger boundaries, a compact operational contract, progressive disclosure for optional detail, and realistic activation/behavior testing.

## Why it exists

A reusable skill can fail even when its prose is good. It may trigger on the wrong requests, overlap another skill, hide important assumptions in metadata, depend on unavailable runtime behavior, or grow into a manual that consumes context every time it loads.

This skill treats authoring as contract design. The description decides when the skill should route. `SKILL.md` defines the common workflow. References and scripts exist only when they materially improve execution.

## When to use it

Use it when creating, revising, or evaluating an agent skill, especially when you need to decide:

- what user intent should activate it;
- which nearby requests should not activate it;
- what inputs and side effects are allowed;
- what belongs in the common body versus `references/`;
- whether a deterministic helper script is justified;
- how to test routing and blocked-capability behavior.

Do not use it for ordinary project documentation, a one-off prompt rewrite, or for executing another skill's domain workflow.

## How it works

1. Define the intended request, observable outcome, exclusions, side effects, and host capabilities.
2. Design positive triggers and nearby exclusions before writing the body.
3. Keep the frontmatter small and discriminating.
4. Put shared operational behavior in `SKILL.md`.
5. Move conditional detail into references only when progressive disclosure saves context or improves clarity.
6. Add scripts only for genuinely deterministic/repeated work.
7. Test direct positives, natural-language variants, near misses, and missing-capability cases.
8. Run the package validator and record what it proves — and what it does not.

## Expected inputs

A good authoring task should provide or establish:

- the kind of request the skill is meant to handle;
- the desired observable result;
- the closest competing or excluded workflows;
- important authority or side-effect boundaries;
- host tools/capabilities the skill may rely on;
- examples of realistic user phrasing when available.

## Expected results

A successful result is a skill package that is:

- discoverable by a specific trigger description;
- narrow enough not to hijack neighboring requests;
- operational rather than persona-driven;
- explicit about evidence and stop conditions;
- compact enough for routine loading;
- supported by working local links/resources;
- tested with at least positive and exclusion cases;
- honest about `PASS`, `FAIL`, `NOT_RUN`, and `BLOCKED_EXTERNAL` states.

The result is not “a longer prompt.” It is a reusable contract with predictable activation and behavior.

## Example

Suppose you want a reusable database-migration skill. Writing “You are an expert database engineer” is not enough. The authoring process should define what migration requests trigger it, when a generic backend workflow should handle the task instead, what schema/data safety invariants exist, which evidence proves a migration is valid, and when the workflow must stop for authority or production access.

## Specific design choices

This skill deliberately discourages:

- unsupported identity/persona instructions;
- giant always-loaded manuals;
- empty `references/` or placeholder directories;
- provider-specific assumptions when capability-based wording is enough;
- scripts that merely wrap prose;
- keyword-only activation tests;
- pretending a structural validator proves the skill behaves correctly in real prompts.

## Works well with

- [`engineering-verification`](../engineering-verification/README.md) for evidence-backed validation of skill changes;
- [`adaptive-agent-routing`](../adaptive-agent-routing/README.md) when the authored skill participates in larger routed workflows;
- [`orchestrated-delivery`](../orchestrated-delivery/README.md) when a skill change itself is implemented and reviewed as a bounded delivery task.

## Limitations

A skill cannot compensate for an inherently ambiguous product requirement. Activation tests also remain samples, not mathematical proof that every future request will route perfectly.

The authoring workflow should improve routing from observed failures over time instead of accumulating defensive prose for hypothetical cases that have never occurred.

## Agent contract

For the exact frontmatter rules, progressive-disclosure requirements, evaluation matrix, validator command, and revision/removal behavior, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
