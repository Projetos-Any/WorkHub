from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

import app.models  # noqa: F401  (registra os models no Base.metadata)
from app.config import settings
from app.database import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# É comparando com isso que o "alembic revision --autogenerate" descobre
# o que mudou nos models.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Gera o SQL das migrations sem conectar no banco (alembic upgrade --sql)."""
    context.configure(
        url=settings.database_url.render_as_string(hide_password=False),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Conecta no banco e aplica as migrations."""
    connectable = create_engine(settings.database_url)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
