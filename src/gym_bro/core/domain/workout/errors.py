from gym_bro.core.domain.common.errors import BaseDomainError


class InvalidWeightError(BaseDomainError):
    def __init__(self, weight: object):
        super().__init__(f"Weight must be a non-negative integer number of grams; got {weight}.")


class InvalidRepsError(BaseDomainError):
    def __init__(self, reps: object):
        super().__init__(f"Repetitions must be a positive integer; got {reps}.")


class InvalidRPEError(BaseDomainError):
    def __init__(self, rpe: object):
        super().__init__(f"RPE must be an integer number of tenths between 10 and 100; got {rpe}.")


class InvalidNameError(BaseDomainError):
    def __init__(self, name: str):
        super().__init__("Name cannot be empty.")
        self.name = name


class InvalidWorkoutTimeError(BaseDomainError):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidWorkoutTemplateOwnerError(BaseDomainError):
    def __init__(self, template_id: object, profile_id: object):
        super().__init__(
            f"Workout template {template_id} does not belong to profile {profile_id}."
        )
