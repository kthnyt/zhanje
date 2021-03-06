"""change misc_descrption to String

Revision ID: 98d36a8586d4
Revises: 3d388a406be8
Create Date: 2022-03-16 18:17:24.118305

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '98d36a8586d4'
down_revision = '3d388a406be8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uber_orders', 'misc_payment_description',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uber_orders', 'misc_payment_description',
               existing_type=sa.String(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    # ### end Alembic commands ###
