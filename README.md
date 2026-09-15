# Scoob — Multi-Agent AI Operating System

> An autonomous AI operating system I built to run my own Forward Deployed Engineering work.

This isn't a chatbot or a productivity wrapper. It's an **operational intelligence layer**
designed to run continuously across multiple active customer accounts — monitoring for
signals, executing work, and surfacing what matters before it becomes a crisis.

---

## The Problem It Solves

An FDE managing 8–12 enterprise accounts simultaneously has a fundamental signal problem:

- 40+ emails/day across customer threads
- Slack/Teams messages in multiple channels
- Gong call summaries to synthesize
- Commitments made on calls that need follow-up
- Data pipeline issues that surface silently
- Account health changes that happen between weekly calls

The instinct is to build better dashboards. The real answer is a system that
**watches everything and tells you what needs your attention.**

That's what this is.

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│              SCOOB AGENT LAYER                   │
├─────────────────────────────────────────────────┤
│  40 Specialist Agents                            │
│  ┌──────────────┐  ┌──────────────┐             │
│  │ QA Agent     │  │ Security     │             │
│  │ Data Eng     │  │ Workflow     │             │
│  │ UX Research  │  │ ETL Builder  │             │
│  │ Beast Mode   │  │ CE Architect │             │
│  │ ... (36 more)│  │              │             │
│  └──────────────┘  └──────────────┘             │
├─────────────────────────────────────────────────┤
│  Orchestration Layer (Claude Code)               │
│  · Delegation gate (5-point decision tree)       │
│  · Context resolution before prompting           │
│  · Effort-level routing per task                 │
│  · Phase summary capsules for in-progress builds │
├─────────────────────────────────────────────────┤
│  Memory System (175+ entries, 4 types)           │
│  · user: how to work with Tom                    │
│  · feedback: rules from corrections + wins       │
│  · project: active work, deadlines, state        │
│  · reference: where things live                  │
├─────────────────────────────────────────────────┤
│  MCP Tool Layer (200+ tools)                     │
│  Domo platform · GitHub · Slack · Teams          │
│  Snowflake · Salesforce · Linear · Compass       │
├─────────────────────────────────────────────────┤
│  Compass Knowledge Lake (shared with PS team)    │
│  · Per-account intelligence                      │
│  · Cross-FDE pattern library                     │
│  · Build learnings, wiring decisions             │
│  · Stakeholder maps                              │
└─────────────────────────────────────────────────┘
```

---

## Key Design Decisions

### 1. Memory over context

Most AI systems rely on the current conversation window. That fails at 4 months.
Scoob uses a **file-based semantic memory system** with four typed categories:

- `user` — who Tom is, how he works, what he knows
- `feedback` — rules extracted from every correction and confirmed approach
- `project` — time-sensitive active work, deadlines, state (absolute dates, not relative)
- `reference` — pointers to where things live in external systems

New memories are written during every session. Old memories are validated against
current state before being acted on. The result: the system gets smarter every session
instead of starting from scratch.

### 2. Specialist agents, not a monolith

A single generalist agent handling QA, security review, data engineering, and UX research
simultaneously is suboptimal across all four domains. Scoob uses **40 specialist agents**
with distinct personas, tools, and evaluation criteria.

The delegation gate determines when to spawn one vs. stay inline:
1. Can it run in parallel with other work?
2. Does it need adversarial separation (QA must not be the builder)?
3. Is specialist domain depth genuinely needed?
4. Does it produce a defined file artifact that outlives the conversation?
5. Will execution exceed ~30K tokens?

If none of these are true, Scoob executes inline. Multi-agent overhead is real —
single agents match multi-agent output 64% of the time.

### 3. Shared knowledge lake

Every build produces artifacts — discovery, UX research, retro, learnings — that
are valuable across the entire team, not just within one session. Scoob automatically:

- Writes to the shared **Compass knowledge lake** after every significant build
- Promotes patterns from 3+ customer builds to the team pattern library
- Drains a queue of pending Compass writes at session start
- Reads Compass before starting any customer work (not just personal memory)

The result: patterns I develop on one customer engagement benefit every FDE
on the next one.

### 4. Continuous monitoring (not polling)

Scoob monitors multiple active customer accounts on a 15-minute cadence:
- New emails in relevant threads
- Teams messages in customer channels
- SharePoint document changes
- Gong call summaries

This is implemented via scheduled cron jobs in the agent layer, not manual checks.
The agent surfaces signals — it doesn't ask me to go look.

### 5. Cost routing

Every prompt is classified before execution:

```
COST_ROUTER: HAIKU  → lean response, minimal tools
COST_ROUTER: SONNET → default depth
COST_ROUTER: OPUS   → upgrade signal to Tom

THINKING: extended  → reason through tradeoffs before committing
THINKING: none      → direct response

EFFORT: high → full tool depth, spawn agents when warranted
EFFORT: lean → one-sentence answer where possible
```

This prevents Claude from treating every query as a multi-tool research project
when the answer is "use pandas `.groupby()`."

---

## What It Does in Practice

**On a typical Monday morning:**
- Reads the previous Friday's session snapshot
- Checks the Compass queue for unsynced artifacts
- Surfaces any monitoring alerts from the weekend
- Loads context for the day's first customer

**During a customer build (e.g., 4-hour session):**
- Phase 1: Discovery → drafts discovery.md with depth-check validation
- Phase 2: UX research → two specialist agents run in parallel (faithful + bold poles)
- Phase 3: Scaffold + compose → view agents run in parallel, one per surface
- Phase 4: QA + Security → adversarial agents with no access to each other's context
- Phase 5: Publish → automated GitHub push, version bump, Compass artifact write

**After a build:**
- Retro agent reads timing logs, audit reports, phase artifacts
- Extracts LEARNINGS.md additions
- Flags patterns for team library promotion
- Coach agent reviews retros across builds, proposes specific prompt improvements

---

## Numbers

| Metric | Value |
|--------|-------|
| Persistent memories | 175+ |
| Specialist agents | 40 |
| MCP tools available | 200+ |
| Customer builds managed | 35+ |
| Industries served | 10+ |
| Team knowledge lake entries | Shared across entire PS org |

---

## Why This Matters for FDE / Solutions Leadership

A traditional FDE is a bottleneck: one person, one customer, one build at a time.
Scoob changes the leverage ratio. The same person can:

- Monitor 8+ active accounts simultaneously
- Run QA and security reviews in parallel instead of sequentially
- Surface cross-account patterns in real time
- Contribute to the team's institutional knowledge automatically

The goal was never to replace FDE judgment — it was to make one FDE's judgment
operate at the scale of a small team.

---

## Related Projects

- [forward-deployed-operations-platform](https://github.com/Concon8991/forward-deployed-operations-platform) — one of the systems Scoob manages
- [ai-support-intelligence](https://github.com/Concon8991/ai-support-intelligence) — LLM pipeline built using Scoob's data engineering patterns
- [customer-data-engineering](https://github.com/Concon8991/customer-data-engineering) — production failure modes Scoob helps avoid

---

## Technologies

`Claude Code` · `MCP` · `Python` · `TypeScript` · `cron scheduling` ·
`file-based semantic memory` · `multi-agent orchestration` · `Domo` ·
`GitHub` · `Slack` · `Microsoft Teams` · `SharePoint` · `Snowflake` ·
`Salesforce` · `Linear` · `Compass knowledge lake`
