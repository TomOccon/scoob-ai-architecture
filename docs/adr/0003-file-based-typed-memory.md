# ADR 0003: File-based typed memory over long context

Status: accepted

## Context
Conversation context does not survive a multi-month engagement, and compaction drops detail at the worst moments.

## Decision
Persistent memory is plain files in four types: `user`, `feedback` (rules from corrections and confirmed approaches), `project` (time-bound state, with absolute dates) and `reference` (pointers to external systems). A one-line index is loaded every session; full entries are recalled on demand. Memories that name a file, function or flag are verified against current state before they are acted on.

## Consequences
Files are diffable, reviewable and portable. Stale memories are the main risk, which is why recall is followed by verification and why contradicted memories are deleted rather than annotated.
