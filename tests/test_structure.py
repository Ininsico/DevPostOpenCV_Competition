"""The repository layout is part of the deliverable (PLAN.md section 4).

A module named in the plan but missing on disk would otherwise only surface in the middle
of a later milestone, so the layout itself is pinned here. When a milestone adds a file,
it is added to the lists below at the same time.
"""

from __future__ import annotations

import importlib

import pytest

CORE_MODULES = [
    "herdwatch.config",
    "herdwatch.video_io",
    "herdwatch.calibration",
    "herdwatch.segmentation",
    "herdwatch.tracking",
    "herdwatch.identity",
    "herdwatch.confidence",
    "herdwatch.scoring",
    "herdwatch.segment_analysis",
    "herdwatch.evidence",
    "herdwatch.cli",
]

FEATURE_MODULES = ["backline", "stride", "symmetry", "headbob"]
AGENT_MODULES = ["tools", "policy", "planner", "orchestrator", "trace"]
AWS_MODULES = [
    "models",
    "adapters",
    "local_backend",
    "aws_backend",
    "worker",
    "agent_handler",
    "api_handler",
]

PACKAGE_MODULES = (
    CORE_MODULES
    + [f"herdwatch.features.{name}" for name in FEATURE_MODULES]
    + [f"herdwatch.agent.{name}" for name in AGENT_MODULES]
    + [f"herdwatch.aws.{name}" for name in AWS_MODULES]
    + ["herdwatch.dashboard.app"]
)

SCRIPT_FILES = [
    "fetch_dataset.py",
    "make_synthetic.py",
    "build_lambda_package.py",
    "deploy_aws.py",
    "destroy_aws.py",
    "run_eval.py",
    "bench_opencv.py",
    "run_local_pipeline.py",
    "run_moto_contract_test.py",
    "render_diagrams.py",
]

# docs/ is written in M8, so the documents are not asserted here yet. Adding the
# assertion before the files exist would keep CI red for the whole build; it goes in
# with the documentation package.

ROOT_FILES = [
    "README.md",
    "PLAN.md",
    "LICENSE",
    "NOTICE",
    "pyproject.toml",
    "tasks.py",
    "Makefile",
    "tasks.ps1",
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
    ".github/workflows/ci.yml",
]


@pytest.mark.parametrize("module", PACKAGE_MODULES)
def test_package_module_exists_and_imports(module):
    importlib.import_module(module)


@pytest.mark.parametrize("name", SCRIPT_FILES)
def test_script_exists(repo_root, name):
    assert (repo_root / "scripts" / name).is_file()


@pytest.mark.parametrize("name", ROOT_FILES)
def test_root_file_exists(repo_root, name):
    assert (repo_root / name).is_file()


def test_dashboard_static_page_exists(repo_root):
    assert (repo_root / "src" / "herdwatch" / "dashboard" / "static" / "index.html").is_file()


def test_infra_exists(repo_root):
    assert (repo_root / "infra" / "template.yaml").is_file()
    assert (repo_root / "infra" / "graviton_bench.sh").is_file()


def test_generated_output_directories_are_created(cfg):
    for key in ("traces", "evidence", "outbox", "bench"):
        assert cfg.paths[key], f"paths.{key} is not configured"


def test_tooling_state_is_not_committed(repo_root):
    """Agent tooling state (.commandcode/, taste/) must never be part of the submission."""
    ignored = (repo_root / ".gitignore").read_text(encoding="utf-8")
    assert ".commandcode/" in ignored
    assert "node_modules/" in ignored
    assert "data/clips/" in ignored
    assert "artifacts/" in ignored
