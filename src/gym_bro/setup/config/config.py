from pydantic import Field
from pydantic_settings import BaseSettings

from gym_bro.setup.config.app import APPConfig
from gym_bro.setup.config.bot import BotConfig
from gym_bro.setup.config.cache import CacheConfig
from gym_bro.setup.config.db import DBConfig


class Config(BaseSettings):
    db: DBConfig = Field(default_factory=DBConfig)
    app: APPConfig = Field(default_factory=APPConfig)
    bot: BotConfig = Field(default_factory=BotConfig)
    cache: CacheConfig = Field(default_factory=CacheConfig)


config: Config = Config()
