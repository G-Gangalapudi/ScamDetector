from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Scam Intelligence"
    debug: bool = False

settings = Settings()
