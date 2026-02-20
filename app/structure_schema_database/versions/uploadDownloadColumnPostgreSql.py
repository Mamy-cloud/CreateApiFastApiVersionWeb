"""ajout col_c, suppression col_b, renommage col_a -> col_name"""

from alembic import op
import sqlalchemy as sa

# Révision Alembic
revision = "20260220_upload_download_column"
down_revision = None  # ou l'ID de la migration précédente si tu en as une
branch_labels = None
depends_on = None


def upgrade():
    # Ajout d'une colonne col_c
    op.add_column("any_table", sa.Column("col_c", sa.String(), nullable=True))

    # Suppression de col_b
    op.drop_column("any_table", "col_b")

    # Renommage de col_a en col_name
    op.alter_column("any_table", "col_a", new_column_name="col_name")


def downgrade():
    # Suppression de col_c
    op.drop_column("any_table", "col_c")

    # Ré‑ajout de col_b
    op.add_column("any_table", sa.Column("col_b", sa.Integer(), nullable=True))

    # Renommage de col_name en col_a
    op.alter_column("any_table", "col_name", new_column_name="col_a")
