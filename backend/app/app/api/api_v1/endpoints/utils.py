import os
from typing import Any

from app.core.config import settings
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from app import models, schemas
from app.api import deps
from app.core.celery_app import celery_app
from app.models.filemap import FileMap
from app.utils import send_test_email

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(
    msg: schemas.Msg,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.post("/csv-uploader/", status_code=201)
async def csv_uploader(
        csvfile: UploadFile = File(...),
        current_user: models.User = Depends(deps.get_current_active_superuser),
        save_dir: str = settings.DEFAULT_FILE_DIRECTORY,):

    original_filename = csvfile.filename

    filename, file_ext = original_filename.split('.')
    filename = filename.replace('(', '').replace(')', '').replace(' ', '_').replace('?', '').replace('-', '_')
    if file_ext == 'csv':
        # use uuid from db table to save filename, for security!
        # TODO Should this be in upsert on File model
        try:
            filemap = FileMap.get_by_name(filename)
        except Exception as e:
            raise e

        if filemap is None:
            # TODO fix source == NoneType
            source = FileMap.determined_source(name=filename)
            filemap = FileMap.create(name=filename, ext=file_ext, source=source)

        save_path = os.path.join(save_dir, str(filemap.id) + '.' + filemap.ext)
        if not os.path.isfile(save_path):
            # TODO check that file is actually a CSV, use csv.Sniffer
            try:
                fp = open(save_path, 'wb')
                content = await csvfile.read()
                fp.write(content)
                fp.close()
                message = f'Upload complete for {original_filename}. File uploaded by {current_user.full_name}'
            except:
                message = f'Error uploading {original_filename}'
        else:
            message = f'{original_filename} already exists.'
    else:
        message = f'{original_filename} not a CSV, upload cancelled'

    return jsonable_encoder({'message' : message})
