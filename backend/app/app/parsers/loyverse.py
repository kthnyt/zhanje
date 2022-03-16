from sqlalchemy import String, Date, Time, Float, Integer, DateTime


class LoyverseParser:
    db_table = 'loyverseorders'

    column_mapper = {'Date':'date',
                     'Receipt number':'receipt_number',
                     'Receipt type':'receipt_type',
                     'Category':'category',
                     'SKU':'sku',
                     'Item':'item',
                     'Variant':'variant',
                     'Modifiers applied':'modifiers_applied',
                     'Quantity':'quantity',
                     'Gross sales':'gross_sales',
                     'Discounts':'discounts',
                     'Net sales':'net_sales',
                     'Cost of goods':'cost_of_goods',
                     'Gross profit':'gross_profit',
                     'Taxes':'taxes',
                     'Dining option':'dining_option',
                     'POS':'pos',
                     'Store':'store',
                     'Cashier name':'cashier_name',
                     'Customer name':'customer_name',
                     'Customer contacts':'customer_contacts',
                     'Comment':'comment',
                     'Status':'status'}

    column_dtype  = {'date':DateTime,
                     'receipt_number':String,
                     'receipt_type':String,
                     'category':String,
                     'sku':Integer,
                     'item':String,
                     'variant':String,
                     'modifiers_applied':String,
                     'quantity':Integer,
                     'gross_sales':Float,
                     'discounts':Float,
                     'net_sales':Float,
                     'cost_of_goods':Float,
                     'gross_profit':Float,
                     'taxes':Float,
                     'dining_option':String,
                     'pos':String,
                     'store':String,
                     'cashier_name':String,
                     'customer_name':String,
                     'customer_contacts':String,
                     'comment':String,
                     'status':String}
