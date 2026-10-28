from pydantic_settings import BaseSettings, SettingsConfigDict


class APPConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    MODE: str

    @property
    def debug(self) -> bool:
        if self.MODE == "dev":
            return True
        return False