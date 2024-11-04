"""chat_history_table

Revision ID: bc036cfd9065
Revises: 
Create Date: 2024-11-05 02:42:41.151300

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "bc036cfd9065"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "chat_history_models",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("message", sa.String(), nullable=False),
        sa.Column("created", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_chat_history_models")),
    )


def downgrade() -> None:
    op.drop_table("chat_history_models")
