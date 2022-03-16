from uuid import UUID

from sqlalchemy import String, Date, Time, Float


class UberParser:
    db_table = 'uber_orders'

    column_mapper = {'Order ID':'order_id',
                     'Workflow ID': 'workflow_id',
                     'Store Name':'store_name',
                     'Order Date / Refund date':'order_or_refund_date',
                     'Order Accept Time':'order_accept_time',
                     'Food Sales (excl VAT)':'food_sales_excl_vat',
                     'Food Sales (incl VAT)':'food_sales_incl_vat',
                     'Delivery Fee (incl VAT)':'delivery_fee_incl_vat',
                     'Total Order (incl VAT)':'total_order_incl_vat',
                     'Cost of Delivery (incl VAT)':'cost_of_delivery_incl_vat',
                     'Gratuity':'gratuity',
                     'Misc Payment Description':'misc_payment_description',
                     'Misc. Payments (incl VAT)':'misc_payments_incl_vat',
                     'Payout':'payout',
                     'Payout Date':'payout_date',
                     'Order Status':'order_status'}

    column_dtype  = {'order_id':String,
                     'workflow_id': UUID,
                     'store_name':String,
                     'order_or_refund_date':Date,
                     'order_accept_time':Time,
                     'food_sales_excl_vat':Float,
                     'food_sales_incl_vat':Float,
                     'delivery_fee_incl_vat':Float,
                     'total_order_incl_vat':Float,
                     'cost_of_delivery_incl_vat':Float,
                     'gratuity':Float,
                     'misc_payment_description': Float,
                     'misc_payments_incl_vat': Float,
                     'payout':Float,
                     'payout_date':Date,
                     'order_status':String}
