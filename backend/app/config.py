from pydantic_settings import BaseSettings
from typing import List, Optional
import os 

class Settings(BaseSettings):
    
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Facial Enhancement Visualizer"
    
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    SECRET_KEY: str = "secret"
    
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 1024 * 1024 * 10
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png"]
    
    MODEL_SErVER_URL: str = "http://localhost:8001"
    
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        
settings = Settings()
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)