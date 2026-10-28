from typing import Protocol

from gym_bro.domain.profile.entities import Profile


class ProfileRepository(Protocol):
    async def get_by_telegram_id(self, telegram_id: int) -> Profile | None: ...

    async def add(self, profile: Profile) -> None: ...

    async def update(self, profile: Profile) -> None: ...
