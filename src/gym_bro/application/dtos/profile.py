from uuid import UUID
from dataclasses import dataclass


@dataclass
class RegisterProfileDTO:
    telegram_id: int
    first_name: str
    last_name: str | None
    id: UUID | None = None
