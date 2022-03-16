from typing import Any, Optional

import pandas as pd
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette import status

from app.core.config import settings
from app import models, crud
from app.api import deps
from app.parsers import Parser


router = APIRouter()


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
        print(platform.name)
        parser_obj = Parser()
        parser= parser_obj.set_by_template(platform.name)

        df = pd.read_csv(csv_file.file)
        df = df.rename(columns=parser.column_mapper).copy()

        df['platform_id'] = platform.id
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
        df.to_sql(
            name=parser.db_table,
            con=engine,
            if_exists='append',
            index=False,
            chunksize=500,
            dtype=parser.column_dtype)
    except Exception as e:
        print(f'{e}')
    return {"filename": csv_file.filename, "template": template}
