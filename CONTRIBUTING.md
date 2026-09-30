# Contributing

Thanks for improving Agent Skills.

The repository favors small, evidence-oriented skills with clear routing boundaries over large prompt collections.

## Before opening a pull request

A contribution should answer five questions:

1. **What request should activate this skill?**
2. **What nearby requests should not activate it?**
3. **What observable outcome does it produce?**
4. **What evidence proves the workflow worked?**
5. **Why does this need a reusable skill instead of a one-off prompt?**

## Skill shape

Each skill lives under:

```text
.agents/skills/<skill-name>/
├── README.md   # human-facing explanation
└── SKILL.md    # executable agent contract
```

Optional `references/` and `scripts/` belong beside those files only when they materially improve progressive disclosure or deterministic execution.

### Human documentation: `README.md`

The README should help a human decide whether the skill is useful before reading its operational contract. Keep it explanatory rather than imperative.

Every skill README must contain:

- `## What this skill does`
- `## When to use it`
- `## How it works`
- `## Expected inputs`
- `## Expected results`
- `## Limitations`
- `## Agent contract`

It should link to `SKILL.md` and may also explain why the skill exists, show a compact example, call out important design choices, and link related skills.

### Agent documentation: `SKILL.md`

`SKILL.md` remains the operational source of truth loaded by the agent. It should define the exact trigger/exclusion boundary, common workflow, invariants, evidence requirements, stop/escalation conditions, result states, and handoff contract needed for execution.

Every public `SKILL.md` in this package also includes a compact operational summary near the top:

- `## Operational contract`
- `### Objective`
- `### Expected inputs`
- `### Required outputs`
- `### Definition of done`

Those headings are not a substitute for the detailed workflow below them. They make the skill's purpose and execution contract legible to an agent before it processes the full instructions.

Use lowercase kebab-case for the directory and frontmatter name.

Minimum frontmatter:

```yaml
---
name: example-skill
description: Use when <specific trigger>; do not use for <nearby exclusion>.
---
```

Keep `SKILL.md` focused. Put conditional detail in `references/` only when it improves progressive disclosure. Add scripts only when deterministic execution materially improves reliability.

The two files serve different readers but must not become competing sources of truth: the README explains; `SKILL.md` governs agent behavior.

## Public-safety rule

This repository is an allowlisted public package.

Do not submit:

- API keys, tokens, cookies, private keys, credentials, `.env` values, or secret hashes;
- private repository URLs, private endpoints, customer names/context, internal IPs, or personal data;
- proprietary brand-direction material;
- copied third-party prompts/skills whose license does not permit redistribution;
- generated logs or artifacts containing sensitive source text.

If in doubt, remove the private context and keep the reusable method.

## Validation

Run:

```bash
python -B tools/validate_skills.py .
```

The validator checks both the human and agent documentation shape, package/profile/version consistency, local links, and repository-wide public-safety markers.

A structural PASS is necessary but not sufficient. For a new or materially changed skill, also test at least:

- one direct positive request;
- one natural-language variant;
- one near miss/excluded request;
- one blocked/missing-capability case when relevant.

Record what actually happened. Do not label an unrun activation test as successful.

## Writing style

Prefer:

- operational instructions in `SKILL.md`;
- plain-language explanation in `README.md`;
- explicit ownership and side-effect boundaries;
- evidence requirements;
- stable output contracts;
- `PASS`, `FAIL`, `NOT_RUN`, and `BLOCKED_EXTERNAL` where validation state matters.

Avoid:

- generic motivational prose;
- duplicate human/agent documents that drift into different rules;
- hidden provider/runtime assumptions;
- giant context dumps;
- “always use the strongest model” rules;
- pretending static inspection proves runtime behavior;
- duplicate skills that differ only by persona wording.

## Pull requests

Keep PRs scoped. Explain:

- trigger/exclusion change;
- files/resources added or removed;
- human documentation changes;
- agent contract changes;
- validation performed;
- activation cases exercised;
- compatibility or privacy considerations;
- unresolved limitations.

Thank you for helping make agents more deliberate, auditable, understandable, and less wasteful.
