from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
)
from gym_bro.core.infrastructure.database.models import mapper_registry
from gym_bro.core.infrastructure.database.models.types import (
    equipment_type,
    planned_sets_type,
)


class PlannedExerciseModel:
    pass


planned_exercises = Table(
    "workout_template_exercises",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "template_id",
        Uuid,
        ForeignKey("workout_templates.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("position", Integer, nullable=False),
    Column("exercise_id", Uuid, ForeignKey("exercises.id"), nullable=False),
    Column("name", String(200), nullable=False),
    Column("equipment", equipment_type, nullable=False),
    Column("sets", planned_sets_type, nullable=False, default=list),
    CheckConstraint("position >= 0", name="ck_workout_template_exercises_position"),
)

mapper_registry.map_imperatively(PlannedExerciseModel, planned_exercises)
