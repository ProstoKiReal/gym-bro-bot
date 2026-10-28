from sqlalchemy import BigInteger, Column, String, Table, UniqueConstraint, Uuid

from gym_bro.infrastructure.database.models.base import metadata


class ProfileModel:
    pass


profiles = Table(
    "profiles",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("first_name", String(100), nullable=False),
    Column("last_name", String(100)),
    Column("telegram_id", BigInteger, nullable=False),
    UniqueConstraint("telegram_id", name="uq_profiles_telegram_id"),
)
