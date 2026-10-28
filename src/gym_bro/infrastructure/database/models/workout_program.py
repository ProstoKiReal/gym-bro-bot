from sqlalchemy import Column, ForeignKey, Index, String, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata


class WorkoutProgramModel:
    pass


workout_programs = Table(
    "workout_programs",
    metadata,
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
