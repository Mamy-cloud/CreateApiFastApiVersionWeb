from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.database.database_web import get_session
from app.request_and_data.PostgreSQL_request import post_add_columns_sql
from app.database.database_web import engine
from app.request_and_data.type_data import map_type_to_postgres, DEFAULT_VALUES

router = APIRouter()


class ColumnItem(BaseModel):
    column_name: str
    type_of_column: str
    default: Optional[str] = None


# 👇 Modèle qui correspond EXACTEMENT à ton JSON frontend
class AddColumnsRequest(BaseModel):
    columns: List[ColumnItem]


@router.post("/admin/tables/{table_name}/add-columns")
async def add_columns(
    table_name: str,
    request: AddColumnsRequest,  # 👈 on reçoit { columns: [...] }
    db: AsyncSession = Depends(get_session)
):
    try:
        transformed_columns = []

        for col in request.columns:
            pg_type = map_type_to_postgres(col.type_of_column)

            default_value = (
                col.default
                if col.default is not None
                else DEFAULT_VALUES.get(pg_type)
            )

            transformed_columns.append({
                "column_name": col.column_name,
                "type": pg_type,
                "default": default_value
            })

        sql = post_add_columns_sql(table_name, transformed_columns)

        await db.execute(sql)
        await db.commit()

        await engine.dispose()

        added = ", ".join([col.column_name for col in request.columns])

        return {
            "message": f"Colonne(s) {added} ajoutée(s) à {table_name}"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))