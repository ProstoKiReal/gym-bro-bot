from dataclasses import dataclass

from gym_bro.domain.common.value_objects import ID


@dataclass(frozen=True, slots=True)
class ProfileID(ID):
    pass
