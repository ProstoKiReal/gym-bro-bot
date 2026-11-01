from aiogram.filters.callback_data import CallbackData

from gym_bro.domain.profile.value_objects import Gender


class GenderCallback(CallbackData, prefix="gender"):
    gender: Gender
