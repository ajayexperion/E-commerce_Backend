from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from typing import Optional
from beanie import PydanticObjectId

class productReview(Document):
    
    name:str
    product:str
    rating:float
    review:str
    date: datetime = datetime.now()