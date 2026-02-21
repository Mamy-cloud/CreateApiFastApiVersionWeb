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

#----------------------get table-------------------------------------
# PostgreSql_request.py

def get_table_PostgreSql(table_name: str) -> str:
    return f"""
        SELECT json_build_object(
            'table', '{table_name}', -- ajout du nom de la table
            'columns', (
                SELECT json_agg(json_build_object(
                    'name', column_name,
                    'type', data_type
                ))
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
            ),
            'rows', (
                SELECT COALESCE(json_agg(row_to_json(t)), '[]'::json)
                FROM (SELECT * FROM {table_name}) t
            )
        );
    """




#--------------------post table_name----------------------------------

def post_rename_table_sql(old_name: str, new_name: str):
    """
    Retourne la requête SQL pour renommer une table PostgreSQL.
    """
    return text(f'ALTER TABLE "{old_name}" RENAME TO "{new_name}"')



#------------------post column-----------------------------------------

# PostgreSQL_request.py

# PostgreSQL_request.py

import re
from sqlalchemy import text


def safe_identifier(name: str) -> str:
    """
    Sécurise les noms de table et de colonnes.
    Autorise uniquement lettres, chiffres et underscore.
    """
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
        raise ValueError(f"Nom invalide : {name}")
    return name


def post_add_columns_sql(table_name: str, columns: list[dict]):
    """
    Génère une requête ALTER TABLE pour ajouter une ou plusieurs colonnes.
    Compatible toutes tables / toutes colonnes.
    """

    table_name = safe_identifier(table_name)
    column_clauses = []

    for col in columns:
        col_name = safe_identifier(col["column_name"])
        col_type = col["type"].upper()
        default_value = col.get("default")

        if default_value is not None and default_value != "":
            clause = f'"{col_name}" {col_type} DEFAULT {default_value}'
        else:
            clause = f'"{col_name}" {col_type}'

        column_clauses.append(
            f'ADD COLUMN IF NOT EXISTS {clause}'
        )

    sql = f'ALTER TABLE "{table_name}" ' + ", ".join(column_clauses)

    return text(sql)







