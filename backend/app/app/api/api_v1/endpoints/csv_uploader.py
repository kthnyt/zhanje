from typing import Any, Optional

import pandas as pd
from psycopg2 import errors
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException, Form
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.config import settings
from app import models, crud
from app.api import deps
from app.parsers import Parser


router = APIRouter()
UniqueViolation = errors.lookup('23505')

@router.post("/csv-uploader/")
async def create_upload_csv(
        db: Session = Depends(deps.get_db),
        template: str = Form(...),
        csv_file: UploadFile = File(...),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new csv file upload and parsing.
    """
    if not template:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="template string not found")

    rows_affected: Optional[int] = None

    try:
        platform = crud.platform.get_by_name(db, name=template)

        if not platform:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No platform found matching template name: '{template}'")
        parser_obj = Parser()
        parser= parser_obj.set_by_template(platform.name)

        df = pd.read_csv(csv_file.file)
        df = df.rename(columns=parser.column_mapper).copy()

        df['platform_id'] = platform.id
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
        rows_affected = df.to_sql(
                            name=parser.db_table,
                            con=engine,
                            if_exists='append',
                            index=False,
                            chunksize=500,
                            dtype=parser.column_dtype)
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            # dupe_field = parse(
            #     'duplicate key value violates unique constraint "{constraint}"\nDETAIL:  Key ({field})=({input}) already exists.\n',
            #     str(e.orig))["field"]
            # TODO: parse args
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.args[0])
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args[0])

        # print(e.message)
    return {"filename": csv_file.filename, "template": template, "rows_affected": rows_affected}
