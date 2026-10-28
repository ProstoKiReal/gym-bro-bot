from sqlalchemy.ext.asyncio import AsyncSession
from dishka import Provider, Scope

from gym_bro.infrastructure.database.tx_manager import AlchemyTXManager
from gym_bro.application.interfaces.tx_manager import TXManager


async def tx_manager_provider(session: AsyncSession) -> TXManager:
    return AlchemyTXManager(session)


def tx_manager_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(source=AlchemyTXManager, provides=TXManager)
    return provider