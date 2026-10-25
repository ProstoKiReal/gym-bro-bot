from dataclasses import dataclass, field
from gym_bro.core.domain.workout.errors import InvalidNameError
from gym_bro.core.domain.workout.value_objects import (
    Equipment,
    ExerciseID,
    Reps,
    RPE,
    SetID,
    Weight,
    WorkoutExerciseID,
)


@dataclass
class Exercise:
    id: ExerciseID
    name: str
    equipment: Equipment

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise InvalidNameError(self.name)


@dataclass
class WorkoutSet:
    id: SetID
    reps: Reps
    load: Weight | None = None
    rpe: RPE | None = None


@dataclass(frozen=True, slots=True)
class PlannedSet:
    target_reps: Reps
    target_load: Weight | None = None


@dataclass
class WorkoutExercise:
    id: WorkoutExerciseID
    exercise_id: ExerciseID
    name: str
    equipment: Equipment
    sets: list[WorkoutSet]
    planned_sets: list[PlannedSet] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise InvalidNameError(self.name)

    def add_set(self, workout_set: WorkoutSet) -> None:
        self.sets.append(workout_set)


@dataclass
class PlannedExercise:
    exercise_id: ExerciseID
    name: str
    equipment: Equipment
    sets: list[PlannedSet] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise InvalidNameError(self.name)

    @property
    def sets_count(self) -> int:
        return len(self.sets)
