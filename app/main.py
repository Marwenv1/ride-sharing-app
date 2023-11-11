from dotenv import load_dotenv
from app.core.config import settings
from fastapi import FastAPI
from app.api.v1.endpoints import ride as ride_endpoint
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(ride_endpoint.app, prefix="/api/v1/rides", tags=["rides"])
    return app

app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)