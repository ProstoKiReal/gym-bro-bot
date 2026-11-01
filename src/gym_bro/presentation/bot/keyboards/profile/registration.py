from aiogram.utils.keyboard import InlineKeyboardBuilder

from gym_bro.domain.profile.value_objects import Gender
from gym_bro.presentation.bot.callback_data import GenderCallback


def inline_choose_gender() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🙍‍♂️",
        callback_data=GenderCallback(gender=Gender.MAN).pack(),
    )
    builder.button(
        text="🙍‍♀️",
        callback_data=GenderCallback(gender=Gender.WOMAN).pack(),
    )
    return builder
