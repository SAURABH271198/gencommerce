from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    open_ai_key: str
    
    class Config:
        env_file = ".env"  # Load from .env

settings = Settings()
