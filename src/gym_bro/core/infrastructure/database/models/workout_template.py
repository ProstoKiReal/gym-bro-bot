from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    String,
    Table,
    Uuid,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from gym_bro.core.infrastructure.database.models import mapper_registry


class WorkoutTemplateModel:
    pass


workout_templates = Table(
    "workout_templates",
    mapper_registry.metadata,
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

mapper_registry.map_imperatively(
    WorkoutTemplateModel,
    workout_templates,
    properties={
        "exercises": relationship(
            "PlannedExerciseModel",
            order_by=lambda: (
                mapper_registry.metadata.tables["workout_template_exercises"].c.position
            ),
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
