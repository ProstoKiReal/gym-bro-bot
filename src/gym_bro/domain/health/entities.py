from dataclasses import dataclass, field
from datetime import datetime

from gym_bro.domain.health.errors import InvalidWeightError
from gym_bro.domain.health.value_objects import BodyWeightID
from gym_bro.domain.profile.value_objects import ProfileID


@dataclass
class BodyWeight:
    weight: int
    profile_id: ProfileID
    id: BodyWeightID = field(default_factory=BodyWeightID.new)
    created_at: datetime = field(default_factory=datetime.utcnow)


    def __post_init__(self):
        if self.weight <= 0:
            raise InvalidWeightError(self.weight)
