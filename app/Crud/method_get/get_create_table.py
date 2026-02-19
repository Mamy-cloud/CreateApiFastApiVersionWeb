import os
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database import database_web
from app.request_and_data.type_data import DEFAULT_VALUES
from app.request_and_data.PostgreSQL_request import build_create_table_sql
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

@router.post("/admin/tables/json")
async def create_table(payload: dict, db: AsyncSession = Depends(database_web.get_db)):
    table_name = payload["table_name"]
    columns = payload["columns"]

    sql = build_create_table_sql(table_name, columns, DEFAULT_VALUES)

    await db.execute(text(sql))   # ⚡ await obligatoire
    await db.commit()             # ⚡ commit asynchrone

    return {"status": "success", "sql": sql, "json": payload}

@router.get("/admin/tables/json")
async def test_get():
    return {"message": "Cette route est GET pour test"}
