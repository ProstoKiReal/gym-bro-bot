"""Add gender and weight to profiles.

Revision ID: c9d4a08b15ef
Revises: faeeec5d628e
Create Date: 2026-10-28
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c9d4a08b15ef"
down_revision: Union[str, Sequence[str], None] = "faeeec5d628e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "profiles",
        sa.Column(
            "gender",
            sa.Enum(
                "man",
                "woman",
                name="profile_gender",
                native_enum=False,
                create_constraint=False,
            ),
            nullable=True,
        ),
    )
    op.add_column("profiles", sa.Column("weight", sa.Integer(), nullable=True))
    op.create_check_constraint(
        "profile_gender",
        "profiles",
        "gender IN ('man', 'woman')",
    )


def downgrade() -> None:
    op.drop_constraint("profile_gender", "profiles", type_="check")
    op.drop_column("profiles", "weight")
    op.drop_column("profiles", "gender")
