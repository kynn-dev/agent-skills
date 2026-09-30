# Security policy

## Supported scope

Security/privacy reports are welcome for the current `main` branch and the public skill package under `.agents/skills/`.

## Report sensitive findings privately

Do **not** paste leaked credentials, private endpoints, customer context, personal data, or other sensitive material into a public issue.

When GitHub private vulnerability reporting is enabled for this repository, use **Security → Report a vulnerability** so the report stays private.

If that option is unavailable, contact the repository owner privately through an available GitHub contact channel and provide only the minimum information needed to locate the problem:

- affected path;
- commit or branch;
- type of sensitive material;
- whether the material is currently reachable;
- remediation suggestion if known.

Do not include a secret value itself unless a secure channel is explicitly established.

## Public-package boundary

This repository is maintained as an allowlist. Public skills must not contain:

- credentials, tokens, cookies, keys, `.env` values, or private hashes;
- private project/client instructions;
- proprietary brand-direction material;
- internal service endpoints or infrastructure identifiers;
- personal data that is not required for the reusable method.

The repository validator checks known private markers, package consistency, local links, and common accidental secret patterns across public text files, but automated scanning is not a substitute for human review.

## Research boundary

Please keep testing to the repository content and infrastructure you are authorized to access. Do not attempt to access private systems, accounts, or data to demonstrate a report.
