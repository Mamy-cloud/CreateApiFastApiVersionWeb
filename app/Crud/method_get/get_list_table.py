from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database import database_web
from app.request_and_data.PostgreSQL_request import get_all_table_names_sql

router = APIRouter()

@router.get("/admin/tables/list")
async def list_tables(db: AsyncSession = Depends(database_web.get_db)):
    """
    Retourne la liste des tables sous forme JSON :
    [
        {"table_name": "table1"},
        {"table_name": "table2"}
    ]
    """
    sql = get_all_table_names_sql()
    result = await db.execute(sql)
    rows = result.mappings().all()  # 🔹 convertit directement en dict
    return rows  # FastAPI sait sérialiser une liste de dict en JSON
