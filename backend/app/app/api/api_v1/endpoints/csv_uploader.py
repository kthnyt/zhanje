from typing import Any, Optional

import pandas as pd
from app.core.config import settings
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy import String, Date, Time, Float, create_engine
from sqlalchemy.orm import Session

from app import models, crud
from app.api import deps
from starlette import status

router = APIRouter()

mrdorder_mapper = {'Invoice Number':'invoice_number',
                   'Date':'date',
                   'Time':'time',
                   'Restaurant':'restaurant',
                   'Suburb':'suburb',
                   'Prep Time':'prep_time_minutes',
                   'Type':'order_type',
                   'Food Total':'food_total',
                   'Comm. Ex VAT(%)':'commission_ex_vat_per',
                   'Due To You':'due_to_you',
                   'Restaurant Status':'restaurant_status'}

mrdorder_dtype = {'invoice_number':String,
                  'date':Date,
                  'time':Time,
                  'restaurant':String,
                  'suburb':String,
                  'prep_time_minutes':Float,
                  'order_type':String,
                  'food_total':Float,
                  'commission_ex_vat_per':Float,
                  'due_to_you':Float,
                  'restaurant_status':String}

@router.post("/csv-uploader/")
async def create_upload_csv(
        db: Session = Depends(deps.get_db),
        template: Optional[str] = None,
        csv_file: UploadFile = File(...),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new csv file upload and parsing.
    """
    if not template:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="template string not found")

    try:
        platform = crud.platform.get_by_name(db, name=template)
        df = pd.read_csv(csv_file.file)
        df = df.rename(columns=mrdorder_mapper).copy()
        df['platform_id'] = platform.id
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
        df.to_sql(name='mrdorders', con=engine, schema=None, if_exists='append', index=False, chunksize=None, dtype=mrdorder_dtype, method=None)
    except Exception as error:
        pass
    return {"filename": csv_file.filename, "template": template}
