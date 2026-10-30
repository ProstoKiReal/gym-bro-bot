from gym_bro.domain.profile.entities import Profile
from gym_bro.domain.health.entities import BodyWeight
from gym_bro.application.interfaces.database.repositories.profile import ProfileRepository
from gym_bro.application.interfaces.database.repositories.body_weight import BodyWeightRepository
from gym_bro.application.dtos.profile import (
    RegisterProfileRequestDTO,
    RegisterProfileResponseDTO,
)
from gym_bro.application.interfaces.database.tx_manager import TXManager
from gym_bro.domain.profile.value_objects import ProfileID


class RegisterProfileUseCase:
    def __init__(
        self,
        profile_repository: ProfileRepository,
        body_weight_repository: BodyWeightRepository,
        tx_manager: TXManager,
    ) -> None:
        self.profile_repository = profile_repository
        self.body_weight_repository = body_weight_repository
        self.tx_manager = tx_manager

    async def __call__(
        self,
        registration_data: RegisterProfileRequestDTO,
    ) -> RegisterProfileResponseDTO:
        current = await self.profile_repository.get_by_telegram_id(registration_data.telegram_id)

        async with self.tx_manager as tx:
            if current is None:
                current = self._to_profile_domain(registration_data)
                await self.profile_repository.add(current)
            else:
                is_changed_profile_data = current.update_details(
                    first_name=registration_data.first_name,
                    last_name=registration_data.last_name,
                    gender=registration_data.gender,
                )
                if is_changed_profile_data:
                    await self.profile_repository.update(current)

            weight = self._to_body_weight_domain(registration_data, current.id)

            body_weight = await self.body_weight_repository.add(current.id.value, weight)

            await tx.commit()

            return self._to_registration_dto(current, body_weight)

    @staticmethod
    def _to_registration_dto(profile: Profile, body_weight: BodyWeight) -> RegisterProfileResponseDTO:
        return RegisterProfileResponseDTO(
            id=profile.id.value,
            first_name=profile.first_name,
            telegram_id=profile.telegram_id,
            last_name=profile.last_name,
            gender=profile.gender,
            weight=body_weight.weight,
        )

    @staticmethod
    def _to_profile_domain(registration: RegisterProfileRequestDTO) -> Profile:
        return Profile(
            first_name=registration.first_name,
            last_name=registration.last_name,
            telegram_id=registration.telegram_id,
            gender=registration.gender,
        )

    @staticmethod
    def _to_body_weight_domain(
        registration: RegisterProfileRequestDTO,
        profile_id: ProfileID,
    ) -> BodyWeight:
        return BodyWeight(
            weight=registration.weight,
            profile_id=profile_id,
        )
