from sqlalchemy import Column, ForeignKey, Index, String, Table, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from gym_bro.core.infrastructure.database.models import mapper_registry


class WorkoutProgramModel:
    pass


workout_programs = Table(
    "workout_programs",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("name", String(200), nullable=False),
)
Index("ix_workout_programs_profile_id", workout_programs.c.profile_id)

mapper_registry.map_imperatively(
    WorkoutProgramModel,
    workout_programs,
    properties={
        "templates": relationship(
            "WorkoutTemplateModel",
            order_by=lambda: (
                mapper_registry.metadata.tables["workout_templates"].c.program_position
            ),
            collection_class=ordering_list("program_position", reorder_on_append=True),
        ),
    },
)
