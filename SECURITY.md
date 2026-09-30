# Security policy

## Supported scope

Security/privacy reports are welcome for the current `main` branch and the public skill package under `.agents/skills/`.

## Please do not publish sensitive details in an issue

If you discover a leaked credential, private endpoint, customer context, personal data, or another sensitive artifact, do **not** paste the secret/value into a public issue.

Instead, contact the repository owner privately through an available GitHub contact channel and provide the minimum information needed to locate the problem:

- affected path;
- commit or branch;
- type of sensitive material;
- whether the material is currently reachable;
- remediation suggestion if known.

Do not include the secret value itself unless a secure channel is explicitly established.

## Public-package boundary

This repository is maintained as an allowlist. Public skills must not contain:

- credentials, tokens, cookies, keys, `.env` values, or private hashes;
- private project/client instructions;
- proprietary brand-direction material;
- internal service endpoints or infrastructure identifiers;
- personal data that is not required for the reusable method.

The repository validator checks a small set of known private markers, but automated scanning is not a substitute for human review.

## Research boundary

Please keep testing to the repository content and infrastructure you are authorized to access. Do not attempt to access private systems, accounts, or data to demonstrate a report.
