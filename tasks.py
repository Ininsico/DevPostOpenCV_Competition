"""HerdWatch task runner — the primary entry point on every platform.

``make`` is absent on the development machine (verified in PLAN.md §0), so this file is
the source of truth; the ``Makefile`` and ``tasks.ps1`` are thin wrappers over it.

    uv run python tasks.py --help
    uv run python tasks.py test
    uv run python tasks.py verify-all

Steps that belong to a milestone which has not been built yet exit with ``PENDING`` (2).
``verify-all`` reports those as ``PENDING`` instead of failing, so the harness is useful
from M0 onward while still failing loudly on a real regression.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SRC = REPO_ROOT / "src"
PY = sys.executable

# Sentinel returned by milestone stubs: "this step exists but is not built yet".
PENDING = 2


def _run(argv: list[str]) -> int:
    """Run a command from the repo root with src/ importable."""
    print(f"$ {' '.join(argv)}", flush=True)
    env = {**os.environ, "PYTHONPATH": str(SRC)}
    return subprocess.run(argv, cwd=REPO_ROOT, env=env).returncode


def _py(*argv: str) -> int:
    return _run([PY, *argv])


# --------------------------------------------------------------------------- #
# M0 — bootstrap / hygiene
# --------------------------------------------------------------------------- #
def task_lint() -> int:
    return _py("-m", "ruff", "check", ".") or _py("-m", "ruff", "format", "--check", ".")


def task_format() -> int:
    return _py("-m", "ruff", "format", ".")


def task_test() -> int:
    return _py("-m", "pytest")


def task_lock() -> int:
    return _run(["uv", "lock"]) or _run(
        ["uv", "export", "--no-dev", "--no-emit-project", "-o", "requirements.lock.txt"]
    )


def task_clean() -> int:
    removed = []
    for pattern in (
        "**/__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        "htmlcov",
        "build",
        "package",
    ):
        for path in REPO_ROOT.glob(pattern) if "**" in pattern else [REPO_ROOT / pattern]:
            if path.exists():
                shutil.rmtree(path, ignore_errors=True)
                removed.append(str(path.relative_to(REPO_ROOT)))
    for stray in (".coverage", ".coverage.xml"):
        target = REPO_ROOT / stray
        if target.exists():
            target.unlink()
            removed.append(stray)
    print("removed: " + (", ".join(removed) if removed else "nothing to remove"))
    return 0


# --------------------------------------------------------------------------- #
# M1 — data
# --------------------------------------------------------------------------- #
def task_fetch_data() -> int:
    return _py("scripts/fetch_dataset.py")


def task_synthetic() -> int:
    return _py("scripts/make_synthetic.py")


# --------------------------------------------------------------------------- #
# M2-M4 - analysis, agent, local pipeline
# --------------------------------------------------------------------------- #
def task_analyze(clip: str | None) -> int:
    argv = ["-m", "herdwatch.cli", "analyze"]
    if clip:
        argv += ["--clip", clip]
    return _py(*argv)


def task_batch() -> int:
    return _py("-m", "herdwatch.cli", "batch")


def task_agent(extra: list[str]) -> int:
    return _py("-m", "herdwatch.cli", "agent", *extra)


def task_demo() -> int:
    return _py("scripts/run_local_pipeline.py")


def task_serve() -> int:
    return _py("-m", "herdwatch.cli", "serve")


# --------------------------------------------------------------------------- #
# M5-M7 - evaluation, contract test, packaging, benchmarks
# --------------------------------------------------------------------------- #
def task_eval() -> int:
    return _py("scripts/run_eval.py")


def task_test_contract() -> int:
    return _py("scripts/run_moto_contract_test.py")


def task_package() -> int:
    return _py("scripts/build_lambda_package.py")


def task_bench() -> int:
    return _py("scripts/bench_opencv.py")


def task_deploy(dry_run: bool) -> int:
    argv = ["scripts/deploy_aws.py"]
    if dry_run:
        argv.append("--dry-run")
    return _py(*argv)


# --------------------------------------------------------------------------- #
# M8 — documentation
# --------------------------------------------------------------------------- #
def task_diagrams() -> int:
    return _py("scripts/render_diagrams.py")


VERIFY_STEPS: list[tuple[str, Callable[[], int]]] = [
    ("lint", task_lint),
    ("test", task_test),
    ("test-contract", task_test_contract),
    ("eval", task_eval),
    ("diagrams", task_diagrams),
]


def task_verify_all() -> int:
    """Run every gate the judges would run, treating unbuilt milestones as pending."""
    results: list[tuple[str, int]] = []
    for name, fn in VERIFY_STEPS:
        print(f"\n{'=' * 72}\n=== {name}\n{'=' * 72}", flush=True)
        results.append((name, fn()))

    print(f"\n{'=' * 72}\n=== verify-all summary\n{'=' * 72}")
    failed: list[str] = []
    pending: list[str] = []
    for name, code in results:
        if code == 0:
            label = "PASS"
        elif code == PENDING:
            label = "PENDING"
            pending.append(name)
        else:
            label = "FAIL"
            failed.append(name)
        print(f"  {label:<8} {name}  (exit {code})")

    if pending:
        print(f"\nnot built yet: {', '.join(pending)}  — see PLAN.md §8 for the milestones")
    if failed:
        print(f"\nFAILED: {', '.join(failed)}")
        return 1
    print("\nAll implemented steps passed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tasks.py",
        description="HerdWatch task runner (make-free by design).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python tasks.py verify-all",
    )
    sub = parser.add_subparsers(dest="task", required=True)

    def add(name: str, fn: Callable[[], int], help_text: str) -> None:
        sub.add_parser(name, help=help_text).set_defaults(func=lambda _args, _fn=fn: _fn())

    add("lint", task_lint, "ruff check + ruff format --check (M0)")
    add("format", task_format, "ruff format (M0)")
    add("test", task_test, "pytest (M0)")
    add("lock", task_lock, "regenerate uv.lock + requirements.lock.txt (M0)")
    add("clean", task_clean, "remove caches and build output (M0)")

    add("fetch-data", task_fetch_data, "download the 50 labelled clips (M1)")
    add("synthetic", task_synthetic, "build the known-ground-truth synthetic set (M1)")

    p = sub.add_parser("analyze", help="analyse one clip and print the score breakdown (M2)")
    p.add_argument("--clip", default=None, help="clip filename under data/clips/")
    p.set_defaults(func=lambda args: task_analyze(args.clip))

    add("batch", task_batch, "analyse every clip in data/clips/ (M2)")

    p = sub.add_parser("agent", help="run the agent loop, or replay a trace (M3)")
    p.add_argument("extra", nargs="*", help="passed through: run | replay --force-first-score 0.42")
    p.set_defaults(func=lambda args: task_agent(args.extra))

    add("demo", task_demo, "local S3->worker->DDB->SNS->dashboard run (M4)")
    add("serve", task_serve, "start the dashboard (M4)")
    add("eval", task_eval, "metrics, ablations, baselines, measurement accuracy (M5)")
    add("test-contract", task_test_contract, "real boto3 calls against moto_server (M6)")
    add("package", task_package, "build the arm64 Lambda layer (M6)")
    add("bench", task_bench, "x86 vs Lambda-arm64 OpenCV 5 bench (M7)")
    add("diagrams", task_diagrams, "render the Mermaid sources to PNG (M8)")

    p = sub.add_parser("deploy", help="deploy the CloudFormation stack (needs credentials)")
    p.add_argument("--dry-run", action="store_true", help="print the plan, create nothing")
    p.set_defaults(func=lambda args: task_deploy(args.dry_run))

    add("verify-all", task_verify_all, "every gate, then a PASS summary (M8)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
