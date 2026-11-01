from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Integer, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata


@dataclass
class WorkoutSetModel:
    id: UUID
    workout_exercise_id: UUID
    position: int
    reps: int
    load: int | None = None
    rpe: int | None = None


workout_sets = Table(
    "workout_sets",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "workout_exercise_id",
        Uuid,
        ForeignKey("workout_exercises.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("position", Integer, nullable=False),
    Column("reps", Integer, nullable=False),
    Column("load", Integer),
    Column("rpe", Integer),
)
