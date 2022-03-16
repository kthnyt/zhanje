from sqlalchemy import Column, ForeignKey, String, Float, Date, Time, text
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base

class UberOrder(Base):
    __tablename__ = 'uberorders'

    id = Column(UUID, server_default=text("uuid_generate_v4()"), primary_key=True)
    order_id = Column(String)
    store_name = Column(String)
    order_or_refund_date = Column(Date)
    order_accept_time = Column(Time)
    food_sales_excl_vat = Column(Float)
    food_sales_incl_vat = Column(Float)
    delivery_fee_incl_vat = Column(Float)
    total_order_incl_vat = Column(Float)
    cost_of_delivery_incl_vat = Column(Float)
    gratuity = Column(Float)
    payout = Column(Float)
    payout_date = Column(Date)
    order_status = Column(String)

    platform_id = Column(UUID, ForeignKey("platforms.id"))
