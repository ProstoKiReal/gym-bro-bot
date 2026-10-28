from dataclasses import dataclass
from uuid import UUID

from gym_bro.domain.profile.value_objects import Gender


@dataclass
class RegisterProfileRequestDTO:
    telegram_id: int
    first_name: str
    last_name: str | None
    gender: Gender
    weight: int


@dataclass
class RegisterProfileResponseDTO:
    id: UUID
    telegram_id: int
    first_name: str
    last_name: str | None
    gender: Gender | None
    weight: int | None
