from beanie import init_beanie
import motor.motor_asyncio
from ecommerce_database.models import productReview
from config import settings
from pydantic import BaseModel


async def init_db():
    
    username=settings.username
    password=settings.password
    hostname=settings.hostname
    databasename=settings.databasename

    connection=f"mongodb+srv://ajayvs:{password}@{hostname}/{databasename}"
  
    client = motor.motor_asyncio.AsyncIOMotorClient(
        
        connection
    )
    await init_beanie(database=client.sample, document_models=[productReview])
    
# connection=mongodb+srv://ajayvs:Aju2nike@workspace.hixkmx6.mongodb.net/sample