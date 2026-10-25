from datetime import datetime

from gym_bro.core.domain.profile.value_objects import ProfileID
from gym_bro.core.domain.workout.aggregates import Workout
from gym_bro.core.domain.workout.entities import WorkoutExercise, WorkoutSet
from gym_bro.core.domain.workout.value_objects import (
    WorkoutExerciseID,
    WorkoutID,
    WorkoutTemplateID,
)


class StartWorkout:
    def __call__(
        self,
        profile_id: ProfileID,
        started_at: datetime,
        template_id: WorkoutTemplateID | None = None,
    ) -> Workout:
        raise NotImplementedError


class AddExerciseToWorkout:
    def __call__(
        self,
        workout_id: WorkoutID,
        exercise: WorkoutExercise,
    ) -> Workout:
        raise NotImplementedError


class RecordWorkoutSet:
    def __call__(
        self,
        workout_id: WorkoutID,
        exercise_id: WorkoutExerciseID,
        workout_set: WorkoutSet,
    ) -> Workout:
        raise NotImplementedError


class FinishWorkout:
    def __call__(self, workout_id: WorkoutID, ended_at: datetime) -> Workout:
        raise NotImplementedError


class AddWorkoutNote:
    def __call__(self, workout_id: WorkoutID, note: str) -> Workout:
        raise NotImplementedError
