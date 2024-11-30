from pydantic import BaseSettings

class Settings(BaseSettings):
    schema_path: str = "schema.json"
    # Add other settings as needed

    class Config:
        env_file = ".env"

settings = Settings()