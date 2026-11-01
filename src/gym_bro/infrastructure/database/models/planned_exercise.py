from dataclasses import dataclass, field
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
    func,
)

from gym_bro.domain.workout.value_objects import Equipment
from gym_bro.infrastructure.database.models.base import metadata
from gym_bro.infrastructure.database.models.types import (
    equipment_type,
    planned_sets_type,
)


@dataclass
class PlannedExerciseModel:
    template_id: UUID
    position: int
    exercise_id: UUID
    name: str
    equipment: Equipment
    sets: list[dict[str, int | None]] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)


planned_exercises = Table(
    "workout_template_exercises",
    metadata,
    Column("id", Uuid, primary_key=True, server_default=func.gen_random_uuid()),
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
