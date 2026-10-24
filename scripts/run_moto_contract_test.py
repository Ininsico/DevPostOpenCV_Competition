"""run_moto_contract_test.py -- real boto3 calls against a fake AWS endpoint.

Milestone M6 (PLAN.md section 5.3). This is the reproducibility evidence for the cloud
path while the project stays at $0.

Starts ``moto_server`` and drives the SAME adapters the cloud uses through
    S3 upload -> SQS -> worker -> DynamoDB -> SNS -> dashboard read -> POST /approve
then asserts the resulting DynamoDB items, the published SNS message and the updated alert
status. Because the call sites are shared with ``aws_backend``, a green run means the
boto3 code path itself works -- not that a stub was called.
"""

from __future__ import annotations

import sys

MILESTONE = "M6"


def main() -> int:
    print(
        f"run_moto_contract_test.py: not implemented yet (milestone {MILESTONE}) - "
        f"see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
