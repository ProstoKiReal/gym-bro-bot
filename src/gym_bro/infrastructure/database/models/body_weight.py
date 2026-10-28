from sqlalchemy import Column, Date, ForeignKey, Index, Integer, Table, Uuid

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
    Column("date", Date, nullable=False),
)
Index("ix_body_weights_profile_date", body_weights.c.profile_id, body_weights.c.date)
