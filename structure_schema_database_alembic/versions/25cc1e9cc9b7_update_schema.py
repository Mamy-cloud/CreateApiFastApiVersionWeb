"""update schema

Revision ID: 25cc1e9cc9b7
Revises: e1ac9eb4b53b
Create Date: 2026-02-20 14:40:30.321186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25cc1e9cc9b7'
down_revision = 'e1ac9eb4b53b'
branch_labels = None
depends_on = None



def upgrade():
    # Exemple générique : modifications sur une table
    with op.batch_alter_table("nom_table") as batch_op:
        # Ajout de colonnes
        batch_op.add_column(sa.Column("nouvelle_colonne1", sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column("nouvelle_colonne2", sa.Integer(), nullable=False, server_default="0"))

        # Suppression de colonnes
        batch_op.drop_column("ancienne_colonne")

        # Renommage de colonnes
        batch_op.alter_column("colonne_a_renommer", new_column_name="nouveau_nom_colonne")

def downgrade():
    # Inverse des opérations ci-dessus
    with op.batch_alter_table("nom_table") as batch_op:
        # Suppression des colonnes ajoutées
        batch_op.drop_column("nouvelle_colonne1")
        batch_op.drop_column("nouvelle_colonne2")

        # Réajout de la colonne supprimée
        batch_op.add_column(sa.Column("ancienne_colonne", sa.String(length=100), nullable=True))

        # Renommage inverse
        batch_op.alter_column("nouveau_nom_colonne", new_column_name="colonne_a_renommer")
