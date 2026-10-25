from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from gym_bro.core.infrastructure.database.models import mapper_registry
from gym_bro.core.infrastructure.database.models.types import (
    equipment_type,
    planned_sets_type,
)


class WorkoutExerciseModel:
    pass


workout_exercises = Table(
    "workout_exercises",
    mapper_registry.metadata,
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

mapper_registry.map_imperatively(
    WorkoutExerciseModel,
    workout_exercises,
    properties={
        "sets": relationship(
            "WorkoutSetModel",
            order_by=lambda: mapper_registry.metadata.tables["workout_sets"].c.position,
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
