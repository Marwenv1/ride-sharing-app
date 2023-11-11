# app/api/v1/endpoints/ride.py
from fastapi import APIRouter, Depends ,status
from sqlalchemy.orm import Session
from app.api.v1.dependencies.db import get_db
from app.schemas import ride as schemas
from app.api.v1.utils import exceptions
from app.services import ride_services as services
from typing import List

app = APIRouter()

from fastapi import HTTPException

@app.post("/rides/", response_model=schemas.Ride, status_code=status.HTTP_201_CREATED)
def create_ride(ride: schemas.RideCreate, db: Session = Depends(get_db)):
    service = services.RideService(db)
    try:
        return service.create_ride(ride)
    except exceptions.RideScheduleException as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/rides/{ride_id}", response_model=schemas.Ride)
def read_ride(ride_id: int, db: Session = Depends(get_db)):
    service = services.RideService(db)
    try:
        return service.get_ride(ride_id)
    except exceptions.RideScheduleException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/rides/", response_model=List[schemas.Ride])
def read_rides(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = services.RideService(db)
    return service.get_all_rides(skip, limit)

@app.put("/rides/{ride_id}", response_model=schemas.Ride)
def update_ride(ride_id: int, ride_update: schemas.RideUpdate, db: Session = Depends(get_db)):
    service = services.RideService(db)
    try:
        return service.update_ride(ride_id, ride_update)
    except exceptions.RideScheduleException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/rides/{ride_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ride(ride_id: int, db: Session = Depends(get_db)):
    service = services.RideService(db)
    try:
        service.delete_ride(ride_id)
        return {"message": "Ride deleted successfully"}
    except exceptions.RideScheduleException as e:
        raise HTTPException(status_code=404, detail=str(e))