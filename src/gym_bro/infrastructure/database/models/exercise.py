from sqlalchemy import Column, String, Table, Uuid

from gym_bro.infrastructure.database.models.base import metadata
from gym_bro.infrastructure.database.models.types import equipment_type


class ExerciseModel:
    pass


exercises = Table(
    "exercises",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("equipment", equipment_type, nullable=False),
)
