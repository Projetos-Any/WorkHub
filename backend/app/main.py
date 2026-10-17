from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import health

app = FastAPI(title="WorkHub API", version="0.1.0")

# Sem isso o navegador bloqueia as chamadas do front (porta 5173) para a
# API (porta 8000), porque são "origens" diferentes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
