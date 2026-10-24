"""agent/planner.py — our planner: goal state, preconditions, utility per action.

Milestone M3 (PLAN.md §5.2).

``agent.planner = rule`` (default): each candidate action is scored by a utility function
over the current goal state and the tool preconditions, with loop detection so the same
(state, action) pair is never chosen twice.

``agent.planner = ollama``: an optional local-LLM hook that must select from the same
validated tool registry. It is **off by default, never required, and never on the critical
path** — nothing in the required path calls a paid API.
"""

from __future__ import annotations

__all__: list[str] = []
