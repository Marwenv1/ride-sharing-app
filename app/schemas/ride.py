from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum
import re

class RideStatus(str, Enum):
    pending = 'pending'
    active = 'active'
    completed = 'completed'
    cancelled = 'cancelled'

class RideBase(BaseModel):
    client_name: str = Field(..., example="John Doe", description="The full name of the client.")
    phone_number: str = Field(..., example="+31612345678", description="The contact phone number of the client.")
    pickup_address: str = Field(..., example="100 Main St, Amsterdam", description="The pickup location for the ride.")
    destination_address: str = Field(..., example="200 Main St, Amsterdam", description="The destination location for the ride.")

class RideCreate(RideBase):
    pickup_time: Optional[datetime] = Field(default=None, example="2024-01-01T08:00:00Z", description="The scheduled pickup time for the ride.")

    @validator('phone_number')
    def validate_phone_number(cls, v):
        pattern = r'^\+31[1-9][0-9]{8}$'  # Regex pattern for Dutch phone numbers
        if not re.match(pattern, v):
            raise ValueError('Phone number must be a valid Dutch number starting with +31')
        return v

class Ride(RideBase):
    id: int = Field(..., example=1, description="The unique id of the ride.")
    pickup_time: datetime = Field(..., example="2023-01-01T08:00:00Z", description="The confirmed pickup time for the ride.")
    status: RideStatus = Field(..., example=RideStatus.pending, description="The current status of the ride.")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "client_name": "John Doe",
                "phone_number": "+31612345678",
                "pickup_address": "100 Main St, Amsterdam",
                "destination_address": "200 Main St, Amsterdam",
                "pickup_time": "2023-01-01T08:00:00Z",
                "status": RideStatus.pending
            }
        }

class RideUpdate(BaseModel):
    client_name: Optional[str] = Field(None, example="John Doe", description="The full name of the client.")
    phone_number: Optional[str] = Field(None, example="+31612345678", description="The contact phone number of the client.")
    pickup_address: Optional[str] = Field(None, example="100 Main St, Amsterdam", description="The pickup location for the ride.")
    destination_address: Optional[str] = Field(None, example="200 Main St, Amsterdam", description="The destination location for the ride.")
    pickup_time: Optional[datetime] = Field(None, example="2023-01-01T08:00:00Z", description="The scheduled pickup time for the ride.")
    status: Optional[RideStatus] = Field(None, example=RideStatus.pending, description="The current status of the ride.")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "client_name": "Jane Doe",
                "phone_number": "+31687654321",
                "pickup_address": "300 Main St, Amsterdam",
                "destination_address": "400 Main St, Amsterdam",
                "pickup_time": "2023-01-02T09:00:00Z",
                "status": RideStatus.active
            }
        }