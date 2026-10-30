from uuid import UUID
from typing import Protocol
from abc import abstractmethod

from gym_bro.domain.health.entities import BodyWeight


class BodyWeightRepository(Protocol):
    @abstractmethod
    async def add(self, profile_id: UUID, body_weight_data: BodyWeight) -> BodyWeight: ...
