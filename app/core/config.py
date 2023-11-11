from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
print(f"Database URL: {settings.DATABASE_URL}")