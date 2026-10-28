from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from gym_bro.application.usecases.profile import RegisterProfileUseCase
from gym_bro.application.dtos.profile import RegisterProfileDTO

router = Router()


@router.message(CommandStart())
async def handle(
    message: Message,
    use_case: FromDishka[RegisterProfileUseCase],
) -> None:
    user = message.from_user
    if user is None:
        raise ValueError("The /start command must be sent by a Telegram user.")

    profile_data = RegisterProfileDTO(
        telegram_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    await use_case(profile_data)
    await message.answer(f"Привет, {profile_data.first_name}! Регистрация выполнена.")

