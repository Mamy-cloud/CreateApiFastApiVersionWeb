from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import database_web
from app.Crud.method_get import get_create_table
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import FileResponse
from app.Crud.method_get import get_list_table
from app.traitement_asynch.webSocket import router as websocket_router
from fastapi.middleware.cors import CORSMiddleware
from app.Crud.method_get.get_column import router as list_columns
from app.Crud.method_get import get_column
from app.Crud.method_get import get_row
#--------------post-----------------------------
from app.Crud.method_post import post_rename_table
from app.Crud.method_post import post_column
from app.Crud.method_post.post_column import router as add_column


app = FastAPI()

app = FastAPI(title="WebSocket Example")

# ⚡ Middleware CORS pour autoriser le front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # remplacer par ton front si besoin, ex: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes backend
app.include_router(get_create_table.router)


# BASE_DIR → racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Monter le dossier static
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Route GET pour afficher l'interface graphique de la liste des tables
@app.get("/admin/tables")
async def get_table_page():
    file_path = BASE_DIR / "templates" / "tables.html"
    if not file_path.exists():
        raise RuntimeError(f"Le fichier HTML n'existe pas : {file_path}")
    return FileResponse(file_path)

#route pour l'interface graphique
@app.get("/admin/{table_name}")
async def show_table_page(table_name: str):    
    file_path = BASE_DIR / "templates" / "tables_name.html"
    if not file_path.exists():
        raise RuntimeError(f"Le fichier HTML n'existe pas : {file_path}")
    return FileResponse(file_path)

# Inclure le router pour les routes /admin/tables/list
app.include_router(get_list_table.router)

#inclure le router pour les routes get_column
app.include_router(get_column.router)

#inclure le router pour les routes get_row
app.include_router(get_row.router)

#inclure le router pour les routes rename_colonne
app.include_router(post_rename_table.router)

#inclure le router pour les routes add_colonne
app.include_router(post_column.router)

# Inclure le WebSocket 
""" app.include_router(websocket_router) """


@app.get("/")
def read_root(db: Session = Depends(database_web.get_db)):
    result = db.execute(text("SELECT 1"))
    return {"message": "Connexion réussie avec psycopg2", "result": result.scalar()}
