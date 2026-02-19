# post_column.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.database.database_web import get_session
from app.request_and_data.PostgreSQL_request import post_add_columns_sql

router = APIRouter()

class ColumnItem(BaseModel):
    name: str
    type: str
    default: str = ""

class AddColumnsRequest(BaseModel):
    columns: list[ColumnItem]

@router.post("/admin/tables/{table_name}/add-columns")
async def add_columns(
    table_name: str,
    request: AddColumnsRequest,
    db: AsyncSession = Depends(get_session)
):
    try:
        sql = post_add_columns_sql(table_name, [col.dict() for col in request.columns])
        await db.execute(sql)
        await db.commit()
        await db.close()
        added = ", ".join([col.name for col in request.columns])
        return {"message": f"Colonne(s) {added} ajoutée(s) à {table_name}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
