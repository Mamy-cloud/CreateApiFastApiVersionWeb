# routes_admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database_web import get_session
from app.request_and_data.PostgreSQL_request import post_rename_table_sql
from pydantic import BaseModel

router = APIRouter()



class RenameRequest(BaseModel):
    new_name: str

@router.post("/admin/tables/{old_name}/rename")
async def rename_table(old_name: str, request: RenameRequest, db: AsyncSession = Depends(get_session)):
    sql = post_rename_table_sql(old_name, request.new_name)
    await db.execute(sql)
    await db.commit()
    await db.close()
    return {"message": f"Table {old_name} renommée en {request.new_name}"}


