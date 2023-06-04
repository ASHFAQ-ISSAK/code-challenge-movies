"""Create roles table

Revision ID: 9744218a4873
Revises: cb2ab2541078
Create Date: 2023-06-04 19:16:47.087127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9744218a4873"
down_revision = "cb2ab2541078"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("movie_id", sa.Integer(), sa.ForeignKey("movies.id"), nullable=False),
        sa.Column("actor_id", sa.Integer(), sa.ForeignKey("actors.id"), nullable=False),
        sa.Column("salary", sa.Integer(), nullable=True),
        sa.Column("character_name", sa.String(), nullable=True),
    )


def downgrade():
    op.drop_table("roles")
