from aiogram.fsm.state import State, StatesGroup


class RegistrationSate(StatesGroup):
    gender = State()
    weight = State()
