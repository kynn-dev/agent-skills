# Security review

> **Human documentation.** The executable agent contract lives in [`SKILL.md`](./SKILL.md).

## What this skill does

`security-review` is an evidence-backed review workflow for application and deployment boundaries with security impact. It starts from assets, actors, entry points, trust boundaries, and invariants, then traces concrete abuse paths through authentication, authorization, tenant isolation, secrets, untrusted input, outbound requests, logging, dependencies, and deployment configuration.

The skill is designed to review controls without weakening them. A bypass used to make a test easier is not evidence that the original control is safe.

## Why it exists

Generic security checklists can produce lots of output without answering the question that matters: who can do what, through which boundary, and what evidence shows the control actually stops the abuse path?

This skill makes the review explicit and bounded. It also separates static evidence from controlled runtime, remote runtime, production observations, and unknowns so a code inspection is not accidentally presented as proof of deployed behavior.

## When to use it

Use it when reviewing:

- authentication or session behavior;
- server-side authorization and object/property permissions;
- tenant/workspace isolation;
- secret handling and sensitive-data exposure;
- user-controlled input/output and injection surfaces;
- uploads, redirects, SSRF, callbacks, imports, or webhooks;
- logging/observability with sensitive data;
- dependencies, build steps, CI/CD, and deployment boundaries.

It is not permission to exploit third-party systems, access another user's data, disable controls, or modify production without explicit authorization.

## How it works

1. Define assets, actors, entry points, trust boundaries, and security invariants.
2. Write concrete abuse paths for high-impact flows.
3. Classify available evidence as `STATIC`, `CONTROLLED_RUNTIME`, `REMOTE_RUNTIME`, `PRODUCTION`, or `UNKNOWN`.
4. Trace authentication and authorization separately.
5. Follow tenant/object scope across alternate paths such as exports, storage, jobs, caches, and direct URLs.
6. Inspect secret exposure and untrusted-data flows without printing sensitive values.
7. Review outbound-network, logging, supply-chain, and deployment boundaries where relevant.
8. Record findings with severity, confidence, evidence, preconditions, impact, remediation, and validation status.

## Expected inputs

Useful inputs include:

- the application/change/deployment surface being reviewed;
- relevant source/configuration/tests/lockfiles;
- known identities, roles, tenants, and trust boundaries;
- authorized runtime environments and synthetic test identities when available;
- explicit limits on production or external-system access.

## Expected results

A successful review produces a bounded threat model and findings that each identify:

- asset, actor, entry point, and trust boundary;
- the abuse path and control expected to stop it;
- severity and confidence with rationale;
- evidence class and exact evidence location;
- whether exploitability was demonstrated or inferred;
- smallest safe remediation;
- validation status and remaining limits.

A clean scanner or passing static review is not, by itself, a declaration that the system is secure.

## Example

Suppose a multi-tenant API accepts an object ID from the browser. The review should not stop at “the UI only shows the user's objects.” It should trace how the server derives identity and tenant context, whether the object query is scoped to that tenant, whether bulk/export/storage paths use the same boundary, and whether a negative test with synthetic identities demonstrates denial across tenants.

## Specific design choices

The workflow deliberately rejects shortcuts such as:

- using an administrator token to prove an ordinary-user path;
- disabling RLS, authorization, TLS, validation, or rate limits;
- widening CORS or outbound URL policy “temporarily”;
- logging tokens or full sensitive payloads for convenience;
- treating a hidden UI control as server authorization;
- treating a clean dependency scanner as proof of application-level security.

## Works well with

- [`engineering-verification`](../engineering-verification/README.md) for scoped positive and negative checks;
- [`debugging`](../debugging/README.md) when a security-relevant failure first needs root-cause isolation;
- [`orchestrated-delivery`](../orchestrated-delivery/README.md) when remediation is implemented and independently reviewed;
- [`adaptive-agent-routing`](../adaptive-agent-routing/README.md) for escalating security-sensitive nodes and review strength proportionally.

## Limitations

A security review is only as complete as its evidence and scope. Missing production configuration, unavailable authenticated sessions, unknown provider behavior, or untested roles remain explicit unknowns.

The skill is not a substitute for organizational security programs, penetration testing under a defined authorization, or domain-specific compliance/legal review.

## Agent contract

For the exact threat-model fields, evidence classes, review domains, safe runtime boundaries, findings format, and red-flag shortcuts, read [`SKILL.md`](./SKILL.md). That file is the operational source of truth for agents.
