from dishka import Provider, Scope

from gym_bro.application.interfaces.database.tx_manager import TXManager
from gym_bro.infrastructure.database.tx_manager import AlchemyTXManager


def tx_manager_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(source=AlchemyTXManager, provides=TXManager)
    return provider
