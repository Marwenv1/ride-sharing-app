from sqlalchemy import Column, Enum, Integer, String, DateTime
from app.api.v1.dependencies.db import Base
from app.schemas.ride import RideStatus  

class Ride(Base):
    __tablename__ = 'rides'

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(255))  
    phone_number = Column(String(20))  
    pickup_address = Column(String(255))
    destination_address = Column(String(255))
    pickup_time = Column(DateTime)  
    status = Column(Enum(RideStatus), default=RideStatus.pending)

