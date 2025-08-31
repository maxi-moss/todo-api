from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import Optional, List



class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


class SupabaseConfig(BaseAppSettings):
    """API keys configuration."""
    url: Optional[str] = Field(None, alias="SUPABASE_PROJECT_URL")
    key: Optional[str] = Field(None, alias="SUPABASE_SERVICE_KEY")


class Settings(BaseAppSettings):
    """Main application settings."""
    supabase: SupabaseConfig = SupabaseConfig()
    
# Settings Singleton
settings = Settings()