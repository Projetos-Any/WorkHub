from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    """Configurações lidas das variáveis de ambiente (ou do arquivo .env).

    O nome de cada campo é o nome da variável, sem diferenciar maiúsculas:
    postgres_user lê POSTGRES_USER.
    """

    # O .env fica na raiz do repositório. Quando a API roda pelo Docker, as
    # variáveis já chegam pelo docker-compose e esse arquivo é ignorado.
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    # Sem valor padrão de propósito: se faltar no .env, a API nem sobe.
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    # Endereços do front que podem chamar a API, separados por vírgula.
    cors_origins: str = "http://localhost:5173"

    @property
    def database_url(self) -> URL:
        # URL.create cuida de caracteres especiais na senha.
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
