from sqlalchemy.orm import Session
from app.crud import crud_ride as crud
from app.schemas import ride as schemas
from app.api.v1.utils import exceptions
from datetime import datetime, timezone

class RideService:
    def __init__(self, db: Session):
        self.db = db

    def create_ride(self, ride: schemas.RideCreate):
        self._validate_ride_time(ride.pickup_time)
        return crud.create_ride(self.db, ride)

    def get_ride(self, ride_id: int):
        ride = crud.get_ride(self.db, ride_id)
        if not ride:
            raise exceptions.RideScheduleException("Ride not found.")
        return ride

    def get_all_rides(self, skip: int, limit: int):
        return crud.get_rides(self.db, skip, limit)

    def update_ride(self, ride_id: int, ride_update: schemas.RideUpdate):
        existing_ride = crud.get_ride(self.db, ride_id)
        if not existing_ride:
            raise exceptions.RideScheduleException("Ride not found for updating.")
        
        if ride_update.pickup_time:
            self._validate_ride_time(ride_update.pickup_time)
        
        return crud.update_ride(self.db, ride_id, ride_update)

    def delete_ride(self, ride_id: int):
        if not crud.delete_ride(self.db, ride_id):
            raise exceptions.RideScheduleException("Unable to delete the ride or ride not found.")
        return {"message": "Ride deleted successfully"}

    def _validate_ride_time(self, pickup_time):
        if pickup_time and pickup_time < datetime.now(timezone.utc):
            raise ValueError("Pickup time cannot be in the past")

