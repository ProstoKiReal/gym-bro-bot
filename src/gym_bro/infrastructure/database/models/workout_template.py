from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Index, Integer, String, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata


@dataclass
class WorkoutTemplateModel:
    id: UUID
    profile_id: UUID
    name: str
    program_id: UUID | None = None
    program_position: int | None = None


workout_templates = Table(
    "workout_templates",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("program_id", Uuid, ForeignKey("workout_programs.id", ondelete="SET NULL")),
    Column("program_position", Integer),
    Column("name", String(200), nullable=False),
)
Index("ix_workout_templates_profile_id", workout_templates.c.profile_id)
Index(
    "ix_workout_templates_program_position",
    workout_templates.c.program_id,
    workout_templates.c.program_position,
)
