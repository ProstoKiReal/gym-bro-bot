from aiogram.fsm.state import StatesGroup, State


class RegistrationSate(StatesGroup):
    gender = State()
    weight = State()
