# ADR 0005: Shared knowledge lake with a promotion threshold

Status: accepted

## Context
Patterns learned on one customer engagement were invisible to the rest of the team.

## Decision
Build artifacts and learnings are written to a shared knowledge store after each significant build and read before customer work starts. A pattern is promoted to the team pattern library only after it appears in three or more independent builds, and promoted entries carry no customer-identifying detail.

## Consequences
The library stays small and trusted. The promotion threshold trades speed for signal: a one-off fix stays in personal memory until it proves general.
