from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).parent.parent
ENV_FILE_PATH = ROOT_DIR.joinpath(".env")


class LoggingConfig(BaseModel):
    file_name: str = "api_response"
    file_size: int = 1 * 1024 * 1024
    file_backup_count: int = 5


class OpenrouterConfig(BaseModel):
    api_key: str
    model: str


class APITagsConfig(BaseModel):
    webhook: str = "Webhook"
    chat_history: str = "Chat History"


class APIPrefixConfig(BaseModel):
    api: str = "/api"
    webhook: str = "/webhook"
    chat_history: str = "/chat-history"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=ENV_FILE_PATH,
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    db: DatabaseConfig
    openrouter: OpenrouterConfig
    tags: APITagsConfig = APITagsConfig()
    logging: LoggingConfig = LoggingConfig()
    prefix: APIPrefixConfig = APIPrefixConfig()


settings = Setting()
