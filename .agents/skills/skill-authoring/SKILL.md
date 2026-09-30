---
name: skill-authoring
description: Use when creating, evaluating, or revising an agent skill, including frontmatter, trigger boundaries, progressive disclosure, references, scripts, and activation tests; do not use for ordinary application documentation, prompt-only rewrites, or executing a skill's domain workflow.
---

# Skill authoring

Create skills that are discoverable, narrowly routed, operationally useful, and maintainable. Treat a skill as a small contract: its description routes requests, its body defines the common workflow, and optional resources supply only the detail needed for a specific mode.

## Authoring contract

Before writing, record the intended user request, desired observable outcome, in-scope actions, exclusions, side effects, risk boundary, and the host capabilities the skill may rely on. Preserve the user's requested location and authorization. Do not install or activate a skill globally as an implicit part of authoring.

Keep the skill operational. Do not write identity claims, role-play instructions, or instructions that depend on hidden activation state. Replace provider/runtime assumptions with portable file/tool behavior, explicit capability checks, or a documented `NOT_RUN` condition whenever practical.

## Trigger and exclusion design

Define both positive and negative routing before drafting the body:

- positive triggers describe the actual intent, artifact, or decision that requires this skill;
- exclusions name nearby work that should be handled directly or by another skill;
- keep descriptions discriminating and concise;
- test explicit requests, natural-language variants, implicit requests, near misses, and ambiguous prompts.

An ambiguous case should route to clarification or a safer boundary rather than trigger an expansive workflow.

## Required file and frontmatter shape

Each skill is a directory with an uppercase `SKILL.md`.

```yaml
---
name: skill-name
description: Use when <specific trigger>; do not use for <nearby exclusion>.
---
```

Apply these checks:

- `name` is lowercase kebab-case and matches the directory name exactly;
- `description` contains a real trigger boundary and useful exclusion;
- keep only supported optional frontmatter fields;
- put purpose, workflow, constraints, outputs, and validation in the Markdown body rather than hiding them in metadata;
- preserve unrelated established frontmatter when revising an existing skill.

## Progressive disclosure

Keep `SKILL.md` concise enough to load for every matching request. It should contain shared purpose, routing boundary, essential invariants, normal workflow, and links to conditional detail.

Add `references/` only when a focused body would otherwise omit material rules, schemas, domain tables, or mode-specific procedures. Link each reference from the section where it is needed and state when to read it.

Add `scripts/` only when deterministic execution or repeated transformation materially improves reliability. A script must have a narrow interface, avoid hidden side effects/secrets, and be executed in validation. Do not add scripts that merely restate prose or wrap a one-off command.

Do not create empty resource directories, placeholder examples, or copied manuals without a concrete packaging requirement. Every relative link must resolve inside the skill package and every resource must have a caller.

## Write the operational body

Use imperative, evidence-oriented instructions. Include only decisions that change behavior or protect a real boundary:

1. state when the skill applies and when it yields to another workflow;
2. define the smallest useful workflow, including required inputs, ownership, side effects, and stop conditions;
3. identify evidence/artifacts that prove each material result;
4. distinguish `PASS`, `FAIL`, `NOT_RUN`, and `BLOCKED_EXTERNAL`;
5. define a stable output/handoff contract when another worker or skill consumes the result;
6. preserve existing architecture and user scope.

Avoid generic advice that the host already enforces, repetitive policy text, speculative edge cases, and fixed steps where multiple safe approaches are equivalent.

## Evaluate activation and behavior

Use a small realistic evaluation matrix rather than checking whether headings or keywords appear:

| Case | Expected result | Evidence |
| --- | --- | --- |
| Direct positive request | Skill activates and follows intended boundary | Observed routing/output |
| Natural-language variant | Activates without exact wording | Observed routing/output |
| Relevant but implicit request | Activates only when outcome needs it | Observed routing/output |
| Near miss/excluded request | Does not activate or routes safer | Observed non-activation/routing |
| Missing capability/dependency | Reports NOT_RUN/BLOCKED_EXTERNAL without fabricating success | Sanitized blocker evidence |

For a new or materially revised skill, test at least one positive case and one exclusion case. Give the evaluator only the realistic request and minimum relevant artifacts; do not seed the intended answer.

## Local validation

Run the package validator, then perform a scoped link/content audit:

```text
python -B tools/validate_skills.py .
```

The validator proves structural constraints only. Also verify that:

- every relative Markdown link inside the skill resolves;
- the description has both a discriminating trigger and an exclusion;
- references/scripts are justified and linked;
- activation cases cover positive and exclusion prompts;
- no secret, cookie, key, token, or environment value was read, printed, or persisted;
- changed scripts, when any, run successfully within documented scope.

Record each check as `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED_EXTERNAL`. A validator exit of zero does not prove useful routing behavior.

## Revision and removal rules

When real evaluation exposes a false positive, false negative, stale instruction, or unnecessary resource, make the smallest supported correction. Re-test the affected trigger and its nearest exclusion. Remove obsolete references, scripts, provider assumptions, hooks, and installation instructions instead of preserving them for historical familiarity.

End the authoring handoff with the skill path, changed resources, trigger/exclusion cases, validation commands/states, assumptions, unresolved risks, and next action.
