# Brand-aware design

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`brand-aware-design` helps an agent make visual decisions from explicit brand and product evidence instead of guessing a personality from a logo, company name, industry stereotype, or fashionable design trend.

It separates four kinds of information:

- `CONFIRMED` — supported by an approved brief, existing product, asset, token, or guideline;
- `CREATIVE DECISION` — a reversible proposal made to fill a gap;
- `UNKNOWN` — something the available evidence does not establish;
- `CONFLICT` — sources disagree or a requested change would violate a confirmed constraint.

The goal is not to eliminate creativity. It is to make creativity accountable and reversible when the evidence does not support calling it “the brand.”

## Why it exists

Design agents often infer too much from too little. A dark logo becomes “luxury.” A healthcare product becomes “calm blue.” A startup becomes “rounded gradient SaaS.” Those choices may be visually competent while still inventing positioning the user never approved.

This skill creates an evidence boundary before visual work begins, so a designer can be expressive without quietly converting taste into brand fact.

## When to use it

Use it when:

- applying an established identity to a new UI, campaign, or channel;
- reviewing whether a design is consistent with existing brand evidence;
- building visual direction from supplied brand files, design tokens, product surfaces, or approved guidelines;
- adapting an identity across components, viewport states, or media;
- deciding which visual choices must be preserved and which may be explored.

Do not use it to invent audience, values, naming, market position, or promises without evidence, or to copy another brand because the target identity is incomplete.

## How it works

1. State exactly which sources were inspected.
2. Inventory the existing identity: logo treatment, type, color, spacing, imagery, iconography, components, tone, density, motion, and responsive behavior.
3. Classify important observations as `CONFIRMED`, `CREATIVE DECISION`, `UNKNOWN`, or `CONFLICT`.
4. Define the product/user task so brand consistency does not come at the expense of usability.
5. Propose the smallest coherent direction, preserving established identity where it already works.
6. Introduce new choices only where the brief or product need creates a real gap.
7. Validate responsive/accessibility implications and hand off unresolved conflicts explicitly.

## Expected inputs

Useful inputs include:

- approved logos, guidelines, tokens, or brand assets;
- existing product/screens/components;
- explicit user/client brief decisions;
- product purpose and target surface;
- examples of what must be preserved or intentionally changed;
- known conflicts between old and new sources.

A domain, company name, or competitor reference is not enough evidence by itself to define the target brand.

## Expected results

A successful result should make it clear:

- what is genuinely confirmed by the inspected evidence;
- which new visual choices are creative proposals rather than brand facts;
- what remains unknown;
- where sources conflict;
- what must not change without approval;
- how responsive/accessibility/product constraints affect the visual direction;
- why the proposed direction serves the product instead of merely following a trend.

The phrase “on-brand” should only be used when the evidence boundary is known. Otherwise the more accurate claim is “consistent with the inspected evidence.”

## Example

Suppose a product has a documented color palette, logo clear-space rules, dense operational screens, and no approved typography guidance. The skill would preserve the palette/logo/density as confirmed, mark typography as unknown, and propose a reversible type choice with rationale. It would not announce that the brand is “minimal luxury” simply because one of the colors is black.

## Specific design choices

The workflow deliberately resists:

- trendy gradients used as default identity;
- arbitrary font pairing;
- “premium,” “editorial,” “playful,” or “technical” labels without evidence;
- generic dashboard components that erase an existing product character;
- using a competitor as the missing brand specification;
- silently resolving source conflicts by personal taste.

## Works well with

- [`frontend-design`](../frontend-design/README.md) to turn the evidence-aware direction into real product UI;
- [`human-copywriting`](../human-copywriting/README.md) when tone or claims are also in scope;
- project-specific brand-direction skills when those exist and are authorized.

## Limitations

The skill cannot recover a complete identity from incomplete evidence. When the source is thin, some decisions must remain proposals or unknowns.

It also does not replace product design fundamentals: a visually faithful result can still be unusable, inaccessible, or inappropriate for the task if those concerns are ignored.

## Agent contract

For exact evidence classes, operating workflow, generic-output guardrails, required handoff fields, and related-skill boundaries, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
