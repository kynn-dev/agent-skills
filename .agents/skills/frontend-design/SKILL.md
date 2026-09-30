---
name: frontend-design
description: Use when designing, implementing, or reviewing substantive UI, interaction, layout, responsive behavior, visual hierarchy, or front-end motion; do not use for copy-only work, brand positioning without evidence, backend/data architecture, or generic visual advice detached from a real product surface.
---

# Frontend design

Design and implement production-grade interfaces that are distinctive because they are grounded in the product, the existing visual language, and the user's task — not because they accumulate decoration.

## Trigger and exclusion boundary

Use this skill when the request asks to design, implement, revise, or review:

- application or website UI;
- visual hierarchy and layout;
- interaction states and component behavior;
- responsive behavior across meaningful viewport classes;
- front-end motion or transitions;
- a visual system that must integrate with an existing repository.

Do not use it for:

- copy-only requests; use `human-copywriting`;
- brand positioning, naming, or unsupported identity invention; use `brand-aware-design` when brand evidence exists;
- backend, database, authentication, infrastructure, or data architecture;
- generic “make it look modern” advice with no target product, implementation, or evidence boundary;
- substantial architecture review where the core decision is not primarily UI.

If the request mixes design with another domain, split the work and route each bounded part to the appropriate skill.

## Non-negotiable design frame

Before writing UI code, establish five things:

1. **Purpose** — what the user needs to accomplish and what the interface must make easier.
2. **Existing identity** — inspect the target repository's components, tokens, assets, routes, content, and interaction patterns before proposing a new visual language.
3. **Confirmed constraints** — distinguish requirements supported by repository or user evidence from reversible creative decisions.
4. **Dominant direction** — choose one primary aesthetic stance and, at most, one supporting influence. Do not use a generic SaaS look as a neutral default.
5. **Differentiation anchor** — identify one visible, useful detail that makes the interface recognizable without relying on the logo.

Preserve an existing identity unless the user explicitly authorizes a change. Do not replace established typography, color tokens, logo treatment, density, imagery, or interaction conventions merely to make a screen look more novel.

If the current identity is incomplete, mark the gap and make reversible decisions rather than silently inventing brand rules.

## Design feasibility and impact

For a material visual direction, use this five-part check before committing:

- aesthetic impact;
- context fit;
- implementation feasibility;
- performance and accessibility safety;
- consistency risk.

A strong direction earns its implementation cost. A visually impressive idea that conflicts with the product, weakens accessibility, creates avoidable performance debt, or breaks a coherent existing system should be reduced or rejected.

Do not turn a heuristic score into false certainty. Explain the tradeoff that actually matters.

## Identity-aware implementation

Translate the direction into working product code, not a static mockup detached from the repository.

- Use semantic HTML and the project's established framework/component conventions.
- Prefer existing tokens, primitives, icons, and layout patterns when they satisfy the need.
- Add new design variables only when a real requirement is missing.
- Keep spacing, typography, color, elevation, radius, iconography, and motion internally coherent.
- Avoid arbitrary font swaps, default dashboard cards, trendy gradients, decorative glass panels, and borrowed competitor identities as substitutes for product-specific thinking.
- Keep implementation complexity proportional to the design ambition.
- Remove dead styles, placeholder experiments, and unused motion before completion.
- Preserve content hierarchy when localizing or when text length changes materially.

Distinctive does not mean noisy. Minimal does not mean generic.

## Responsive behavior

Responsive design is not one media query and a narrower desktop layout.

Define how the following change across widths when relevant:

- navigation;
- hierarchy;
- density;
- grid/list structure;
- controls and form layout;
- tables and dense data;
- media/imagery;
- interaction model;
- fixed/sticky elements;
- typography and line length.

Preserve the primary task on the smallest supported viewport instead of merely shrinking everything.

Verify at least:

- the smallest supported viewport;
- one intermediate width;
- the widest supported layout;
- long or localized text;
- missing/slow media where applicable;
- touch targets and keyboard navigation;
- zoom/reflow behavior when relevant.

Avoid horizontal overflow, accidental clipping, unstable layout shifts, and fixed elements that cover actionable content.

## Accessibility states

Accessibility is part of the design, not a later audit.

Cover applicable states and behaviors:

- semantic landmarks and heading structure;
- meaningful labels and accessible names;
- logical keyboard order;
- visible focus;
- sufficient contrast;
- non-color status cues;
- usable touch targets;
- loading, empty, success, error, disabled, validation, and permission states;
- reduced-motion behavior;
- meaningful alt text or intentionally empty alt text for decorative imagery.

Do not claim accessibility from visual inspection alone. Name the checks actually performed and their scope.

## Motion and substantial 3D

Use motion to communicate state, hierarchy, continuity, or feedback. Prefer a small number of meaningful interactions over constant animation.

Treat work as **substantial motion/3D** when it includes material specialist complexity such as:

- continuous render loops or coordinated timelines;
- scene graphs with camera, lighting, post-processing, physics, or many objects;
- custom WebGL/shaders/particle systems;
- complex model viewers or 3D interaction;
- authored 3D assets whose loading, memory, device support, or fallback materially affects the product.

For substantial motion or 3D, use `adaptive-agent-routing` when available to decide whether a specialist/stronger worker or reviewer is justified. Route by actual difficulty, performance risk, and blast radius — not by novelty alone.

The specialist brief should cover:

- why the effect earns its cost;
- performance/loading budget;
- device/browser constraints;
- graceful degradation;
- reduced-motion or static fallback;
- accessibility implications;
- exact acceptance checks.

Simple CSS transitions, one SVG animation, or an ordinary hover effect do not justify heavyweight specialist routing.

## Visual evidence and QA

When implementation is in scope, validate the actual rendered result rather than relying only on code inspection.

Use the strongest evidence available:

- screenshots at representative viewport sizes;
- browser inspection of the exact route/state;
- keyboard/touch interaction checks;
- responsive behavior under real content;
- before/after comparison when modifying an existing interface;
- automated browser checks when they meaningfully cover the acceptance criteria.

If the browser/runtime environment is unavailable, mark that validation `NOT_RUN` or `BLOCKED_EXTERNAL`; do not upgrade a static code review into visual approval.

## Required delivery notes

For a substantive design or implementation, provide a compact record containing:

1. **Design direction** — purpose, evidence boundary, confirmed constraints, and reversible creative decisions.
2. **System snapshot** — relevant type, color, spacing, elevation, iconography, and motion conventions.
3. **Responsive states** — which viewport classes and content stresses were covered.
4. **Accessibility states** — what was checked and what was not.
5. **Motion/3D classification** — ordinary or substantial; specialist routing if applicable.
6. **Implementation evidence** — changed surfaces and validation actually performed.
7. **Differentiation callout** — what makes the result recognizable and why it serves the product instead of acting as decoration.

Do not claim that a design is production-ready, responsive, accessible, or performant without naming the evidence that supports that claim.

## Related skills

- `brand-aware-design` — establishes visual decisions from explicit brand/product evidence.
- `human-copywriting` — owns copy and claim discipline.
- `engineering-verification` — verifies implementation claims with fresh evidence.
- `adaptive-agent-routing` — routes specialist visual/3D work by difficulty, context, and residual risk.
