from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.platform import Platform
from app.schemas.platform import PlatformCreate, PlatformUpdate


class CRUDPlatform(CRUDBase[Platform, PlatformCreate, PlatformUpdate]):
    def get_by_name(self, db: Session, *,  name: str) -> Optional[Platform]:
        return db.query(Platform).filter(Platform.name == name).first()

    def create(self, db: Session, *, obj_in: PlatformCreate) -> Platform:
        db_obj = Platform(
            name=obj_in.name,
            description=obj_in.description,
            is_active=obj_in.is_active,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Platform, obj_in: Union[PlatformUpdate, Dict[str, Any]]
    ) -> Platform:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_active(self, platform: Platform) -> bool:
        return platform.is_active

platform = CRUDPlatform(Platform)
