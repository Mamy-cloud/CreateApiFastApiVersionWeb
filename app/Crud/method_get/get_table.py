# get_table.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database.database_web import get_db
from app.request_and_data.PostgreSQL_request import get_table_PostgreSql

router = APIRouter()

@router.get("/admin/{table_name}/get_table")
async def get_table(table_name: str, session: AsyncSession = Depends(get_db)):
    query = get_table_PostgreSql(table_name)

    result = await session.execute(text(query))
    json_data = result.scalar()  # récupère directement l'objet JSON

    return json_data



