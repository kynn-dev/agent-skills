---
name: brand-aware-design
description: Design visual direction from explicit brand and product evidence, separating confirmed requirements from reversible creative decisions and unknowns. Use for brand-sensitive UI or visual work; exclude unsupported positioning and generic styling detached from evidence.
---

# Brand-aware design

Make visual decisions that are accountable to evidence. A brand-aware result is not a guessed palette, a fashionable style, or a familiar SaaS template; it is a clear record of what the source establishes, what the designer proposes, and what remains unknown.

## Operational contract

### Objective

Translate real brand and product evidence into a coherent visual direction without turning guesses, trends, or personal taste into brand facts. Preserve confirmed identity, make reversible creative choices explicit, and keep unknowns/conflicts visible until resolved.

### Expected inputs

Use the approved brief, brand guidelines, existing product/repository surfaces, design tokens, logo/assets, typography/color evidence, imagery/iconography, product task, responsive/accessibility constraints, and any explicit user authorization to change established identity.

### Required outputs

Return the evidence boundary, a compact `CONFIRMED`/`CREATIVE DECISION`/`UNKNOWN`/`CONFLICT` record, the proposed direction and rationale, do-not-change constraints, unresolved questions, responsive/accessibility implications, and implementation/review evidence actually inspected or executed.

### Definition of done

The design direction is done when every material identity claim is traceable to inspected evidence or labeled as a reversible proposal, conflicts are not silently arbitrated, established brand elements are preserved unless change was authorized, and any statement such as “on-brand” is scoped to the evidence that was actually reviewed.

## Trigger and exclusion boundary

Use this skill when a request asks to:

- apply or preserve a brand identity in UI, product surfaces, campaigns, or visual systems;
- review whether a design is consistent with an existing brand;
- establish a design direction from supplied brand files, repository evidence, or approved guidelines;
- adapt a known identity across responsive states, components, or channels.

Do not use it for:

- inventing brand positioning, audience, values, naming, or claims without evidence;
- generic “make it look premium/modern” work with no source or product context;
- copy-only tasks, where `human-copywriting` applies;
- substantial implementation architecture or performance analysis;
- borrowing another brand's identity because the target evidence is missing.

## Evidence classes

Maintain these classes in every material design decision:

| Class | Meaning | What to do |
| --- | --- | --- |
| CONFIRMED | Directly supported by an approved brief, existing product, public file, design token, asset, or cited guideline. | Preserve it unless the user authorizes a change; cite the source. |
| CREATIVE DECISION | A reversible choice made to fill a gap or satisfy a brief. | Label it, explain the rationale, and keep an alternative available. |
| UNKNOWN | Not established by the available evidence or contradicted by sources. | Ask, use a neutral placeholder, or defer. Never silently promote it to confirmed. |
| CONFLICT | Two sources disagree or the requested change would break a confirmed constraint. | Show the conflict and ask for resolution; do not arbitrate by taste. |

A product domain, company name, existing code, or common industry pattern is not by itself a brand specification.

## Operating workflow

1. State the evidence boundary: files, links, approved references, and existing implementation actually inspected. Do not imply that private, remote, or secret sources were checked.
2. Inventory existing identity: logo treatment, type, colors, spacing, imagery, iconography, component patterns, tone, density, motion, and responsive behavior. Record exact paths or source names.
3. Build a short evidence table with CONFIRMED, CREATIVE DECISION, UNKNOWN, and any CONFLICT.
4. Define the design problem and user task. A brand decision must still serve comprehension, action, accessibility, and maintainability.
5. Propose the smallest coherent direction. Preserve existing identity where it is sufficient; introduce new choices only where the evidence or task requires them.
6. Validate contrast, focus, keyboard behavior, content states, responsive layouts, reduced motion, and long or localized content when applicable.
7. Handoff with explicit decisions, unresolved gaps, and what must not be changed without approval.

## Avoid generic output

Do not use a trendy gradient, default dashboard cards, rounded containers, stock “premium” language, arbitrary type pairing, or a fashionable effect as a substitute for evidence. Do not call a direction editorial, luxury, playful, technical, organic, or minimal unless that description is confirmed or clearly labeled as a creative proposal.

Avoid flattening an existing identity into a neutral component library. If the product is operational, preserve useful density and task orientation; if it is editorial, preserve reading rhythm and hierarchy; if the source does not establish either, mark the choice UNKNOWN and propose a reversible test.

## Required output

Use a compact format suited to the request, but include:

- evidence boundary and source paths;
- confirmed visual/product requirements;
- creative decisions and rationale;
- unknowns, conflicts, and questions;
- do-not-change constraints;
- accessibility and responsive implications;
- implementation or review result, with checks actually run.

Never claim “on-brand” as a fact when the brand source is incomplete. Say “consistent with the inspected evidence” and name the evidence scope.

## Related skills

- `human-copywriting` owns factual, human copy when copy is in scope.
- use the project's own brand-direction skill or guidelines when one exists;
- load only the brand profile relevant to the current repository or artifact.
