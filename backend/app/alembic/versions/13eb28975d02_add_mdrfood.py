"""add mdrfood

Revision ID: 13eb28975d02
Revises: 924619910053
Create Date: 2022-03-15 22:30:18.242918

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13eb28975d02'
down_revision = '924619910053'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mrdfood',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('invoice_number', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('restaurant', sa.String(), nullable=True),
    sa.Column('suburb', sa.String(), nullable=True),
    sa.Column('prep_time_minutes', sa.Float(), nullable=True),
    sa.Column('order_type', sa.String(), nullable=True),
    sa.Column('food_total', sa.Float(), nullable=False),
    sa.Column('commission_ex_vat_per', sa.Float(), nullable=True),
    sa.Column('due_to_you', sa.Float(), nullable=False),
    sa.Column('restaurant_status', sa.String(), nullable=True),
    sa.Column('platform_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mrdfood_id'), 'mrdfood', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mrdfood_id'), table_name='mrdfood')
    op.drop_table('mrdfood')
    # ### end Alembic commands ###