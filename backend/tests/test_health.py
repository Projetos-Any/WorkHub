from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.database import get_db
from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    # Este teste usa o banco de verdade: rode "docker compose up db" antes.
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


class BrokenSession:
    def execute(self, *args, **kwargs):
        raise OperationalError("SELECT 1", {}, Exception("sem conexão"))


def test_health_returns_503_when_database_is_down():
    # Troca a sessão real por uma que sempre falha, simulando o banco fora do ar.
    app.dependency_overrides[get_db] = lambda: BrokenSession()
    try:
        response = client.get("/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
