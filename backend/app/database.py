from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

# pool_pre_ping testa a conexão antes de usar, evitando erro depois que o
# banco reinicia.
engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """Classe mãe de todos os models (tabelas) do projeto."""


def get_db() -> Iterator[Session]:
    """Abre uma sessão por requisição e garante que ela seja fechada no fim.

    Use nas rotas com Depends(get_db).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
