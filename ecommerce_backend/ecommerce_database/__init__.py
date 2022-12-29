from beanie import init_beanie
import motor.motor_asyncio
from ecommerce_database.models import productReview
from config import settings
from pydantic import BaseModel


async def init_db():
    connection=settings.connection
    client = motor.motor_asyncio.AsyncIOMotorClient(
        connection
    )
    await init_beanie(database=client.sample, document_models=[productReview])
    
