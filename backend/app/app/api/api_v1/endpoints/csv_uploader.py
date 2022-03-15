from typing import Any, Optional

from app import models, schemas
from app.api import deps
from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/csv-uploader/")
async def create_upload_csv(
        db: Session = Depends(deps.get_db),
        # csv_in = schemas.CsvUploaderCreate,
        template: Optional[str] = None,
        csv_file: UploadFile = File(...),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new csv file upload and parsing.
    """
    return {"filename": csv_file.filename, "template": template or csv_in.template}
