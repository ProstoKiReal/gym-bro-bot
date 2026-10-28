from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from gym_bro.application.interfaces.profile import ProfileRepository
from gym_bro.infrastructure.database.repositories import AlchemyProfileRepository



def profile_repository(session: AsyncSession) -> ProfileRepository:
    return AlchemyProfileRepository(session)

def repositories_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(source=AlchemyProfileRepository, provides=ProfileRepository)
    return provider
