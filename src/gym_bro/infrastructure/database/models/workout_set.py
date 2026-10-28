from sqlalchemy import Column, ForeignKey, Integer, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata


class WorkoutSetModel:
    pass


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
