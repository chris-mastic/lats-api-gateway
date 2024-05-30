"""05172024_addadditionalcolumns

Revision ID: 14abd921bcaf
Revises: e948cba3d608
Create Date: 2024-05-17 11:12:08.317723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '14abd921bcaf'
down_revision: Union[str, None] = 'e948cba3d608'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('jur', sa.String(length=4), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('altid', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('assessment_number', sa.String(length=20), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('city', sa.String(length=50), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('state', sa.String(length=2), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('zipcode', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_ltc_sub_class_old', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_ltc_sub_class_new', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_quantity_old', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_quantity_new', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_units_old', sa.String(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_units_new', sa.String(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_other_exempt_old', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_other_exempt_new', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_old_total', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_new_total', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_old_hs', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_new_hs', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_old_tp', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('land_value_new_tp', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_ltc_sub_class_old', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_ltc_sub_class_new', sa.String(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_quantity_old', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_quantity_new', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_units_old', sa.String(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_units_new', sa.String(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_other_exempt_old', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_other_exempt_new', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_old_tota', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_new_total', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_old_hs', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_new_hs', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_old_tp', sa.Integer(), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('building_value_new_tp', sa.Integer(), nullable=True))
    op.drop_column('noa_ltc_change_order', 'other_exempt_old_building')
    op.drop_column('noa_ltc_change_order', 'value_old_total_land')
    op.drop_column('noa_ltc_change_order', 'units_new_land')
    op.drop_column('noa_ltc_change_order', 'value_new_hs_land')
    op.drop_column('noa_ltc_change_order', 'ltc_sub_class_old_land')
    op.drop_column('noa_ltc_change_order', 'quantity_new_building')
    op.drop_column('noa_ltc_change_order', 'units_new_building')
    op.drop_column('noa_ltc_change_order', 'value_new_total_building')
    op.drop_column('noa_ltc_change_order', 'value_old_tp_land')
    op.drop_column('noa_ltc_change_order', 'quantity_new_land')
    op.drop_column('noa_ltc_change_order', 'ltc_sub_class_old_building')
    op.drop_column('noa_ltc_change_order', 'value_new_tp_building')
    op.drop_column('noa_ltc_change_order', 'value_old_tota_building')
    op.drop_column('noa_ltc_change_order', 'value_old_hs_building')
    op.drop_column('noa_ltc_change_order', 'value_new_total_land')
    op.drop_column('noa_ltc_change_order', 'quantity_old_land')
    op.drop_column('noa_ltc_change_order', 'other_exempt_old_land')
    op.drop_column('noa_ltc_change_order', 'value_new_tp_land')
    op.drop_column('noa_ltc_change_order', 'value_new_hs_building')
    op.drop_column('noa_ltc_change_order', 'units_old_land')
    op.drop_column('noa_ltc_change_order', 'value_old_hs_land')
    op.drop_column('noa_ltc_change_order', 'other_exempt_new_building')
    op.drop_column('noa_ltc_change_order', 'value_old_tp_building')
    op.drop_column('noa_ltc_change_order', 'quantity_old_building')
    op.drop_column('noa_ltc_change_order', 'units_old_building')
    op.drop_column('noa_ltc_change_order', 'assessment_no')
    op.drop_column('noa_ltc_change_order', 'other_exempt_new_land')
    op.drop_column('noa_ltc_change_order', 'ltc_sub_class_new_building')
    op.drop_column('noa_ltc_change_order', 'ltc_sub_class_new_land')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('noa_ltc_change_order', sa.Column('ltc_sub_class_new_land', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('ltc_sub_class_new_building', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('other_exempt_new_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('assessment_no', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('units_old_building', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('quantity_old_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_tp_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('other_exempt_new_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_hs_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('units_old_land', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_hs_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_tp_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('other_exempt_old_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('quantity_old_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_total_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_hs_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_tota_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_tp_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('ltc_sub_class_old_building', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('quantity_new_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_tp_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_total_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('units_new_building', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('quantity_new_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('ltc_sub_class_old_land', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_new_hs_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('units_new_land', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('value_old_total_land', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('noa_ltc_change_order', sa.Column('other_exempt_old_building', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('noa_ltc_change_order', 'building_value_new_tp')
    op.drop_column('noa_ltc_change_order', 'building_value_old_tp')
    op.drop_column('noa_ltc_change_order', 'building_value_new_hs')
    op.drop_column('noa_ltc_change_order', 'building_value_old_hs')
    op.drop_column('noa_ltc_change_order', 'building_value_new_total')
    op.drop_column('noa_ltc_change_order', 'building_value_old_tota')
    op.drop_column('noa_ltc_change_order', 'building_other_exempt_new')
    op.drop_column('noa_ltc_change_order', 'building_other_exempt_old')
    op.drop_column('noa_ltc_change_order', 'building_units_new')
    op.drop_column('noa_ltc_change_order', 'building_units_old')
    op.drop_column('noa_ltc_change_order', 'building_quantity_new')
    op.drop_column('noa_ltc_change_order', 'building_quantity_old')
    op.drop_column('noa_ltc_change_order', 'building_ltc_sub_class_new')
    op.drop_column('noa_ltc_change_order', 'building_ltc_sub_class_old')
    op.drop_column('noa_ltc_change_order', 'land_value_new_tp')
    op.drop_column('noa_ltc_change_order', 'land_value_old_tp')
    op.drop_column('noa_ltc_change_order', 'land_value_new_hs')
    op.drop_column('noa_ltc_change_order', 'land_value_old_hs')
    op.drop_column('noa_ltc_change_order', 'land_value_new_total')
    op.drop_column('noa_ltc_change_order', 'land_value_old_total')
    op.drop_column('noa_ltc_change_order', 'land_other_exempt_new')
    op.drop_column('noa_ltc_change_order', 'land_other_exempt_old')
    op.drop_column('noa_ltc_change_order', 'land_units_new')
    op.drop_column('noa_ltc_change_order', 'land_units_old')
    op.drop_column('noa_ltc_change_order', 'land_quantity_new')
    op.drop_column('noa_ltc_change_order', 'land_quantity_old')
    op.drop_column('noa_ltc_change_order', 'land_ltc_sub_class_new')
    op.drop_column('noa_ltc_change_order', 'land_ltc_sub_class_old')
    op.drop_column('noa_ltc_change_order', 'zipcode')
    op.drop_column('noa_ltc_change_order', 'state')
    op.drop_column('noa_ltc_change_order', 'city')
    op.drop_column('noa_ltc_change_order', 'assessment_number')
    op.drop_column('noa_ltc_change_order', 'altid')
    op.drop_column('noa_ltc_change_order', 'jur')
    # ### end Alembic commands ###