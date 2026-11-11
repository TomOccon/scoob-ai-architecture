# ADR 0004: Token discipline is a correctness rule

Status: accepted

## Context
Every tool result is re-billed with the full accumulated context. Unfiltered output, whole-file reads and large attachments caused repeated compaction loops and lost state.

## Decision
Hard rules for every session: filter verbose commands (count or list first, then targeted context), batch independent calls, never re-read a file after editing it (edits fail loudly), never load attachments whole (page them or delegate to a reader agent), and consult memory before re-deriving anything. Guards inject reminders at fixed context thresholds.

## Consequences
Sessions stay inside the context budget, and long builds finish without a compaction loop. The rules are enforced by hooks, because rules that depend on remembering them do not hold.
