"""refactor rename platform order models

Revision ID: 7b9d6dfe061c
Revises: 86353543b8ac
Create Date: 2022-03-16 16:05:16.084275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b9d6dfe061c'
down_revision = '86353543b8ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loyverse_orders',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('receipt_number', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('sku', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('gross_sales', sa.Float(), nullable=True),
    sa.Column('pos', sa.String(), nullable=True),
    sa.Column('store', sa.String(), nullable=True),
    sa.Column('cashier_name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('platform_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('receipt_number')
    )
    op.create_table('mrd_orders',
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
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('invoice_number')
    )
    op.create_table('uber_orders',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('store_name', sa.String(), nullable=True),
    sa.Column('order_or_refund_date', sa.Date(), nullable=True),
    sa.Column('order_accept_time', sa.Time(), nullable=True),
    sa.Column('food_sales_excl_vat', sa.Float(), nullable=True),
    sa.Column('food_sales_incl_vat', sa.Float(), nullable=True),
    sa.Column('delivery_fee_incl_vat', sa.Float(), nullable=True),
    sa.Column('total_order_incl_vat', sa.Float(), nullable=True),
    sa.Column('cost_of_delivery_incl_vat', sa.Float(), nullable=True),
    sa.Column('gratuity', sa.Float(), nullable=True),
    sa.Column('payout', sa.Float(), nullable=True),
    sa.Column('payout_date', sa.Date(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=True),
    sa.Column('platform_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_id')
    )
    op.drop_table('mrdorders')
    op.drop_table('uberorders')
    op.drop_table('loyverseorders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loyverseorders',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('receipt_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('sku', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('item', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gross_sales', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pos', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('store', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cashier_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('platform_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], name='loyverseorders_platform_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='loyverseorders_pkey'),
    sa.UniqueConstraint('receipt_number', name='loyverseorders_receipt_number_key')
    )
    op.create_table('uberorders',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('order_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('store_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('order_or_refund_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('order_accept_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('food_sales_excl_vat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('food_sales_incl_vat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('delivery_fee_incl_vat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('total_order_incl_vat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cost_of_delivery_incl_vat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('gratuity', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('payout', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('payout_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('order_status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('platform_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], name='uberorders_platform_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='uberorders_pkey'),
    sa.UniqueConstraint('order_id', name='uberorders_order_id_key')
    )
    op.create_table('mrdorders',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('invoice_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('restaurant', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('suburb', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prep_time_minutes', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('order_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('food_total', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('commission_ex_vat_per', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('due_to_you', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('restaurant_status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('platform_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['platform_id'], ['platforms.id'], name='mrdorders_platform_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='mrdorders_pkey'),
    sa.UniqueConstraint('invoice_number', name='mrdorders_invoice_number_key')
    )
    op.drop_table('uber_orders')
    op.drop_table('mrd_orders')
    op.drop_table('loyverse_orders')
    # ### end Alembic commands ###