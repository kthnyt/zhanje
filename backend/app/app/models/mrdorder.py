from sqlalchemy import Column, ForeignKey, String, Float, Date, Time
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class MrDOrder(Base):
    __tablename__ = "mrdorders"

    id = Column(UUID, primary_key=True, index=True)
    invoice_number = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    restaurant = Column(String)
    suburb = Column(String)
    prep_time_minutes = Column(Float)
    order_type = Column(String)
    food_total = Column(Float, nullable=False)
    commission_ex_vat_per = Column(Float)
    due_to_you = Column(Float, nullable=False)
    restaurant_status = Column(String)

    platform_id = Column(UUID, ForeignKey("platforms.id"))



