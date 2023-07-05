"""Modify Account to handle Open Collective account type

Revision ID: 980eb1553510
Revises: e1649ad1d26b
Create Date: 2023-07-05 11:02:43.048153

"""
from alembic import op
import sqlalchemy as sa


# Polar Custom Imports
from polar.kit.extensions.sqlalchemy import PostgresUUID

# revision identifiers, used by Alembic.
revision = "980eb1553510"
down_revision = "e1649ad1d26b"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "accounts",
        sa.Column("open_collective_slug", sa.String(length=255), nullable=True),
    )
    op.alter_column(
        "accounts",
        "account_type",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(length=255),
        existing_nullable=False,
    )
    op.alter_column(
        "accounts", "stripe_id", existing_type=sa.VARCHAR(length=100), nullable=True
    )
    op.alter_column(
        "accounts",
        "business_type",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(length=255),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "accounts",
        "business_type",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=10),
    )
    op.alter_column(
        "accounts", "stripe_id", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.alter_column(
        "accounts",
        "account_type",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=10),
        existing_nullable=False,
    )
    op.drop_column("accounts", "open_collective_slug")
    # ### end Alembic commands ###
