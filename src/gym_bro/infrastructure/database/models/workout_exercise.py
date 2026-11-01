from dataclasses import dataclass, field
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Uuid

from gym_bro.domain.workout.value_objects import Equipment
from gym_bro.infrastructure.database.models.base import metadata
from gym_bro.infrastructure.database.models.types import (
    equipment_type,
    planned_sets_type,
)


@dataclass
class WorkoutExerciseModel:
    id: UUID
    workout_id: UUID
    exercise_id: UUID
    position: int
    name: str
    equipment: Equipment
    planned_sets: list[dict[str, int | None]] = field(default_factory=list)


workout_exercises = Table(
    "workout_exercises",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "workout_id",
        Uuid,
        ForeignKey("workouts.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("exercise_id", Uuid, ForeignKey("exercises.id"), nullable=False),
    Column("position", Integer, nullable=False),
    Column("name", String(200), nullable=False),
    Column("equipment", equipment_type, nullable=False),
    Column("planned_sets", planned_sets_type, nullable=False, default=list),
)
