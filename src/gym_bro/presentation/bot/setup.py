from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from gym_bro.setup.config import config
from gym_bro.presentation.bot.handlers import router
from gym_bro.setup.di.setup import create_dishka
from gym_bro.setup.di.providers import providers
from gym_bro.infrastructure.cache.client import redis_conn


async def run_bot():
    storage = RedisStorage(redis_conn)
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    create_dishka(providers=providers, dp=dp)
    bot = Bot(token=config.bot.TOKEN.get_secret_value())
    await dp.start_polling(bot)
