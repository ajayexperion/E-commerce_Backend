from pydantic import BaseSettings


class Settings(BaseSettings):
    connection: str
    class Config:
        env_file = ".env"
settings = Settings()