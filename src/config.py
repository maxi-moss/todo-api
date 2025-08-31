"""Centralized configuration management using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List, Optional


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    

class CORSConfig(BaseAppSettings):
    """CORS configuration."""
    allowed_origins: str = Field("http://localhost:5173", alias="CORS_ALLOWED_ORIGINS")
    allow_credentials: str = Field("true", alias="CORS_ALLOW_CREDENTIALS")
    allowed_methods: str = Field("GET,POST,PUT,DELETE,OPTIONS", alias="CORS_ALLOWED_METHODS")
    allowed_headers: str = Field("*", alias="CORS_ALLOWED_HEADERS")
    
    @property
    def allowed_origins_list(self) -> List[str]:
        return self.allowed_origins.split(",")
    
    @property
    def allow_credentials_bool(self) -> bool:
        return self.allow_credentials.lower() == "true"
    
    @property
    def allowed_methods_list(self) -> List[str]:
        return self.allowed_methods.split(",")
    
    @property
    def allowed_headers_list(self) -> List[str]:
        return self.allowed_headers.split(",")


class SupabaseConfig(BaseAppSettings):
    """API keys configuration."""
    url: Optional[str] = Field(None, alias="SUPABASE_PROJECT_URL")
    key: Optional[str] = Field(None, alias="SUPABASE_SERVICE_KEY")


class Settings(BaseAppSettings):
    """Main application settings."""
    cors: CORSConfig = CORSConfig()
    supabase: SupabaseConfig = SupabaseConfig()
    

# Settings Singleton
settings = Settings()