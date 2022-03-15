"""add mrd

Revision ID: 255afeb7035b
Revises: 13eb28975d02
Create Date: 2022-03-15 22:40:04.062221

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '255afeb7035b'
down_revision = '13eb28975d02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mrds',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mrds')
    # ### end Alembic commands ###