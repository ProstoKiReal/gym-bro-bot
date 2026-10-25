from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def registration(message: Message):
    await message.answer(text="Здесь должна была быть регистрайция в боте")
