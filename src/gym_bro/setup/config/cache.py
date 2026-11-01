from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class CacheConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CACHE_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    HOST: str
    PORT: int
    PASSWORD: SecretStr
