from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models import ride as models
from app.schemas import ride as schemas

def create_ride(db: Session, ride: schemas.RideCreate):
    try:
        db_ride = models.Ride(**ride.dict()) 
        db.add(db_ride)
        db.commit()
        db.refresh(db_ride)
        return db_ride
    except SQLAlchemyError:
        db.rollback()
        raise  # Re-raises the caught exception

def get_ride(db: Session, ride_id: int):
    try:
        return db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    except SQLAlchemyError:
        raise  # Re-raises the caught exception

def get_rides(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Ride).offset(skip).limit(limit).all()
    except SQLAlchemyError:
        raise  # Re-raises the caught exception

def update_ride(db: Session, ride_id: int, ride_update: schemas.RideUpdate):
    try:
        db_ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
        if db_ride:
            update_data = ride_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_ride, key, value)
            db.commit()
            return db_ride
    except SQLAlchemyError:
        db.rollback()
        raise  # Re-raises the caught exception

def delete_ride(db: Session, ride_id: int):
    try:
        db_ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
        if db_ride:
            db.delete(db_ride)
            db.commit()
            return True
    except SQLAlchemyError:
        db.rollback()
        raise  # Re-raises the caught exception
