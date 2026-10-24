"""config.py — load ``config.yaml`` and expose it as dotted attributes.

PLAN.md §6: every threshold lives in ``src/herdwatch/config.yaml``, never hard-coded.
This module is the only place that reads it, so ``HERDWATCH_CONFIG`` can point a run at
a different frozen config (useful for the ablations and the threshold sweep).

    >>> from herdwatch import config
    >>> config.config().score.escalate_threshold
    0.6
    >>> config.ensure_dirs()
    [...]
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"
ENV_CONFIG_PATH = "HERDWATCH_CONFIG"


class Section(dict):
    """A read-only dict with recursive attribute access."""

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(f"no such config key: {name!r}") from exc

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("config is read-only; edit config.yaml instead")


def _wrap(value: Any) -> Any:
    if isinstance(value, dict):
        return Section({key: _wrap(item) for key, item in value.items()})
    if isinstance(value, list):
        return [_wrap(item) for item in value]
    return value


def load(path: str | Path | None = None) -> Section:
    """Read a config file and return it as a :class:`Section`.

    Resolution order: explicit ``path``, then ``$HERDWATCH_CONFIG``, then the packaged
    ``config.yaml``.
    """
    resolved = Path(path or os.environ.get(ENV_CONFIG_PATH) or DEFAULT_CONFIG_PATH)
    with resolved.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    section = _wrap(raw)
    section["_source"] = str(resolved)
    return section


_CACHE: Section | None = None


def config(reload: bool = False) -> Section:
    """The process-wide config singleton."""
    global _CACHE
    if _CACHE is None or reload:
        _CACHE = load()
    return _CACHE


def repo_path(*parts: str) -> Path:
    """An absolute path inside the repository."""
    return REPO_ROOT.joinpath(*parts)


def ensure_dirs(cfg: Section | None = None) -> list[Path]:
    """Create every directory named under ``paths`` and return them.

    ``data/`` and ``artifacts/`` are git-ignored, so a fresh clone has neither until
    something runs. Called by the CLI entry points and by the tests.
    """
    cfg = cfg or config()
    created: list[Path] = []
    for relative in cfg.paths.values():
        directory = repo_path(str(relative))
        directory.mkdir(parents=True, exist_ok=True)
        created.append(directory)
    return created


__all__ = [
    "DEFAULT_CONFIG_PATH",
    "ENV_CONFIG_PATH",
    "REPO_ROOT",
    "Section",
    "config",
    "ensure_dirs",
    "load",
    "repo_path",
]
