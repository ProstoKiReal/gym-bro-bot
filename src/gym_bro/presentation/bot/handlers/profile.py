from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, User
from dishka.integrations.aiogram import FromDishka

from gym_bro.application.dtos.profile import RegisterProfileRequestDTO
from gym_bro.application.usecases.profile import RegisterProfileUseCase
from gym_bro.domain.profile.value_objects import Gender
from gym_bro.presentation.bot.callback_data import GenderCallback
from gym_bro.presentation.bot.filters.profile import AccessibleMessage
from gym_bro.presentation.bot.filters.profile.registration import WeightFilter
from gym_bro.presentation.bot.fsms.profile.registration import RegistrationSate
from gym_bro.presentation.bot.keyboards.profile.registration import inline_choose_gender

router = Router()


@router.message(CommandStart())
async def start_registration(
    message: Message,
    state: FSMContext,
    user: User,
) -> None:
    await state.set_state(RegistrationSate.gender)
    await message.answer(
        text=f"Привет, {user.first_name}! Регистрация почти выполнена. Укажите пол и вес.",
        reply_markup=inline_choose_gender().as_markup(),
    )


@router.callback_query(
    RegistrationSate.gender,
    GenderCallback.filter(),
    AccessibleMessage(),
)
async def choose_gender(
    callback: CallbackQuery,
    callback_data: GenderCallback,
    msg: Message,
    state: FSMContext,
) -> None:
    gender = callback_data.gender
    await state.update_data(gender=gender.value)
    await state.set_state(RegistrationSate.weight)
    await msg.answer("Введите ваш вес в кг:")
    await callback.answer()


@router.callback_query()
async def stale_callback(callback: CallbackQuery) -> None:
    await callback.answer(
        "Кнопка устарела, начните заново.",
        show_alert=True,
    )


@router.message(RegistrationSate.weight, WeightFilter())
async def enter_weight(
    message: Message,
    state: FSMContext,
    user: User,
    weight: float,
    use_case: FromDishka[RegisterProfileUseCase],
) -> None:
    state_data = await state.get_data()
    weight = round(weight * 1000)

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
