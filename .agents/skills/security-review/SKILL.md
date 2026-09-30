---
name: security-review
description: Use when conducting an evidence-backed security review of an application, change, service boundary, or deployment path, including authentication, authorization, tenant isolation, secrets, input/output handling, SSRF, XSS, injection, logging, dependencies, and deployment boundaries. Separate static evidence from runtime and production evidence; never recommend bypasses.
---

# Security review

Use this skill to identify security-relevant trust boundaries, abuse paths, and control gaps without weakening the controls under review. The result is a bounded threat model and evidence-backed findings, not a generic checklist, exploit exercise, or production change.

## Operational contract

### Objective

Produce a bounded threat model and evidence-backed security findings for the authorized scope while preserving the controls being reviewed. The review should explain which assets, actors, entry points, trust boundaries, and invariants matter, then test whether the relevant controls actually protect them without using bypasses as proof.

### Expected inputs

The workflow expects the review scope, architecture or repository evidence, affected identities/roles/tenants, assets and data classes, relevant entry points, configuration/deployment boundaries, available test environments, and the user's authorization boundary for runtime checks. Unknown provider or production behavior must remain explicitly unknown until observed.

### Required outputs

Return the threat model, prioritized abuse paths, findings with severity and confidence, exact evidence class (`STATIC`, `CONTROLLED_RUNTIME`, `REMOTE_RUNTIME`, `PRODUCTION`, or `UNKNOWN`), preconditions/impact/scope, the smallest safe remediation, validation status, and unresolved evidence gaps. Never include secret values or unnecessary personal data in the report.

### Definition of done

The review is complete only when the material trust boundaries in scope have been assessed, findings are tied to concrete evidence, runtime claims do not exceed the environment actually exercised, high-impact unknowns are surfaced, and no conclusion depends on weakening authentication, authorization, tenant isolation, validation, TLS, rate limiting, or deployment controls.

## Non-negotiable invariant

> Never recommend or perform a bypass of authentication, authorization, tenant isolation, validation, encryption, rate limiting, or deployment controls to make a review easier.

An administrator token, disabled row-level security, permissive CORS, arbitrary outbound URL, logged credential, or suppressed validation is not evidence that a regular user flow is safe.

## When to use

Use for:

- a code, configuration, dependency, API, storage, database, or deployment-boundary review with security impact;
- changes involving identity, sessions, roles, tenant/object access, secrets, untrusted input, output rendering, network fetches, logging, or CI/CD;
- a request to map threats, review controls, or distinguish static findings from runtime or production results.

Do not use as permission to exploit third-party systems, access data outside the authorized scope, rotate or reveal secrets, or modify production. If the required environment or account is unavailable, record that boundary and stop the affected runtime check.

## Start with a threat model

Before reviewing individual lines, establish:

- assets: credentials, sessions, tenant data, personal data, business records, files, logs, build artifacts, and service credentials;
- actors: anonymous users, authenticated users, other tenants, privileged operators, maintainers, service accounts, dependencies, and attackers;
- entry points: HTTP routes, APIs, webhooks, jobs, queues, file uploads, imports, admin tools, scripts, and deployment pipelines;
- trust boundaries: browser to server, tenant to tenant, user to operator, service to service, application to database, application to provider, and build to deployment;
- security invariants: who may perform each action, what data each actor may access, what must never leave a boundary, and how failures must behave;
- assumptions and unknowns: label them explicitly rather than treating architecture, provider behavior, or configuration as fact.

For each high-impact flow, write the abuse path in one sentence: actor, entry point, untrusted input or capability, control that should stop it, and impact if the control fails. Prioritize by impact, exploitability, exposure, and confidence in the evidence.

## Evidence classes

Classify every conclusion as one of:

- `STATIC` — code, configuration, tests, dependency manifests, lockfiles, generated bundles, or diff evidence;
- `CONTROLLED_RUNTIME` — an authorized local, test, or sandbox flow with known identity and data scope;
- `REMOTE_RUNTIME` — an authorized staging or remote flow, with environment and identity recorded;
- `PRODUCTION` — an explicitly authorized production flow, with the exact path and identity recorded;
- `UNKNOWN` — evidence is insufficient; state what would resolve it.

Static evidence can reveal a missing check. It cannot prove production behavior, remote provider health, or that every role and tenant is isolated.

## Review workflow

### Authentication

Check the server-side identity boundary, not just the client: credentials/tokens/sessions, expiration and revocation, transport, protected entry points, server-side identity derivation, recovery/MFA/CSRF/replay when applicable, service-to-service identity, webhook signatures, and least-privilege credentials.

Do not suggest disabling a check, accepting an unsigned token, trusting a client claim, or using a privileged credential to “test” authentication. If a valid test session is unavailable, the authenticated runtime check is `NOT_RUN` or `BLOCKED_EXTERNAL`, not PASS.

### Authorization

Verify authorization at the server or policy boundary for every sensitive operation:

- function-level permission;
- object-level permission;
- property-level permission;
- role and privilege transitions;
- fail-closed defaults;
- background jobs, exports, caches, webhooks, direct object URLs, and alternate API versions.

UI hiding, route guards, disabled buttons, and client-side role checks are ergonomics, not authorization.

### Tenant and object isolation

Where a tenant/workspace model exists, derive tenant context from verified server-side identity and membership. Scope reads, writes, searches, exports, files, caches, jobs, notifications, and realtime subscriptions to the authorized tenant and object. Review alternate lookup paths, bulk operations, storage rules, restore/import flows, errors, counts, logs, backups, and generated artifacts.

Use dedicated test identities and synthetic records for cross-tenant negative checks. Never use another person’s data or an administrator path as proof.

### Secrets and sensitive data

Search for exposure in source, authorized history, configuration, logs, error payloads, client bundles, artifacts, screenshots, fixtures, and dependency metadata without printing values. Report the secret type, location, and exposure class — not the value.

### Input and output handling

Trace untrusted data from each entry point to storage, queries, commands, templates, redirects, network clients, and responses. Check schema/type/size validation, parameterization, output encoding, file upload boundaries, path traversal, error disclosure, parser differentials, open redirects, and other context-relevant injection surfaces.

Validation is not a substitute for parameterization or contextual output encoding. Escaping is not a substitute for authorization.

### SSRF and outbound requests

For user-influenced URLs, callbacks, imports, previews, webhooks, or redirects: use strict scheme/host policy, validate resolved destinations, account for redirects and private/link-local ranges, enforce timeouts/size/content/redirect limits, and prevent credentials or internal headers from crossing to untrusted destinations.

Do not “fix” SSRF by allowing every URL, disabling certificate validation, routing through a privileged proxy, or accepting arbitrary redirects.

### Logging and observability

Security events should be attributable and useful without becoming an exfiltration path. Do not log tokens, passwords, session identifiers, private keys, full personal data, or sensitive payloads. Structure user-controlled log fields and keep correlation identifiers from becoming authorization capabilities.

### Dependencies and supply chain

Inspect manifests, lockfiles, registries, build scripts, plugins, generated code, update policy, install scripts, artifact provenance, and CI permissions. A clean scanner is not proof of application authorization or runtime safety.

### Deployment boundaries

Review environment/project separation, service-account privilege, ingress/egress, CORS, CSRF, security headers, TLS, debug settings, public/server-only config, CI/CD triggers, secret scopes, migrations, storage permissions, queues, caches, workers, previews, staging, and production differences.

Do not deploy, change production policy, widen network access, disable protections, or apply a migration as part of a review unless that exact action is explicitly authorized.

## Findings format

For each finding, record:

- severity and confidence, with the reason for both;
- asset, actor, entry point, trust boundary, and abuse path;
- evidence class and exact file/symbol/configuration boundary/test/authorized runtime observation;
- preconditions, impact, affected scope, and whether exploitability is demonstrated or inferred;
- smallest safe remediation, preserving existing authorization and privacy boundaries;
- validation command or test, expected result, actual status, and remaining limits.

Use `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED_EXTERNAL` for validation status. Do not call a control effective when its required evidence was unavailable.

## Safe verification boundaries

- use synthetic data and dedicated accounts for runtime checks;
- test both allowed and denied paths without bypassing the control being reviewed;
- prefer read-only, reversible, rate-bounded probes in an authorized environment;
- stop before destructive actions, privilege changes, cross-tenant data access, exploit payloads against third parties, or production mutations;
- sanitize output and retain only the minimum evidence needed to reproduce the reasoning;
- if a required session, provider, network, permission, or deployment artifact is unavailable, classify the gap honestly.

## Red flags: reject the shortcut

- “Use an admin token to prove the regular user path.”
- “Disable RLS, authorization, TLS, validation, or rate limiting temporarily.”
- “Allow all origins or all URLs for now.”
- “Log the token or full payload so we can see what happened.”
- “The UI hides it, so authorization is covered.”
- “The static scan is clean, so production is secure.”
- “A local anonymous request proves the authenticated route.”
- “Upgrade everything” without a bounded dependency finding and regression plan.

## Reusable checklist

- [ ] Assets, actors, entry points, trust boundaries, and invariants are explicit.
- [ ] Authentication and server-side authorization were reviewed separately.
- [ ] Object, property, function, and tenant isolation were traced across alternate paths.
- [ ] Secrets and sensitive data were checked without exposing values.
- [ ] Input validation, output encoding, injection, upload, and error paths were reviewed.
- [ ] SSRF and outbound-request restrictions were reviewed where applicable.
- [ ] Logging and observability avoid sensitive data and log injection.
- [ ] Dependencies, lockfiles, build steps, and deployment boundaries were reviewed.
- [ ] Static, controlled runtime, remote, and production evidence are separated.
- [ ] Every required check is PASS, FAIL, NOT_RUN, or BLOCKED_EXTERNAL.
- [ ] No bypass, unauthorized access, production mutation, or secret exposure was recommended.
