"""render_diagrams.py -- render docs/*.mmd to PNG with matplotlib.

Milestone M8 (PLAN.md section 5.3, section 10.4).

Draws docs/architecture.png and docs/agent_workflow.png from the same node/edge data the
Mermaid sources describe. matplotlib (a Python dependency we already have) is used on
purpose: it keeps Node and mermaid-cli off the judge's critical path while the .mmd
sources stay in the repository for GitHub's renderer.
"""

from __future__ import annotations

import sys

MILESTONE = "M8"


def main() -> int:
    print(
        f"render_diagrams.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
