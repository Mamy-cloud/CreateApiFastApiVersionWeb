import os
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from app.database.database_web import Base
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Lecture du fichier alembic.ini
config = context.config
fileConfig(config.config_file_name)

# URL synchrone pour Alembic
DATABASE_URL_SYNC = os.getenv("DATABASE_URL_SYNC_ALEMBIC")
if not DATABASE_URL_SYNC:
    raise RuntimeError("DATABASE_URL_SYNC_ALEMBIC is not set in .env")

# Métadonnées des modèles SQLAlchemy
target_metadata = Base.metadata

def run_migrations_offline():
    """Exécute les migrations en mode offline (génère du SQL sans se connecter)."""
    context.configure(
        url=DATABASE_URL_SYNC,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Exécute les migrations en mode online (connexion réelle à la base)."""
    connectable = create_engine(DATABASE_URL_SYNC, echo=True, future=True)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# Choix du mode en fonction de la commande Alembic
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
