#----------------------create table------------------------------
from sqlalchemy import text

def build_create_table_sql(table_name, columns, default_values):
    # ⚡ Sécuriser le nom de table
    sql = f'CREATE TABLE "{table_name}" (\n'
    sql += "    id SERIAL PRIMARY KEY,\n"

    for col in columns:
        col_name = col["column_name"]
        col_type = col["type_of_column"]

        # Valeur par défaut
        if col_type in default_values:
            default_val = default_values[col_type]
            if isinstance(default_val, str):
                default_val = f"DEFAULT '{default_val}'"
            else:
                default_val = f"DEFAULT {default_val}"
        else:
            default_val = ""

        sql += f'    "{col_name}" {col_type} {default_val},\n'

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

import re
from sqlalchemy import text

def safe_identifier(name: str) -> str:
    """Vérifie que le nom est sûr pour SQL (lettres, chiffres, underscore)."""
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
        raise ValueError(f"Nom invalide : {name}")
    return name

def post_add_columns_sql(table_name: str, columns: list[dict]):
    """
    Génère une requête SQL pour ajouter une ou plusieurs colonnes.

    columns = [
        {"name": "col1", "type": "INTEGER", "default": "DEFAULT 0"},
        {"name": "col2", "type": "VARCHAR", "default": "DEFAULT ''"}
    ]
    """
    table_name = safe_identifier(table_name)
    column_clauses = []
    for col in columns:
        col_name = safe_identifier(col["name"])
        col_type = col["type"].upper()
        default_value = col.get("default", "")
        column_clauses.append(f'"{col_name}" {col_type} {default_value}')

    # On concatène toutes les colonnes avec ALTER TABLE
    sql = f'ALTER TABLE "{table_name}" ADD COLUMN ' + ", ADD COLUMN ".join(column_clauses)
    return text(sql)






