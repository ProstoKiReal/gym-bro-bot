from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from gym_bro.application.interfaces.database.repositories.body_weight import (
    BodyWeightRepository,
)
from gym_bro.application.interfaces.database.repositories.profile import (
    ProfileRepository,
)
from gym_bro.infrastructure.database.repositories import (
    AlchemyBodyWeightRepository,
    AlchemyProfileRepository,
)


def profile_repository(session: AsyncSession) -> ProfileRepository:
    return AlchemyProfileRepository(session)


def body_weight_repository(session: AsyncSession) -> BodyWeightRepository:
    return AlchemyBodyWeightRepository(session)


def repositories_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(source=AlchemyProfileRepository, provides=ProfileRepository)
    provider.provide(source=AlchemyBodyWeightRepository, provides=BodyWeightRepository)
    return provider
