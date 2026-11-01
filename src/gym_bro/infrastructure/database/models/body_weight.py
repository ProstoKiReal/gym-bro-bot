from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, Table, Uuid, func

from gym_bro.infrastructure.database.models.base import metadata


@dataclass
class BodyWeightModel:
    id: UUID
    profile_id: UUID
    weight: int
    created_at: datetime


body_weights = Table(
    "body_weights",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("weight", Integer, nullable=False),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
)
Index(
    "ix_body_weights_profile_date", body_weights.c.profile_id, body_weights.c.created_at
)
