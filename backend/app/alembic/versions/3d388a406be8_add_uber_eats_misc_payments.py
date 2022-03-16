"""add uber eats misc payments

Revision ID: 3d388a406be8
Revises: 44e433255140
Create Date: 2022-03-16 18:08:08.045895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d388a406be8'
down_revision = '44e433255140'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('uber_orders', sa.Column('misc_payment_description', sa.Float(), nullable=True))
    op.add_column('uber_orders', sa.Column('misc_payments_incl_vat', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('uber_orders', 'misc_payments_incl_vat')
    op.drop_column('uber_orders', 'misc_payment_description')
    # ### end Alembic commands ###