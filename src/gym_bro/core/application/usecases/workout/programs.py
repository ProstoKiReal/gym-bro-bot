from collections.abc import Sequence

from gym_bro.core.domain.profile.value_objects import ProfileID
from gym_bro.core.domain.workout.aggregates import WorkoutProgram, WorkoutTemplate
from gym_bro.core.domain.workout.value_objects import WorkoutProgramID, WorkoutTemplateID


class CreateWorkoutProgram:
    def __call__(self, profile_id: ProfileID, name: str) -> WorkoutProgram:
        raise NotImplementedError


class AddTemplateToProgram:
    def __call__(
        self,
        program_id: WorkoutProgramID,
        template: WorkoutTemplate,
    ) -> WorkoutProgram:
        raise NotImplementedError


class RemoveTemplateFromProgram:
    def __call__(
        self,
        program_id: WorkoutProgramID,
        template_id: WorkoutTemplateID,
    ) -> WorkoutProgram:
        raise NotImplementedError


class ReorderProgramTemplates:
    def __call__(
        self,
        program_id: WorkoutProgramID,
        template_ids: Sequence[WorkoutTemplateID],
    ) -> WorkoutProgram:
        raise NotImplementedError
