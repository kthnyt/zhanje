from sqlalchemy import String, Date, Time, Float


class MrDParser:
    db_table = 'mrdorders'

    column_mapper = {'Invoice Number': 'invoice_number',
                       'Date': 'date',
                       'Time': 'time',
                       'Restaurant': 'restaurant',
                       'Suburb': 'suburb',
                       'Prep Time': 'prep_time_minutes',
                       'Type': 'order_type',
                       'Food Total': 'food_total',
                       'Comm. Ex VAT(%)': 'commission_ex_vat_per',
                       'Due To You': 'due_to_you',
                       'Restaurant Status': 'restaurant_status'}

    column_dtype = {'invoice_number': String,
                      'date': Date,
                      'time': Time,
                      'restaurant': String,
                      'suburb': String,
                      'prep_time_minutes': Float,
                      'order_type': String,
                      'food_total': Float,
                      'commission_ex_vat_per': Float,
                      'due_to_you': Float,
                      'restaurant_status': String}
