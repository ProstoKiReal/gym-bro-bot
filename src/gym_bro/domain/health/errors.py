from gym_bro.domain.common.errors import BaseDomainError


class InvalidWeightError(BaseDomainError):
    def __init__(self, weight):
        super().__init__(f"Body weight must be a positive integer number of grams; got {weight}.")
