# ADR 0001: Delegation gate, default inline

Status: accepted

## Context
Early versions of the system delegated to a specialist agent whenever a task touched that agent's domain. Briefing a fresh agent costs tokens and loses detail in both directions, and the orchestrator cannot watch the agent work. For small single-domain tasks the briefing cost exceeded the execution cost.

## Decision
Work runs inline by default. A task is delegated only when at least one of five conditions holds:
1. It can run in parallel with other work.
2. Specialist depth is genuinely needed.
3. Adversarial separation is required (a reviewer must not share the builder's context).
4. It produces a defined artifact that outlives the conversation.
5. Inline execution would exceed roughly 30K tokens, or about 10 tool calls of multi-asset work.

Reference implementation: [examples/delegation_gate.py](../../examples/delegation_gate.py), with tests.

## Consequences
Fewer spawned agents and less context spend. The cost is that the orchestrator must keep the five conditions honest; the tests pin them down. Independent measurement showed single agents matching multi-agent output on a majority of tasks, so the gate treats delegation as something that has to earn its place.
