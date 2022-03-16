from sqlalchemy import String, Date, Time, Float


class UberParser:
    db_table = 'uberorders'

    column_mapper = {'Order ID':'Order_Id',
                     'Store Name':'Store_Name',
                     'Order Date / Refund date':'Order_Or_Refund_Date',
                     'Order Accept Time':'Order_Accept_Time',
                     'Food Sales (excl VAT)':'Food_Sales_Excl_Vat',
                     'Food Sales (incl VAT)':'Food_Sales_Incl_Vat',
                     'Delivery Fee (incl VAT)':'Delivery_Fee_Incl_Vat',
                     'Total Order (incl VAT)':'Total_Order_Incl_Vat',
                     'Cost of Delivery (incl VAT)':'Cost_Of_Delivery_Incl_Vat',
                     'Gratuity':'Gratuity',
                     'Payout':'Payout',
                     'Payout Date':'Payout_Date',
                     'Order Status':'Order_Status'}

    column_dtype  = {'order_id':String,
                     'store_name':String,
                     'order_or_refund_date':Date,
                     'order_accept_time':Time,
                     'food_sales_excl_vat':Float,
                     'food_sales_incl_vat':Float,
                     'delivery_fee_incl_vat':Float,
                     'total_order_incl_vat':Float,
                     'cost_of_delivery_incl_vat':Float,
                     'gratuity':Float,
                     'payout':Float,
                     'payout_date':Date,
                     'order_status':String}
