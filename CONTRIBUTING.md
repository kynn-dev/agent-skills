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
.agents/skills/<skill-name>/SKILL.md
```

Use lowercase kebab-case for the directory and frontmatter name.

Minimum frontmatter:

```yaml
---
name: example-skill
description: Use when <specific trigger>; do not use for <nearby exclusion>.
---
```

Keep the main `SKILL.md` focused. Put conditional detail in `references/` only when it improves progressive disclosure. Add scripts only when deterministic execution materially improves reliability.

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

A structural PASS is necessary but not sufficient. For a new or materially changed skill, also test at least:

- one direct positive request;
- one natural-language variant;
- one near miss/excluded request;
- one blocked/missing-capability case when relevant.

Record what actually happened. Do not label an unrun activation test as successful.

## Writing style

Prefer:

- operational instructions;
- explicit ownership and side-effect boundaries;
- evidence requirements;
- stable output contracts;
- `PASS`, `FAIL`, `NOT_RUN`, and `BLOCKED_EXTERNAL` where validation state matters.

Avoid:

- generic motivational prose;
- hidden provider/runtime assumptions;
- giant context dumps;
- “always use the strongest model” rules;
- pretending static inspection proves runtime behavior;
- duplicate skills that differ only by persona wording.

## Pull requests

Keep PRs scoped. Explain:

- trigger/exclusion change;
- files/resources added or removed;
- validation performed;
- activation cases exercised;
- compatibility or privacy considerations;
- unresolved limitations.

Thank you for helping make agents more deliberate, auditable, and less wasteful.
