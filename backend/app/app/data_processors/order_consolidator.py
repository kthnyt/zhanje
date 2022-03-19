from typing import Optional

import pandas as pd
from app.core.config import settings
from fastapi import HTTPException
from sqlalchemy import create_engine
from starlette import status

from app.models import LoyverseOrder, UberOrder, MrDOrder


class OrderProcessor:
    # if mrd:
    # use mrd_to_consol mapper
    # change df to consol_df
    #  consol_df.to_sql
    # write into platform_order db is_processed
    # run it in batches, switching between platforms
    # scheduler 1 hour
    #  trigger manual bulk processing on anny order-related api call

    #  ????? ######################
    #  Trigger an asynchronous celery task to consolidated platform orders, on CSV upload
    #  Schedular to clean up afterward, if any platform orders remain unprocessed
    # celery_app.send_task("app.worker.consolidate_platform_orders", args=[template])
    # beat takes over where async does not finish processing
    def __init__(self):
        self._platform = {
            "MRDFOOD": "mrdorders",
            "UBEREATS": "uberorders",
            "LOYVERSE": "loyverseorders"
        }


    def consolidate(self, template: str):
        # iterate thorough all platforms when scheduler is consolidating with `template='All'`
        if template:
            if template == 'All':
                pass
            # else deal with platform from current template
            else:
                # pd.read_sql chunk of unprocessed template orders
                engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
                try:
                    # sql_query = """SELECT * FROM %(table)s  where %(column)s = %(condiiton)s"""
                    # df = pd.read_sql(
                    #     sql=sql_query,
                    #     con=engine,
                    #     params={'table' : self._platform[template], 'column': 'is_processed', 'condition': 'false'},
                    #     index_col=None,
                    #     chunksize=50)
                    # print(df.head(2))
                    pass
                except Exception as e:
                    print('ERROR')

            # filter columns using platform_to_consol column_map
            # rename columns
            # df.to_sql
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Template argument can not be left empty')
        return False
