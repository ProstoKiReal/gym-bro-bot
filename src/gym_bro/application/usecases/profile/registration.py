from gym_bro.domain.profile.entities import Profile
from gym_bro.domain.profile.value_objects import ProfileID
from gym_bro.application.interfaces.profile import ProfileRepository
from gym_bro.application.dtos.profile import RegisterProfileDTO
from gym_bro.application.interfaces.tx_manager import TXManager


class RegisterProfileUseCase:
    def __init__(
        self,
        profile_repository: ProfileRepository,
        tx_manager: TXManager,
    ) -> None:
        self.profile_repository = profile_repository
        self.tx_manager = tx_manager

    async def __call__(
        self,
        profile_data: RegisterProfileDTO,
    ) -> RegisterProfileDTO:
        current = await self.profile_repository.get_by_telegram_id(profile_data.telegram_id)

        async with self.tx_manager as tx:
            if current is None:
                profile = self._to_domain(profile_data)
                await self.profile_repository.add(profile)
            else:
                profile = self._to_domain(profile_data)
                await self.profile_repository.update(profile)

            await tx.commit()

            return self._to_dto(profile)

    @staticmethod
    def _to_dto(profile: Profile) -> RegisterProfileDTO:
        return RegisterProfileDTO(
            id=profile.id.value,
            first_name=profile.first_name,
            telegram_id=profile.telegram_id,
            last_name=profile.last_name,
        )

    @staticmethod
    def _to_domain(profile: RegisterProfileDTO) -> Profile:
        return Profile(
            id=ProfileID(profile.id) if profile.id is not None else ProfileID.new(),
            first_name=profile.first_name,
            last_name=profile.last_name,
            telegram_id=profile.telegram_id,
        )
