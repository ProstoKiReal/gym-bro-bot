from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Index,
    Integer,
    Table,
    Uuid,
)

from gym_bro.core.infrastructure.database.models import mapper_registry


class BodyWeightModel:
    pass


body_weights = Table(
    "body_weights",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("weight", Integer, nullable=False),
    Column("date", Date, nullable=False),
)
Index("ix_body_weights_profile_date", body_weights.c.profile_id, body_weights.c.date)

mapper_registry.map_imperatively(BodyWeightModel, body_weights)
