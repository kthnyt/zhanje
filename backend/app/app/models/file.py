import logging
from typing import TYPE_CHECKING, Optional
from uuid import uuid4

from app.api import deps
from fastapi import Depends
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Session

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401

# TODO: Move to API ?
class File(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4,)
    name = Column(String, index=True)
    ext = Column(String)
    source = Column(String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO make generic AppBaseModel, with standard methods creat, get
    # TODO is it good practice to add model methods to the model?
    @staticmethod
    def create(name: str, ext: str,source: Optional[str] = None):
        file = File(name=name, ext=ext, source=source)
        # https://stackoverflow.com/questions/64763770/
        # why-we-use-yield-to-get-sessionlocal-in-fastapi-with-sqlalchemy
        # https://github.com/tiangolo/fastapi/issues/2894
        db = next(deps.get_db())
        db.add(file)
        db.commit()
        db.refresh(file)
        return file


    @staticmethod
    def get_by_name(name: str):
        db = next(deps.get_db())
        return db.query(File).filter(File.name == name).first()


    @staticmethod
    def determined_source(name: str):
        source_map  = {'Order_Summary': 'MrDFood'}
        source = None

        for key in source_map.keys():
            if key in name:
                source = source_map[key]

        return source

