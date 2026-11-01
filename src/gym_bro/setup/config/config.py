from pydantic_settings import BaseSettings

from gym_bro.setup.config.app import APPConfig
from gym_bro.setup.config.bot import BotConfig
from gym_bro.setup.config.cache import CacheConfig
from gym_bro.setup.config.db import DBConfig


class Config(BaseSettings):
    db: DBConfig = DBConfig()
    app: APPConfig = APPConfig()
    bot: BotConfig = BotConfig()
    cache: CacheConfig = CacheConfig()


config: Config = Config()
