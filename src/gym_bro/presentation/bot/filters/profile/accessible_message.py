from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message


class AccessibleMessage(Filter):
    async def __call__(self, callback: CallbackQuery) -> bool | dict[str, Message]:
        if isinstance(callback.message, Message):
            return {"msg": callback.message}
        return False
