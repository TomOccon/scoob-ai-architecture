# AI-first delivery framework

The operating method used to deliver AI and data builds in Forward Deployed Engineering and Professional Services. Its central rule: **prove each pattern in one engagement, then package it so other teams can replicate it.**

## The loop

1. **Discover outcomes, not features.** Five questions: what winning looks like, what the user's Tuesday looks like, the one hero metric, the decision they make with least confidence, and what would make them tell someone else.
2. **Prove in one engagement.** Build the smallest version that exercises the pattern against real data and a real user. Write down what broke.
3. **Gate before shipping.** Independent QA and security review, with a persona-by-capability matrix for anything multi-persona or external-facing.
4. **Package.** Turn the proven pattern into a reusable asset: a skill, an agent definition, a template or a checklist. Include the failure modes found in step 2.
5. **Promote.** After three independent uses, move it into the shared library. Before that it stays local.
6. **Retro.** Every build ends with a structured retro whose output feeds the next build's discovery.

## What makes it AI-first
- Agents do the assembly (data wiring, scaffolding, QA passes); people own judgment (outcome definition, tradeoffs, customer relationship).
- Every agent has a brief with exact files, acceptance criteria and known traps. A vague brief produces vague work.
- Memory, not heroics, carries lessons between builds.

## Enablement
The framework was taught to a 35-person consulting organization (pod consultants, data scientists and offshore teams) as a working method: the same loop, the same gates, the same brief template.

Evidence in this repo: [delegation gate](../examples/delegation_gate.py), [ADRs](adr/).
