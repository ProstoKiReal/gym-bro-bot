from pydantic_settings import  BaseSettings, SettingsConfigDict
from pydantic import  SecretStr


class BotConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BOT_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    TOKEN: SecretStr
