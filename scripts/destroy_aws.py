"""destroy_aws.py -- tear the whole stack down.

Milestone M6 (PLAN.md section 5.3).

Deletes the CloudFormation stack and then the artifacts it does not own (the S3 objects
the bucket was emptied of, the log groups). A $0 project must be able to prove it can
leave no billable trace behind, so teardown ships with deployment rather than as an
afterthought.
"""

from __future__ import annotations

import sys

MILESTONE = "M6"


def main() -> int:
    print(
        f"destroy_aws.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
