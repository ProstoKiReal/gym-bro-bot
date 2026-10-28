from aiogram import Bot, Dispatcher

from gym_bro.setup.config import config
from gym_bro.presentation.bot.handlers import router
from gym_bro.setup.di.setup import create_dishka
from gym_bro.setup.di.providers import providers


async def run_bot():
    dp = Dispatcher()
    dp.include_router(router)
    create_dishka(providers=providers, dp=dp)
    bot = Bot(token=config.bot.TOKEN.get_secret_value())
    await dp.start_polling(bot)
