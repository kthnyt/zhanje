import uuid

from app.db.base_class import Base
from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID


class AuditMixin(Base):
    id = Column(UUID, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
