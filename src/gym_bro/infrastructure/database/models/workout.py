from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

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


@dataclass
class WorkoutModel:
    id: UUID
    profile_id: UUID
    started_at: datetime
    ended_at: datetime
    template_id: UUID | None = None
    note: str | None = None


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
    Column(
        "template_id", Uuid, ForeignKey("workout_templates.id", ondelete="SET NULL")
    ),
    Column("started_at", DateTime, nullable=False),
    Column("ended_at", DateTime, nullable=False),
    Column("note", Text),
    CheckConstraint("ended_at > started_at", name="ck_workouts_valid_time_range"),
)
Index("ix_workouts_profile_started_at", workouts.c.profile_id, workouts.c.started_at)
