from pydantic import BaseSettings


class Settings(BaseSettings):
    # connection:str
    username:str
    password:str
    hostname:str
    databasename:str

    class Config:
        env_file = ".env"
settings = Settings()