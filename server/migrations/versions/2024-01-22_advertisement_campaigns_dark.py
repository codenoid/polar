"""advertisement_campaigns_dark

Revision ID: bedd8fdf9f8c
Revises: 5ada39168fdb
Create Date: 2024-01-22 11:06:32.635803

"""
import sqlalchemy as sa
from alembic import op

# Polar Custom Imports
from polar.kit.extensions.sqlalchemy import PostgresUUID

# revision identifiers, used by Alembic.
revision = "bedd8fdf9f8c"
down_revision = "5ada39168fdb"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "advertisement_campaigns",
        sa.Column("image_url_dark", sa.String(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("advertisement_campaigns", "image_url_dark")
    # ### end Alembic commands ###
