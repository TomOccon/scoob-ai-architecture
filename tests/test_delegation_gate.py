import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "examples"))
from delegation_gate import Task, decide


def test_default_is_inline():
    assert decide(Task(estimated_tokens=2_000, briefing_cost_tokens=3_000))[0] == "inline"


def test_qa_never_shares_builder_context():
    action, reasons = decide(Task(needs_adversarial_separation=True))
    assert action == "delegate" and "adversarial" in reasons[0]


def test_each_condition_triggers_delegation():
    for kw in ({"parallelizable": True}, {"needs_specialist_depth": True},
               {"produces_durable_artifact": True}, {"estimated_tokens": 40_000},
               {"estimated_tool_calls": 12}):
        assert decide(Task(**kw))[0] == "delegate", kw
