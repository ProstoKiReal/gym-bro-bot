from typing import Protocol
from abc import abstractmethod

from gym_bro.domain.profile.entities import Profile


class ProfileRepository(Protocol):
    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: int) -> Profile | None: ...

    @abstractmethod
    async def add(self, profile: Profile) -> None: ...

    @abstractmethod
    async def update(self, profile: Profile) -> None: ...
