from collections.abc import Sequence

from gym_bro.core.domain.profile.value_objects import ProfileID
from gym_bro.core.domain.workout.aggregates import WorkoutTemplate
from gym_bro.core.domain.workout.entities import PlannedExercise
from gym_bro.core.domain.workout.value_objects import WorkoutTemplateID


class CreateWorkoutTemplate:
    def __call__(self, profile_id: ProfileID, name: str) -> WorkoutTemplate:
        raise NotImplementedError


class AddExerciseToTemplate:
    def __call__(
        self,
        template_id: WorkoutTemplateID,
        exercise: PlannedExercise,
    ) -> WorkoutTemplate:
        raise NotImplementedError


class RemoveExerciseFromTemplate:
    def __call__(
        self,
        template_id: WorkoutTemplateID,
        exercise_index: int,
    ) -> WorkoutTemplate:
        raise NotImplementedError


class ReorderTemplateExercises:
    def __call__(
        self,
        template_id: WorkoutTemplateID,
        exercise_order: Sequence[int],
    ) -> WorkoutTemplate:
        raise NotImplementedError
