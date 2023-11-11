from typing import List
from pydantic import BaseSettings ,Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field("mysql+mysqlconnector://root:@localhost/ride-sharing", env="DATABASE_URL")
    ALLOWED_ORIGINS: list = Field(
        default=["http://localhost:3000"],
        env="ALLOWED_ORIGINS"
    )
    class Config:
        env_file = ".env"

settings = Settings()
