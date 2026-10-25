from dataclasses import dataclass, field
from datetime import datetime

from gym_bro.core.domain.profile.value_objects import ProfileID
from gym_bro.core.domain.workout.errors import (
    InvalidNameError,
    InvalidWorkoutTemplateOwnerError,
    InvalidWorkoutTimeError,
)
from gym_bro.core.domain.workout.entities import PlannedExercise, WorkoutExercise
from gym_bro.core.domain.workout.value_objects import (
    WorkoutID,
    WorkoutProgramID,
    WorkoutTemplateID,
)


@dataclass(slots=True)
class Workout:
    id: WorkoutID
    profile_id: ProfileID
    started_at: datetime
    ended_at: datetime
    exercises: list[WorkoutExercise] = field(default_factory=list)
    template_id: WorkoutTemplateID | None = None
    note: str | None = None

    def __post_init__(self) -> None:
        if self.ended_at <= self.started_at:
            raise InvalidWorkoutTimeError("Workout cannot end before it starts.")

    def add_exercise(self, exercise: WorkoutExercise) -> None:
        self.exercises.append(exercise)

    def finish(self) -> None:
        ended_at = datetime.utcnow()

        if ended_at < self.started_at:
            raise InvalidWorkoutTimeError("Workout cannot end before it starts.")

        self.ended_at = ended_at


@dataclass(slots=True)
class WorkoutTemplate:
    id: WorkoutTemplateID
    profile_id: ProfileID
    name: str
    exercises: list[PlannedExercise] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if not self.name:
            raise InvalidNameError(self.name)

    def add_exercise(self, exercise: PlannedExercise) -> None:
        self.exercises.append(exercise)


@dataclass(slots=True)
class WorkoutProgram:
    id: WorkoutProgramID
    profile_id: ProfileID
    name: str
    templates: list[WorkoutTemplate] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = self.name.strip()

        if not self.name:
            raise InvalidNameError(self.name)

        if any(template.profile_id != self.profile_id for template in self.templates):
            raise InvalidWorkoutTemplateOwnerError(
                next(
                    template.id
                    for template in self.templates
                    if template.profile_id != self.profile_id
                ),
                self.profile_id,
            )

    def add_template(self, template: WorkoutTemplate) -> None:
        if template.profile_id != self.profile_id:
            raise InvalidWorkoutTemplateOwnerError(template.id, self.profile_id)
        self.templates.append(template)
