from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.v1.dependencies.db import get_db
from app.main import app  
from app.api.v1.dependencies.db import Base 
from app.core.config import settings 

DATABASE_URL = settings.TEST_DATABASE_URL  # Define a test database URL in your settings
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)  # Create tables for the test database

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_ride():
    response = client.post(
        "/api/v1/rides/",
        json={
            "client_name": "Test Client",
            "phone_number": "+31612345678",
            "pickup_address": "100 Test St",
            "destination_address": "200 Test St",
            "pickup_time": "2023-01-01T08:00:00Z",
        },
    )
    assert response.status_code == 201
    assert response.json()["client_name"] == "Test Client"

def test_read_ride():
    response = client.get("/api/v1/rides/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

