from dataclasses import dataclass
from enum import Enum

from gym_bro.domain.common.value_objects import ID


class Gender(Enum):
    MAN = "man"
    WOMAN = "woman"


@dataclass(frozen=True, slots=True)
class ProfileID(ID):
    pass
