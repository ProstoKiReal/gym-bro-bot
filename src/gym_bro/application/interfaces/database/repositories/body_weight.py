from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from gym_bro.domain.health.entities import BodyWeight


class BodyWeightRepository(Protocol):
    @abstractmethod
    async def add(self, profile_id: UUID, body_weight_data: BodyWeight) -> BodyWeight: ...
