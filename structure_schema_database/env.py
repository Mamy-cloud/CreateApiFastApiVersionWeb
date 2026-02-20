from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from alembic import context
from app.database.database_web import Base

load_dotenv()

DATABASE_URL_SYNC = os.getenv("DATABASE_URL_SYNC_ALEMBIC")
if not DATABASE_URL_SYNC:
    raise RuntimeError("DATABASE_URL_SYNC_ALEMBIC is not set in .env")

target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_engine(DATABASE_URL_SYNC)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

