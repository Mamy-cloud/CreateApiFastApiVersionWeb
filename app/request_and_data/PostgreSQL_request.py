#----------------------create table------------------------------
from sqlalchemy import text
import re

def build_create_table_sql(table_name, columns, default_values):
    sql = f'CREATE TABLE "{table_name}" (\n    id SERIAL PRIMARY KEY,\n'
    for col in columns:
        col_name = col["column_name"]
        col_type = col["type_of_column"]
        default_val = default_values.get(col_type)
        if default_val is not None:
            sql += f'    "{col_name}" {col_type} DEFAULT {default_val},\n'
        else:
            sql += f'    "{col_name}" {col_type},\n'
    sql = sql.rstrip(",\n") + "\n);"
    return sql

#----------------------get name list table----------------------------


def get_all_table_names_sql(schema: str = "public") -> str:
    """
    Retourne la requête SQL pour lister toutes les tables dans le schéma donné.
    """
    return text(f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '{schema}'
        AND table_type = 'BASE TABLE';
    """)

#--------------------------get column-------------------------------------

def get_columns_sql(table_name: str, schema: str = "public"):
    """
    Génère une requête SQL pour obtenir les colonnes d'une table PostgreSQL.
    """
    sql = text("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = :schema
          AND table_name   = :table
    """)
    return sql.bindparams(schema=schema, table=table_name)

#--------------------get row--------------------------------------------

def get_rows_sql(table_name: str):
    """
    Requête PostgreSQL classique pour récupérer toutes les lignes d'une table.
    """
    return text(f'SELECT * FROM "{table_name}";')

#--------------------post table_name----------------------------------

def post_rename_table_sql(old_name: str, new_name: str):
    """
    Retourne la requête SQL pour renommer une table PostgreSQL.
    """
    return text(f'ALTER TABLE "{old_name}" RENAME TO "{new_name}"')

#------------------post column-----------------------------------------

# PostgreSQL_request.py

def safe_identifier(name: str) -> str:
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
        raise ValueError(f"Nom invalide : {name}")
    return name

def post_add_columns_sql(table_name: str, columns: list[dict]):
    table_name = safe_identifier(table_name)
    column_clauses = []
    for col in columns:
        col_name = safe_identifier(col["name"])
        col_type = col["type"].upper()
        default_value = col.get("default")
        if default_value:
            clause = f'"{col_name}" {col_type} DEFAULT {default_value}'
        else:
            clause = f'"{col_name}" {col_type}'
        column_clauses.append(clause)

    sql = f'ALTER TABLE "{table_name}" ' + ", ".join([f'ADD COLUMN IF NOT EXISTS {clause}' for clause in column_clauses])
    return text(sql)







