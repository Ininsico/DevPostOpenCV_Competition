"""The cloud path — real, deployable, and runnable with no account at all.

PLAN.md §5.3. Three adapters behind one interface, selected by ``aws.adapter``:

    local   filesystem + SQLite + outbox/   (default: no account, no spend)
    moto    same code against a moto_server endpoint
    aws     the same code against real boto3

Because ``local``, ``moto`` and ``aws`` share one interface, the contract test that runs
against ``moto_server`` exercises the real boto3 call path, and adding credentials makes
the stack live with one command.
"""

from __future__ import annotations

__all__ = ["adapters", "local_backend", "models"]
