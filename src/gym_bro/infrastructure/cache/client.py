from redis.asyncio import Redis

from gym_bro.setup.config import config


redis_conn = Redis(
    host=config.cache.HOST,
    port=config.cache.PORT,
    password=config.cache.PASSWORD.get_secret_value(),
)
