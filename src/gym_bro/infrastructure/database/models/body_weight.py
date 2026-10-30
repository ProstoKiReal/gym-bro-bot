from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, Table, Uuid, func

from gym_bro.infrastructure.database.models.base import metadata


class BodyWeightModel:
    pass


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
Index("ix_body_weights_profile_date", body_weights.c.profile_id, body_weights.c.created_at)
