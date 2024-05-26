from pydantic_settings import BaseSettings, SettingsConfigDict

from helloasso_api_wrapper import HelloAssoAPIWrapper


class Dotenv(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.test",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    API_BASE: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    ORGANIZATION_SLUG: str


dotenv = Dotenv()

hello_asso = HelloAssoAPIWrapper(
    api_base=dotenv.API_BASE,
    client_id=dotenv.CLIENT_ID,
    client_secret=dotenv.CLIENT_SECRET,
    timeout=60,
)


organization_slug = dotenv.ORGANIZATION_SLUG
