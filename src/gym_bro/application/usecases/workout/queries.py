from datetime import datetime

from gym_bro.domain.profile.value_objects import ProfileID
from gym_bro.domain.workout.aggregates import Workout
from gym_bro.domain.workout.entities import PlannedSet, WorkoutExercise
from gym_bro.domain.workout.value_objects import ExerciseID


class GetWorkoutHistory:
    def __call__(
        self,
        profile_id: ProfileID,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
    ) -> list[Workout]:
        raise NotImplementedError


class GetPreviousExercisePerformance:
    def __call__(
        self,
        profile_id: ProfileID,
        exercise_id: ExerciseID,
        before: datetime,
    ) -> WorkoutExercise | None:
        raise NotImplementedError


class GetActiveWorkout:
    def __call__(self, profile_id: ProfileID) -> Workout | None:
        raise NotImplementedError


class GetProgressionSuggestion:
    def __call__(
        self,
        profile_id: ProfileID,
        exercise_id: ExerciseID,
    ) -> PlannedSet | None:
        raise NotImplementedError
