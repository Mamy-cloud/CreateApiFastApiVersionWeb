from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database_web import get_db
from app.request_and_data.PostgreSQL_request import get_rows_sql

router = APIRouter()

@router.get("/admin/tables/rows/{table_name}")
async def get_rows(table_name: str, db: AsyncSession = Depends(get_db)):
    sql = get_rows_sql(table_name)
    result = await db.execute(sql)
    rows = result.fetchall()

    # Structuration JSON
    output = []
    for row in rows:
        for col, val in row._mapping.items():
            output.append({
                "row_name": col,
                "value_data": val if val is not None else None
            })

    return output
