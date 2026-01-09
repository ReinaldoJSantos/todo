from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = Field(..., alias="APP_NAME")
    app_env: str = Field("development", alias="APP_ENV")

    secret_key: str = Field(..., alias="SECRET_KEY")
    access_token_expire_minutes: int = Field(
        30, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
        )

    database_url: str = Field(..., alias="DATABASE_URL")

    class Config:
        env_file = ".env"
        case_sesitive = False


settings = Settings()