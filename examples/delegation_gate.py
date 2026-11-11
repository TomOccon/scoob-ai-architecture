"""Delegation gate: decide whether a task runs inline or goes to a specialist agent.

Default is inline. Delegate when ANY condition holds. Multi-agent overhead is real,
so the gate exists to stop delegation that does not pay for its briefing cost.
"""
from dataclasses import dataclass

TOKEN_THRESHOLD = 30_000
TOOL_CALL_THRESHOLD = 10


@dataclass
class Task:
    parallelizable: bool = False        # can run alongside other work
    needs_specialist_depth: bool = False
    needs_adversarial_separation: bool = False  # reviewer must not be the builder
    produces_durable_artifact: bool = False     # e.g. a QA report that outlives the session
    estimated_tokens: int = 0
    estimated_tool_calls: int = 0
    single_domain: bool = True
    context_already_held: bool = True
    briefing_cost_tokens: int = 0


def delegation_reasons(task: Task) -> list[str]:
    reasons = []
    if task.parallelizable:
        reasons.append("parallel: runs alongside other work")
    if task.needs_specialist_depth:
        reasons.append("specialist depth needed")
    if task.needs_adversarial_separation:
        reasons.append("adversarial separation: reviewer must be a separate context")
    if task.produces_durable_artifact:
        reasons.append("produces an artifact that outlives the conversation")
    if task.estimated_tokens > TOKEN_THRESHOLD or task.estimated_tool_calls > TOOL_CALL_THRESHOLD:
        reasons.append("large enough that inline execution would bloat the context")
    return reasons


def decide(task: Task) -> tuple[str, list[str]]:
    reasons = delegation_reasons(task)
    if reasons:
        return "delegate", reasons
    cheap_inline = (
        task.single_domain
        and task.estimated_tokens < TOKEN_THRESHOLD
        and task.context_already_held
        and task.briefing_cost_tokens >= task.estimated_tokens
    )
    return "inline", ["default: single domain, small, context already held"] if cheap_inline else ["default inline"]


if __name__ == "__main__":
    print(decide(Task(needs_adversarial_separation=True)))
    print(decide(Task(estimated_tokens=4_000, briefing_cost_tokens=6_000)))
