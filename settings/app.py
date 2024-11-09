from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from utilities.base_path import get_env_path


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(get_env_path() / "defaults.env", get_env_path() / ".env")
    )
    environment: Annotated[str, Field(alias="env")]
