from sqlalchemy import Column, ForeignKey, String, Float, text, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class LoyverseOrder(Base):
    __tablename__ = "loyverse_orders"

    id = Column(UUID, server_default=text("uuid_generate_v4()"), primary_key=True)
    date = Column(DateTime(timezone=True))
    receipt_number = Column(String, unique=True)
    category = Column(String)
    sku = Column(Integer)
    item = Column(String)
    quantity = Column(Integer)
    gross_sales = Column(Float)
    pos = Column(String)
    store = Column(String)
    cashier_name = Column(String)
    status = Column(String)

    platform_id = Column(UUID, ForeignKey("platforms.id"))
