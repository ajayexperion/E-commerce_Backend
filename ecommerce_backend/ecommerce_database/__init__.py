from beanie import init_beanie
import motor.motor_asyncio
from ecommerce_database.models import productReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://ajayvs:Aju2nike@workspace.hixkmx6.mongodb.net/sample"
    )
    
    
    await init_beanie(database=client.sample, document_models=[productReview])