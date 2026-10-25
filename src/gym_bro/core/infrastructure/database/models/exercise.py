from sqlalchemy import Column, String, Table, Uuid

from gym_bro.core.infrastructure.database.models import mapper_registry
from gym_bro.core.infrastructure.database.models.types import equipment_type


class ExerciseModel:
    pass


exercises = Table(
    "exercises",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("equipment", equipment_type, nullable=False),
)

mapper_registry.map_imperatively(ExerciseModel, exercises)
