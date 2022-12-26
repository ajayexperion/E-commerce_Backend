from beanie import init_beanie
import motor.motor_asyncio
from ecommerce_database.models import productReview
from dotenv import load_dotenv
import os
# from conf import connection

def configure():
    load_dotenv()

async def init_db():
    configure()
    connection=os.getenv('connection')
    client = motor.motor_asyncio.AsyncIOMotorClient(
        connection
    )
    
    
    await init_beanie(database=client.sample, document_models=[productReview])