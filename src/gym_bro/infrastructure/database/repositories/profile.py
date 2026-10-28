from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from gym_bro.application.interfaces.profile import ProfileRepository
from gym_bro.domain.profile.entities import Profile
from gym_bro.domain.profile.value_objects import ProfileID
from gym_bro.infrastructure.database.models import ProfileModel


class AlchemyProfileRepository(ProfileRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> Profile | None:
        query = select(ProfileModel).where(ProfileModel.telegram_id == telegram_id)
        model = (await self.session.execute(query)).scalar_one_or_none()
        return self._to_domain(model) if model is not None else None

    async def add(self, profile: Profile) -> None:
        new_profile = self._to_model(profile)
        self.session.add(new_profile)

    async def update(self, profile: Profile) -> None:
        query = (
            update(ProfileModel)
            .where(ProfileModel.id == profile.id.value)
            .values(first_name=profile.first_name, last_name=profile.last_name)
        )
        await self.session.execute(query)

    @staticmethod
    def _to_domain(profile: ProfileModel) -> Profile:
        return Profile(
            id=ProfileID(profile.id),
            first_name=profile.first_name,
            telegram_id=profile.telegram_id,
            last_name=profile.last_name,
        )

    @staticmethod
    def _to_model(profile: Profile) -> ProfileModel:
        return ProfileModel(
            id=profile.id.value,
            first_name=profile.first_name,
            last_name=profile.last_name,
            telegram_id=profile.telegram_id,
        )
