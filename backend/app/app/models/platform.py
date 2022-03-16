import uuid

from sqlalchemy import Column, String, Boolean

from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, nullable=False, server_default='TRUE')

    mrd_orders = relationship("MrDOrder", backref="mrd_order", lazy='select')
    uber_orders = relationship("UberOrder", backref="uber_order", lazy='select')
    loyverse_orders = relationship("LoyverseOrder", backref="loyverse_order", lazy='select')
