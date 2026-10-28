from gym_bro.domain.profile.entities import Profile
from gym_bro.application.interfaces.profile import ProfileRepository
from gym_bro.application.dtos.profile import (
    RegisterProfileRequestDTO,
    RegisterProfileResponseDTO,
)
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
        profile_data: RegisterProfileRequestDTO,
    ) -> RegisterProfileResponseDTO:
        current = await self.profile_repository.get_by_telegram_id(profile_data.telegram_id)

        async with self.tx_manager as tx:
            if current is None:
                current = self._to_domain(profile_data)
                await self.profile_repository.add(current)
            else:
                is_changed_profile = current.update_details(
                    first_name=profile_data.first_name,
                    last_name=profile_data.last_name,
                    gender=profile_data.gender,
                    weight=profile_data.weight,
                )
                if is_changed_profile:
                    await self.profile_repository.update(current)

            await tx.commit()

            return self._to_dto(current)

    @staticmethod
    def _to_dto(profile: Profile) -> RegisterProfileResponseDTO:
        return RegisterProfileResponseDTO(
            id=profile.id.value,
            first_name=profile.first_name,
            telegram_id=profile.telegram_id,
            last_name=profile.last_name,
            gender=profile.gender,
            weight=profile.weight,
        )

    @staticmethod
    def _to_domain(profile: RegisterProfileRequestDTO) -> Profile:
        return Profile(
            first_name=profile.first_name,
            last_name=profile.last_name,
            telegram_id=profile.telegram_id,
            gender=profile.gender,
            weight=profile.weight,
        )
