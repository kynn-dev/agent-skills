# Routing calibration

Use this reference after enough routed nodes exist to evaluate whether the current routing policy is saving cost without increasing defects or rework.

## Do not calibrate from anecdotes

Do not hardcode new thresholds from one task, one repository, or a handful of successful routes. Collect a meaningful sample first.

The routing system is successful when it uses weaker/cheaper workers where appropriate while preserving or improving correctness, review quality, and wall-clock efficiency.

## Per-node telemetry

Record, when available:

- node id;
- task class;
- router difficulty/risk/blast-radius/reversibility outputs;
- router worker recommendation and confidence;
- captain final worker choice;
- whether the captain overrode the route;
- context scope and budget class;
- selected specialist role;
- worker model/tier and effort;
- worker latency;
- worker result state;
- deterministic checks and result states;
- review class selected;
- reviewer model/tier and effort;
- review verdict/findings;
- number of repair cycles;
- escalation count;
- token/cost metrics when observable;
- whether the node ultimately integrated successfully.

Do not log secrets or full prompts merely for telemetry.

## Aggregate metrics

Track at least:

- route count;
- route acceptance rate;
- captain override rate;
- overrides by task class;
- worker count by tier;
- reviewer count by tier;
- deterministic-only node count;
- escalation rate;
- first-pass success rate;
- review finding rate;
- rework rate;
- average repair cycles;
- context-budget distribution;
- context-budget override rate;
- wall-clock by class when measurable;
- cost/token distribution when measurable.

## Under-routing signals

A route may be too weak when a class consistently shows repeated worker misunderstandings despite adequate packets, multiple repair cycles, strong-reviewer findings that basic deterministic checks cannot catch, frequent captain escalation, repeated context expansion, or architecture/domain errors rather than mechanical mistakes.

Improve the task descriptor/context policy first. Escalate worker strength only when the problem is genuinely capability-related.

## Over-routing signals

A route may be too strong when a class consistently shows near-zero reviewer findings, simple deterministic work performed by expensive workers, high model effort on reversible isolated edits, reviewer packets much larger than the actual diff/evidence required, or strong-model outcomes indistinguishable from lighter-worker outcomes for the same class.

Reduce worker/reviewer tier gradually and keep deterministic validation constant while measuring the effect.

## Context-bloat signals

Context may be too broad when workers mention unrelated repository details, output becomes less focused as packet size increases, stable architecture material is copied to every node, subagents receive the full parent goal despite owning one local edit, or review latency/cost rises without better findings.

Move stable background into concise summaries and select only the files/interfaces that constrain the node.

## Suggested A/B calibration

When safe and inexpensive, compare similar bounded tasks across routes rather than re-running the exact same mutable task. Keep packet contracts and deterministic checks stable, then compare first-pass success, rework, review findings, latency, and cost.

Do not A/B test production mutations, destructive operations, security boundaries, or irreversible migrations simply to measure routing economics.

## Structured-router calibration

For a cheap structured router such as Jev, track call count, decision latency/cost, confidence distributions, captain override rate by question, outcomes after accepted routes, false-low and false-high recommendations, context-scope disagreements, and review-class disagreements.

A low router cost does not justify bad decisions. The value comes from reducing unnecessary strong-model/context use while maintaining outcome quality.

## Policy changes

When a calibration finding is strong enough to change routing behavior:

1. state the observed pattern;
2. identify the affected task classes;
3. make the smallest policy adjustment;
4. keep safety boundaries unchanged;
5. evaluate the next sample;
6. revert or adjust if rework/findings worsen materially.

Keep capability-tier semantics stable even when concrete model names change.
