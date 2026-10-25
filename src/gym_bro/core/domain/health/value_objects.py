from dataclasses import dataclass

from gym_bro.core.domain.common.value_objects import ID


@dataclass(frozen=True, slots=True)
class BodyWeightID(ID):
    pass
