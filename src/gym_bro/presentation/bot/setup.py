from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from gym_bro.infrastructure.cache.client import redis_conn
from gym_bro.presentation.bot.handlers import router
from gym_bro.presentation.bot.middlewares import RequireUserMiddleware
from gym_bro.setup.config import config
from gym_bro.setup.di.providers import providers
from gym_bro.setup.di.setup import create_dishka


async def run_bot() -> None:
    storage = RedisStorage(redis_conn)
    dp = Dispatcher(storage=storage)
    dp.message.outer_middleware(RequireUserMiddleware())
    dp.include_router(router)
    create_dishka(providers=providers, dp=dp)
    bot = Bot(token=config.bot.TOKEN.get_secret_value())
    await dp.start_polling(bot)
