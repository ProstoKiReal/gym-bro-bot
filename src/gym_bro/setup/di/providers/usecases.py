from dishka import Provider, Scope

from gym_bro.application.interfaces.profile import ProfileRepository
from gym_bro.application.usecases.profile import RegisterProfileUseCase
from gym_bro.application.interfaces.tx_manager import TXManager



def register_profile_use_case(profile_repository: ProfileRepository, tx_manager: TXManager) -> RegisterProfileUseCase:
    return RegisterProfileUseCase(profile_repository=profile_repository, tx_manager=tx_manager)


def use_cases_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(source=RegisterProfileUseCase)
    return provider
