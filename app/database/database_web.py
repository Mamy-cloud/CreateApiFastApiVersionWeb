import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL_ASYNC")
# Exemple : "postgresql+asyncpg://user:password@localhost:5432/ma_base"

# 1️⃣ Créer l'engine asynchrone
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    # ⚠️ pool_size et max_overflow ne sont pas supportés par asyncpg, on les supprime
)

# 2️⃣ Créer le sessionmaker asynchrone (SQLAlchemy 2.x)
SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=True
)

# 3️⃣ Base pour les modèles ORM
Base = declarative_base()

# 4️⃣ Dépendance FastAPI
async def get_db():
    async with SessionLocal() as session:
        yield session


async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

