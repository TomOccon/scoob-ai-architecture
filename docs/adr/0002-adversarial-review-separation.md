# ADR 0002: QA and security agents never review their own work

Status: accepted

## Context
In one build, the reviewing agent also wrote the fix for the defect it found, then approved its own fix. The review had no adversarial value.

## Decision
QA and security agents run in a separate context from the builder and do not author the code they review. They receive the artifact and the acceptance criteria, not the builder's reasoning. A failing review goes back to the builder as a defect list.

## Consequences
One more handoff per build. Defects found by an independent reader are not anchored on the builder's assumptions, and every gate leaves a report file that outlives the session.
