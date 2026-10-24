"""aws/adapters.py — one interface, three implementations.

Milestone M6 (PLAN.md §5.3).

    S3Store   put/get/presign        local dir | moto | boto3 S3
    DynamoStore  put/query/update    SQLite   | moto | boto3 DynamoDB
    Notifier  publish                outbox/  | moto | boto3 SNS
    Queue     send/receive/delete    dir      | moto | boto3 SQS

Selected by ``aws.adapter`` in config.yaml. The interface is deliberately small: it is the
contract that lets the whole pipeline run end-to-end today with no AWS account, while the
identical call sites run against real AWS once credentials exist.
"""

from __future__ import annotations

__all__: list[str] = []
