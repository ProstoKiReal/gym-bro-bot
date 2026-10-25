from aiogram import Bot, Dispatcher

from gym_bro.bot.config import config
from gym_bro.bot.handlers import router


async def run_bot():
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=config.bot.TOKEN.get_secret_value(), dispatcher=dp)
    await dp.start_polling(bot)
