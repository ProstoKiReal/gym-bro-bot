from dataclasses import dataclass

from gym_bro.core.domain.profile.errors import InvalidNameError, InvalidTelegramIDError
from gym_bro.core.domain.profile.value_objects import ProfileID


@dataclass
class Profile:
    id: ProfileID
    first_name: str
    telegram_id: int
    last_name: str | None = None

    def __post_init__(self) -> None:
        self.first_name = self.first_name.strip()

        if not self.first_name:
            raise InvalidNameError(self.first_name)

        if self.last_name is not None:
            self.last_name = self.last_name.strip() or None

        if self.telegram_id <= 0:
            raise InvalidTelegramIDError(self.telegram_id)