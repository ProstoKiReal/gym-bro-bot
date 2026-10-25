from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Index,
    Table,
    Text,
    Uuid,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from gym_bro.core.infrastructure.database.models import mapper_registry


class WorkoutModel:
    pass


workouts = Table(
    "workouts",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True),
    Column(
        "profile_id",
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "template_id", Uuid, ForeignKey("workout_templates.id", ondelete="SET NULL")
    ),
    Column("started_at", DateTime, nullable=False),
    Column("ended_at", DateTime, nullable=False),
    Column("note", Text),
    CheckConstraint("ended_at > started_at", name="ck_workouts_valid_time_range"),
)
Index("ix_workouts_profile_started_at", workouts.c.profile_id, workouts.c.started_at)

mapper_registry.map_imperatively(
    WorkoutModel,
    workouts,
    properties={
        "exercises": relationship(
            "WorkoutExerciseModel",
            order_by=lambda: (
                mapper_registry.metadata.tables["workout_exercises"].c.position
            ),
            collection_class=ordering_list("position", reorder_on_append=True),
            cascade="all, delete-orphan",
        ),
    },
)
