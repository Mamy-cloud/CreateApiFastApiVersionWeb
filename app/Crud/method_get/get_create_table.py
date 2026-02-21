import os
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database import database_web
from app.request_and_data.type_data import DEFAULT_VALUES, map_type_to_postgres
from app.request_and_data.PostgreSQL_request import build_create_table_sql
from pathlib import Path

router = APIRouter()



@router.post("/admin/tables/json")


async def create_table(payload: dict, db: AsyncSession = Depends(database_web.get_db)):
    table_name = payload["table_name"]
    columns = payload["columns"]

    # ⚡ Appliquer le mapping pour chaque colonne
    mapped_columns = []
    for col in columns:
        mapped_columns.append({
            "column_name": col["column_name"],
            "type_of_column": map_type_to_postgres(col["type_of_column"])
        })

    # Construire la requête SQL avec les types traduits
    sql = build_create_table_sql(table_name, mapped_columns, DEFAULT_VALUES)

    await db.execute(text(sql))
    await db.commit()

    return {"status": "success", "sql": sql, "json": payload}


@router.get("/admin/tables/json")
async def test_get():
    return {"message": "Cette route est GET pour test"}
