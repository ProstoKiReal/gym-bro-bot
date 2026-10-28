from sqlalchemy import Column, ForeignKey, Integer, String, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata
from gym_bro.infrastructure.database.models.types import (
    equipment_type,
    planned_sets_type,
)


class WorkoutExerciseModel:
    pass


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
