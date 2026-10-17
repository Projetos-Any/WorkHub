"""Models do SQLAlchemy: cada classe aqui vira uma tabela no banco.

Todo model novo precisa herdar de app.database.Base e ser importado neste
arquivo, senão o Alembic não enxerga a tabela ao gerar migrations.
"""
