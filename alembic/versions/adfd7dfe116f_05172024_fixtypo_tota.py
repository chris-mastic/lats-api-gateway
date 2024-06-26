"""05172024_fixtypo_tota

Revision ID: adfd7dfe116f
Revises: e8ef7d6cf3ed
Create Date: 2024-05-17 11:25:34.081585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'adfd7dfe116f'
down_revision: Union[str, None] = 'e8ef7d6cf3ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('building_value_old_total', sa.Integer(), nullable=True))
    op.drop_column('noa_ltc_change_order', 'building_value_old_tota')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('building_value_old_tota', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('noa_ltc_change_order', 'building_value_old_total')
    # ### end Alembic commands ###
