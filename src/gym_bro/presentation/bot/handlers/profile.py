from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from dishka.integrations.aiogram import FromDishka

from gym_bro.application.usecases.profile import RegisterProfileUseCase
from gym_bro.application.dtos.profile import RegisterProfileRequestDTO
from gym_bro.domain.profile.value_objects import Gender
from gym_bro.presentation.bot.fsms.profile.registration import RegistrationSate
from gym_bro.presentation.bot.keyboards.profile.registration import inline_choose_gender
from gym_bro.presentation.bot.filters.profile.registration import WeightFilter


router = Router()


@router.message(CommandStart())
async def start_registration(
    message: Message,
    state: FSMContext,
) -> None:
    user = message.from_user

    await state.set_state(RegistrationSate.gender)
    await message.answer(
        text=f"Привет, {user.first_name}! Регистрация почти выполнена. Укажите пол и вес.",
        reply_markup=inline_choose_gender().as_markup(),
    )

@router.callback_query(
    RegistrationSate.gender,
    F.data.in_({"gender:man", "gender:woman"}),
)
async def choose_gender(callback: CallbackQuery, state: FSMContext):
    gender = Gender(callback.data.removeprefix("gender:"))
    await state.update_data(gender=gender.value)
    await state.set_state(RegistrationSate.weight)
    await callback.message.answer("Введите ваш вес в кг:")
    await callback.answer()


@router.message(RegistrationSate.weight, WeightFilter())
async def enter_weight(
    message: Message,
    state: FSMContext,
    weight: float,
    use_case: FromDishka[RegisterProfileUseCase],
):
    state_data = await state.get_data()
    user = message.from_user
    weight = int(round(weight * 1000))

    profile_data = RegisterProfileRequestDTO(
        telegram_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=Gender(state_data["gender"]),
        weight=weight,
    )
    await use_case(profile_data)
    await state.clear()
    await message.answer("Регистрация завершена!")