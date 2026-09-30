# OpenAI + Jev example mapping

This file is an example capability mapping, not a hard dependency of the skill. Keep the routing vocabulary stable and update concrete model names when the available stack changes.

A practical current mapping can look like this:

| Capability tier | Example mapping |
| --- | --- |
| `deterministic_tool` | Script, test, query, parser, validator |
| `light_worker` | GPT-6 Luna at low/medium effort |
| `general_worker` | GPT-6 Luna at medium/high effort |
| `captain_worker` | GPT-6 Luna at high/max effort with broad curated context |
| `strong_worker_low` | GPT-6.1 Sol Low |
| `strong_worker_medium` | GPT-6.1 Sol Medium |
| `strong_worker_high` | GPT-6.1 Sol High |
| `strong_worker_extreme` | GPT-6.1 Sol XHigh/Max only when justified |
| `strong_reviewer_low` | GPT-6.1 Sol Low over a compact evidence bundle |
| `strong_reviewer_medium/high` | GPT-6.1 Sol Medium/High for unusually difficult residual risk |

A structured decision model such as Jev can sit below the captain and answer closed-set routing questions cheaply. The captain remains the semantic authority and may override every route.

Recommended split:

```text
User goal
   ↓
Broad-context captain
   ↓
DAG decomposition
   ↓
Structured router (e.g. Jev)
   ↓
route recommendation
   ↓
Captain accept / override
   ↓
minimal context packet
   ↓
worker
   ↓
deterministic validation
   ↓
review routing
   ↓
independent reviewer only when justified
   ↓
Captain integration
```

Do not send secrets, full repository state, or the full parent conversation to the structured router. Prefer bounded questions such as task class, difficulty, risk, blast radius, context scope, worker tier, and reviewer tier.
