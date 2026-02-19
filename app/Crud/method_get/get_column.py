from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database_web import get_db 
from app.request_and_data.PostgreSQL_request import get_columns_sql

router = APIRouter()

@router.get("/admin/tables/columns/{table_name}")
async def list_columns(table_name: str, db: AsyncSession = Depends(get_db)):
    sql = get_columns_sql(table_name)
    result = await db.execute(sql)
    rows = result.fetchall()

    # Conversion en JSON
    columns = [
        {"column_name": row[0], "type_data": row[1]}
        for row in rows
    ]

    return columns
