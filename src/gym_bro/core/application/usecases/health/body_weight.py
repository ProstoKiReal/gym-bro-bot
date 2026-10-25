from datetime import date

from gym_bro.core.domain.health.entities import BodyWeight
from gym_bro.core.domain.profile.value_objects import ProfileID


class RecordBodyWeight:
    def __call__(
        self,
        profile_id: ProfileID,
        weight_grams: int,
        measured_on: date,
    ) -> BodyWeight:
        raise NotImplementedError


class GetBodyWeightHistory:
    def __call__(self, profile_id: ProfileID) -> list[BodyWeight]:
        raise NotImplementedError
