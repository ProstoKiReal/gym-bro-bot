from dataclasses import dataclass
from datetime import date

from gym_bro.core.domain.health.errors import InvalidWeightError
from gym_bro.core.domain.health.value_objects import BodyWeightID
from gym_bro.core.domain.profile.value_objects import ProfileID


@dataclass
class BodyWeight:
    id: BodyWeightID
    weight: int
    date: date
    profile_id: ProfileID

    def __post_init__(self):
        if self.weight <= 0:
            raise InvalidWeightError(self.weight)

    @property
    def weight(self) -> float:
        return self.weight / 1000
