"""Shared pytest fixtures.

Deliberately tiny. The pipeline writes into ``data/`` and ``artifacts/`` (both
git-ignored), so tests that need real paths use them through ``config.ensure_dirs()``
instead of inventing a parallel fixture tree that could drift from production layout.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def cfg():
    """The loaded config, with the data/ and artifacts/ trees created."""
    from herdwatch import config

    config.ensure_dirs()
    return config.config()
