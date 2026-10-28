from dataclasses import dataclass, field

from gym_bro.domain.profile.errors import InvalidNameError, InvalidTelegramIDError
from gym_bro.domain.profile.value_objects import Gender, ProfileID


@dataclass
class Profile:
    first_name: str
    telegram_id: int
    id: ProfileID = field(default_factory=ProfileID.new)
    last_name: str | None = None
    gender: Gender | None = None
    weight: int | None = None

    def __post_init__(self) -> None:
        self.first_name = self.first_name.strip()

        if not self.first_name:
            raise InvalidNameError(self.first_name)

        if self.last_name is not None:
            self.last_name = self.last_name.strip() or None

        if self.telegram_id <= 0:
            raise InvalidTelegramIDError(self.telegram_id)

    def update_details(
        self,
        *,
        first_name: str,
        last_name: str | None,
        gender: Gender,
        weight: int,
    ) -> bool:
        if (
            self.first_name,
            self.last_name,
            self.gender,
            self.weight,
        ) == (first_name, last_name, gender, weight):
            return False

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.weight = weight
        return True
