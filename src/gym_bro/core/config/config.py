from pydantic_settings import BaseSettings

from gym_bro.core.config.db import DBConfig


class Config(BaseSettings):
    db: DBConfig = DBConfig()

config: Config = Config()
