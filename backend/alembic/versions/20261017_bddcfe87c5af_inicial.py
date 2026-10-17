"""inicial

Revision ID: bddcfe87c5af
Revises:
Create Date: 2026-10-17 16:30:20.507869

"""

from collections.abc import Sequence

# Identificadores usados pelo Alembic para saber a ordem das migrations.
revision: str = "bddcfe87c5af"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
