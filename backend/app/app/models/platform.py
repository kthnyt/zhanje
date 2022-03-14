import uuid

from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base
from app.db.auditmixin import AuditMixin
from sqlalchemy.dialects.postgresql import UUID


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, nullable=False, server_default='TRUE')
