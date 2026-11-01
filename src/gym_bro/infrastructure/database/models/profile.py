from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    Column,
    Integer,
    String,
    Table,
    UniqueConstraint,
    Uuid,
)

from gym_bro.domain.profile.value_objects import Gender
from gym_bro.infrastructure.database.models.base import metadata
from gym_bro.infrastructure.database.models.types import profile_gender_type


@dataclass
class ProfileModel:
    id: UUID
    first_name: str
    telegram_id: int
    last_name: str | None = None
    gender: Gender | None = None
    weight: int | None = None


profiles = Table(
    "profiles",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("first_name", String(100), nullable=False),
    Column("last_name", String(100)),
    Column("telegram_id", BigInteger, nullable=False),
    Column("gender", profile_gender_type),
    Column("weight", Integer),
    UniqueConstraint("telegram_id", name="uq_profiles_telegram_id"),
)
