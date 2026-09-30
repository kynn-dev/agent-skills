# Frontend design

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`frontend-design` is a product-grounded UI workflow for designing, implementing, or reviewing real interface surfaces. It treats visual quality as the combination of product purpose, existing identity, hierarchy, responsive behavior, accessibility, interaction states, implementation quality, and rendered evidence.

It is not a “make it modern” prompt. The skill tries to produce interfaces that are distinctive because they belong to the product, not because they collect trendy effects.

## Why it exists

Agents can generate attractive-looking UI quickly, but they also tend to converge on the same defaults: generic cards, arbitrary gradients, oversized radii, random font swaps, decorative glass panels, and desktop-first layouts that collapse badly on smaller screens.

This skill makes the agent inspect the existing product before inventing a direction and requires visual/interaction validation when implementation is in scope.

## When to use it

Use it for substantive work involving:

- application or website UI;
- layout and visual hierarchy;
- component behavior and interaction states;
- responsive design;
- front-end motion or transitions;
- visual systems that must integrate with an existing repository;
- review of an implemented product surface.

Do not use it for copy-only work, unsupported brand positioning, backend/data architecture, or generic visual advice detached from an actual surface.

## How it works

1. Establish the user task and what the interface must make easier.
2. Inspect the existing components, tokens, assets, routes, content, and interaction conventions.
3. Separate confirmed constraints from reversible creative decisions.
4. Choose one dominant design direction and a useful differentiation anchor.
5. Check aesthetic impact, context fit, feasibility, performance/accessibility safety, and consistency risk.
6. Implement using the existing product system where it is sufficient.
7. Define responsive behavior instead of merely shrinking desktop.
8. Cover accessibility and application states as part of the design.
9. Classify ordinary versus substantial motion/3D and route specialist work when justified.
10. Validate the rendered result at representative states/viewports when runtime access exists.

## Expected inputs

The workflow benefits from:

- a concrete product surface or repository;
- the user task and desired behavior;
- existing components, design tokens, assets, and brand evidence;
- target viewport/device/browser constraints;
- content, localization, and state requirements;
- performance or motion constraints when relevant.

When evidence is missing, the skill favors reversible design decisions over silently inventing a brand system.

## Expected results

A substantive result should include:

- a clear design direction tied to purpose and inspected evidence;
- a snapshot of the relevant visual system;
- implementation consistent with repository conventions;
- defined responsive behavior across meaningful viewport classes;
- applicable loading/empty/error/disabled/validation/permission states;
- accessibility considerations such as semantics, focus, contrast, touch targets, and reduced motion;
- visual/runtime evidence for claims that depend on rendering;
- explicit notes about what was not tested.

The result should also identify the differentiation anchor: the useful visual or interaction choice that gives the surface identity without relying on gratuitous decoration.

## Example

Imagine redesigning a dense inventory page. The skill would first inspect the product's existing typography, spacing, controls, tables, and navigation. Instead of replacing everything with a generic card grid, it might preserve operational density, improve hierarchy and filtering, define a mobile interaction model, ensure keyboard focus and long localized labels work, then capture representative rendered states to verify the result.

## Specific design choices

This skill makes a few distinctions explicit:

- preserving an existing identity is the default unless change is authorized;
- “distinctive” does not mean noisy;
- “minimal” does not mean generic;
- responsive design changes hierarchy and interaction, not just width;
- accessibility is designed into states rather than appended later;
- motion should communicate state/continuity/feedback rather than exist constantly;
- simple CSS motion does not justify heavyweight 3D/specialist routing;
- visual claims require rendered evidence when that evidence is available.

## Works well with

- [`brand-aware-design`](../brand-aware-design/README.md) for evidence-grounded identity decisions;
- [`human-copywriting`](../human-copywriting/README.md) for content and claim discipline;
- [`engineering-verification`](../engineering-verification/README.md) for implementation evidence;
- [`adaptive-agent-routing`](../adaptive-agent-routing/README.md) when substantial motion, graphics, or 3D merits specialist routing.

## Limitations

The skill cannot infer a complete brand system from a company name or a single screenshot, and static code inspection cannot prove that a rendered interface is visually correct, responsive, accessible, or performant.

When browser/runtime evidence is unavailable, those claims remain `NOT_RUN` or `BLOCKED_EXTERNAL` rather than being upgraded from code inspection.

## Agent contract

For exact trigger boundaries, design frame, responsive/accessibility requirements, motion/3D classification, visual-QA rules, and delivery notes, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
