from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

# Shared properties
class PlatformBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True


# Properties to receive via API on creation
class PlatformCreate(PlatformBase):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True


# Properties to receive via API on update
class PlatformUpdate(PlatformBase):
    pass


class PlatformInDBBase(PlatformBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Platform(PlatformInDBBase):
    pass


# Additional properties stored in DB
class PlatformInDB(PlatformInDBBase):
    pass
