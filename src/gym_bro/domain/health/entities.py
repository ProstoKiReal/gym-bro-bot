from dataclasses import dataclass
from datetime import date

from gym_bro.domain.health.errors import InvalidWeightError
from gym_bro.domain.health.value_objects import BodyWeightID
from gym_bro.domain.profile.value_objects import ProfileID


@dataclass
class BodyWeight:
    id: BodyWeightID
    weight_grams: int
    date: date
    profile_id: ProfileID

    def __post_init__(self):
        if (
            isinstance(self.weight_grams, bool)
            or not isinstance(self.weight_grams, int)
            or self.weight_grams <= 0
        ):
            raise InvalidWeightError(self.weight_grams)
