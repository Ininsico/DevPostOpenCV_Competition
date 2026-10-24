"""cli.py — the ``herdwatch`` command line.

Commands (PLAN.md §4): ``analyze | batch | agent | bench | serve``.

Each command is filled in by its milestone; until then it exits with ``PENDING`` (2) so
the task runner can tell "not built yet" apart from "broken".
"""

from __future__ import annotations

import argparse
import sys

from herdwatch import __version__

#: Exit code meaning "this command exists but its milestone has not been built yet".
PENDING = 2

#: command name -> milestone that implements it.
MILESTONES = {
    "analyze": "M2",
    "batch": "M2",
    "agent": "M3",
    "serve": "M4",
    "bench": "M7",
}


def _pending(command: str) -> int:
    print(
        f"herdwatch {command}: not implemented yet (milestone {MILESTONES[command]}) — "
        f"see PLAN.md §8",
        file=sys.stderr,
    )
    return PENDING


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="herdwatch",
        description="Dairy cow lameness risk alerts from barn video (OpenCV 5 + agentic loop).",
    )
    parser.add_argument("--version", action="version", version=f"herdwatch {__version__}")
    parser.add_argument("--config", default=None, help="path to a config.yaml override")

    sub = parser.add_subparsers(dest="command", required=True)

    p_analyze = sub.add_parser("analyze", help="analyse one clip; print the score breakdown")
    p_analyze.add_argument("--clip", required=False, help="clip path or filename under data/clips/")
    p_analyze.add_argument("--cow-key", default=None, help="analyse a single tracked cow")
    p_analyze.add_argument("--json", action="store_true", help="emit the breakdown as JSON")

    sub.add_parser("batch", help="analyse every clip in data/clips/")

    p_agent = sub.add_parser("agent", help="run the agent loop over a clip")
    agent_sub = p_agent.add_subparsers(dest="agent_command", required=True)
    p_run = agent_sub.add_parser("run", help="perceive -> decide -> act, writing a JSONL trace")
    p_run.add_argument("--clip", required=True)
    p_replay = agent_sub.add_parser("replay", help="replay a trace (used for the counterfactual)")
    p_replay.add_argument("--clip", required=True)
    p_replay.add_argument(
        "--force-first-score",
        type=float,
        default=None,
        help="override the first-pass score: same clip + code, only the OpenCV-derived "
        "number differs — the causal proof that perception drove the action",
    )

    p_bench = sub.add_parser("bench", help="op-level OpenCV 5 benchmark (x86 vs arm64)")
    p_bench.add_argument("--suite", default="default", choices=["default", "all"])

    p_serve = sub.add_parser("serve", help="serve the local dashboard")
    p_serve.add_argument("--host", default=None)
    p_serve.add_argument("--port", type=int, default=None)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.config:
        # Deferred import keeps ``--help`` working without touching the filesystem.
        from herdwatch import config as config_module

        config_module._CACHE = config_module.load(args.config)

    return _pending(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
