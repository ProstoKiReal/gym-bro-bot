from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Index,
    Table,
    Text,
    Uuid,
)

from gym_bro.infrastructure.database.models.base import metadata


class WorkoutModel:
    pass


workouts = Table(
    "workouts",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("template_id", Uuid, ForeignKey("workout_templates.id", ondelete="SET NULL")),
    Column("started_at", DateTime, nullable=False),
    Column("ended_at", DateTime, nullable=False),
    Column("note", Text),
    CheckConstraint("ended_at > started_at", name="ck_workouts_valid_time_range"),
)
Index("ix_workouts_profile_started_at", workouts.c.profile_id, workouts.c.started_at)
