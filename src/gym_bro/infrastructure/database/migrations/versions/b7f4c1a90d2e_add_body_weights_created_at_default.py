"""add body_weights created_at server default

Revision ID: b7f4c1a90d2e
Revises: e863e38ac8e2
Create Date: 2026-10-30 23:24:00.000000

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "b7f4c1a90d2e"
down_revision: str | Sequence[str] | None = "e863e38ac8e2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column(
        "body_weights",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "body_weights",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=None,
        existing_nullable=False,
    )
