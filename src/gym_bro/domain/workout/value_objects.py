from dataclasses import dataclass
from enum import Enum

from gym_bro.domain.common.value_objects import ID
from gym_bro.domain.workout.errors import InvalidRPEError, InvalidRepsError, InvalidWeightError


@dataclass(frozen=True, slots=True)
class SetID(ID):
    pass


@dataclass(frozen=True, slots=True)
class WorkoutID(ID):
    pass


@dataclass(frozen=True, slots=True)
class ExerciseID(ID):
    pass


@dataclass(frozen=True, slots=True)
class WorkoutExerciseID(ID):
    pass


@dataclass(frozen=True, slots=True)
class WorkoutTemplateID(ID):
    pass


@dataclass(frozen=True, slots=True)
class WorkoutProgramID(ID):
    pass


class Equipment(Enum):
    BODYWEIGHT = "bodyweight"
    DUMBBELL = "dumbbell"
    BARBELL = "barbell"
    MACHINE = "machine"
    OTHER = "other"


@dataclass(frozen=True, slots=True)
class Weight:
    weight: int

    def __post_init__(self) -> None:
        if self.weight < 0:
            raise InvalidWeightError(self.weight)


@dataclass(frozen=True, slots=True)
class Reps:
    value: int

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise InvalidRepsError(self.value)


@dataclass(frozen=True, slots=True)
class RPE:
    value: int

    def __post_init__(self) -> None:
        if not (0 <= self.value <= 10):
            raise InvalidRPEError(self.value)
