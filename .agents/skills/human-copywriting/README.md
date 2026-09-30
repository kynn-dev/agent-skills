# Human copywriting

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`human-copywriting` is a writing and editing workflow that tries to keep copy natural without sacrificing factual discipline. It is designed for landing pages, product text, emails, scripts, UX copy, case studies, headlines, and other content where the language should sound human while every material claim remains traceable.

The skill separates facts from voice, creative language, missing evidence, and genuine unknowns so an agent does not turn a plausible sentence into an unsupported promise.

## Why it exists

LLM copy often fails in two directions at once: it sounds generic and it becomes overconfident. Common symptoms include stacked adjectives, fake intimacy, invented urgency, unsupported social proof, vague authority language, and brand voice flattened into generic “professional” prose.

This skill keeps the useful parts of human writing — specificity, rhythm, personality, directness, cultural context — while putting factual claims behind an evidence boundary.

## When to use it

Use it when:

- editing existing copy while preserving meaning and voice;
- writing new copy from a brief or approved source material;
- adapting a message to a new channel, language, audience, or length;
- improving clarity, hierarchy, rhythm, specificity, or conversion;
- creating variants that must stay within the same factual boundary.

Do not use it to invent legal/medical/financial/safety advice, unsupported brand positioning, testimonials, metrics, certifications, product capabilities, or competitive claims.

## How it works

The skill starts with a small claim ledger:

- `CONFIRMED` — supported by the user or an identified source;
- `VOICE / INTENT` — what must remain true about speaker, audience, promise, and emotional register;
- `CREATIVE LANGUAGE` — framing, rhythm, metaphor, and emphasis that do not imply unsupported proof;
- `SOURCE NEEDED` — a claim that cannot safely be written as fact yet;
- `UNKNOWN` — a gap that must not be filled from convention or plausibility.

For editing, the agent identifies what must remain, makes the smallest useful intervention, then re-checks changed claims against the source.

For new copy, the agent establishes the brief, builds the claim ledger, drafts with concrete language, then runs claim, voice, clarity, and channel passes.

## Expected inputs

Useful inputs include:

- source text or a content brief;
- objective and desired action;
- audience and channel;
- language and length constraints;
- approved product/company facts;
- source material for material claims;
- tone/voice examples or non-negotiable phrases when voice preservation matters.

If an important claim is missing evidence, the agent should ask for the source or keep a visible placeholder rather than quietly inventing support.

## Expected results

A successful result should:

- sound specific to the speaker/product instead of template-generated;
- preserve confirmed facts and required qualifiers;
- preserve or intentionally change voice with that change visible;
- avoid unsupported superiority, guarantees, social proof, scarcity, metrics, or authority claims;
- use clear, concrete language appropriate to the channel;
- identify remaining source gaps or unknowns;
- keep optional creative variants distinct from approved positioning.

For a short request, the result can simply be the finished line. The workflow should not bury a one-sentence edit under a methodology report.

## Example

Suppose a product brief says a tool can reduce a workflow from six manual steps to three in a documented internal test. The skill may turn that into concise product copy, preserving the scope and qualifier. It should not silently upgrade the claim to “cuts your workload in half for every customer” or add “trusted by thousands” because those statements sound persuasive.

## Specific design choices

The skill deliberately protects against several common LLM writing habits:

- fake intimacy that assumes a relationship with the reader;
- invented urgency or scarcity;
- empty superlatives and stacked adjectives;
- “premium,” “innovative,” or “industry-leading” language without evidence;
- changing a material promise while supposedly “improving flow”;
- normalizing away useful regional or personal voice;
- turning cautious source language such as “may” or “intended to” into certainty.

## Works well with

- [`brand-aware-design`](../brand-aware-design/README.md) when copy must fit an established identity without inventing positioning;
- [`frontend-design`](../frontend-design/README.md) for landing pages, UX content, and interface hierarchy;
- [`engineering-verification`](../engineering-verification/README.md) when factual/product claims depend on implemented behavior that should be verified.

## Limitations

This skill does not perform legal, regulatory, medical, financial, or safety approval. It also cannot establish facts that were never supplied or researched.

A polished draft can still require domain review. When that review did not happen, the correct state remains `NOT_RUN` rather than “approved” or “compliant.”

## Agent contract

For exact claim classes, editing/new-copy workflows, source discipline, voice rules, and verification boundaries, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
