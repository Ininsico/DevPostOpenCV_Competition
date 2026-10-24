"""The CLI surface: every documented command exists, and unbuilt ones say so clearly.

``PENDING`` (2) is the contract between the commands and ``tasks.py``: it means "this
command exists but its milestone has not been built yet", which is distinguishable from a
real failure. A command that silently succeeds before it is implemented would be the more
dangerous outcome.
"""

from __future__ import annotations

import pytest

from herdwatch.cli import MILESTONES, PENDING, build_parser, main


def test_help_exits_zero_and_lists_the_documented_commands(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])
    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    for command in ("analyze", "batch", "agent", "bench", "serve"):
        assert command in out


def test_version_exits_zero(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])
    assert excinfo.value.code == 0
    assert "herdwatch" in capsys.readouterr().out


def test_no_command_is_an_error():
    with pytest.raises(SystemExit) as excinfo:
        main([])
    assert excinfo.value.code != 0


@pytest.mark.parametrize(
    "argv",
    [
        ["analyze", "--clip", "L (1).mp4"],
        ["batch"],
        ["serve"],
        ["bench"],
        ["agent", "run", "--clip", "L (1).mp4"],
    ],
)
def test_unbuilt_commands_report_pending_and_explain_themselves(argv, capsys):
    assert main(argv) == PENDING
    err = capsys.readouterr().err
    assert "not implemented yet" in err
    # The message must name the milestone, so the reader knows where to look.
    assert "M" in err


def test_every_command_has_a_milestone_entry():
    parser = build_parser()
    subparsers = [
        action for action in parser._actions if hasattr(action, "choices") and action.choices
    ]
    commands = set(subparsers[-1].choices) if subparsers else set()
    assert commands == set(MILESTONES)


def test_agent_replay_accepts_the_counterfactual_override():
    args = build_parser().parse_args(
        ["agent", "replay", "--clip", "L (1).mp4", "--force-first-score", "0.42"]
    )
    assert args.force_first_score == 0.42
    assert args.agent_command == "replay"
