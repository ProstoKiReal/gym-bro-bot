from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    HOST: str
    PORT: int
    USER: str
    PASSWORD: SecretStr
    NAME: str

    @property
    def url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.USER}:{self.PASSWORD.get_secret_value()}"
            f"@{self.HOST}:{self.PORT}/{self.NAME}"
        )
