from typing import Any, List

from app import models, crud, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter()

@router.get("/", response_model=List[schemas.Platform])
def read_platforms(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve platforms.
    """
    platforms = crud.platform.get_multi(db=db, skip=skip, limit=limit)

    if not platforms:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Platforms not found")

    return platforms


@router.post("/", response_model=schemas.Platform)
def create_platform(
    *,
    db: Session = Depends(deps.get_db),
    platform_in: schemas.PlatformCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new platform.
    """
    platform = crud.platform.create(db=db, obj_in=platform_in)
    return platform
