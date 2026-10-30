from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from gym_bro.application.interfaces.database.repositories.body_weight import BodyWeightRepository
from gym_bro.domain.health.entities import BodyWeight
from gym_bro.infrastructure.database.models.body_weight import BodyWeightModel


class AlchemyBodyWeightRepository(BodyWeightRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, profile_id: UUID, body_weight_data: BodyWeight) -> BodyWeight:
        weight = self._to_model(body_weight_data, profile_id)
        self.session.add(weight)
        return body_weight_data

    @staticmethod
    def _to_model(body_weight: BodyWeight, profile_id: UUID) -> BodyWeightModel:
        return BodyWeightModel(
            id=body_weight.id.value,
            weight=body_weight.weight,
            profile_id=profile_id,
            created_at=body_weight.created_at,
        )
