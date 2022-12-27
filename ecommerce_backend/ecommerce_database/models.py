from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from typing import Optional
from beanie import PydanticObjectId
from bson import ObjectId
class productReview(Document):
    
    name:str
    product:str
    rating:float
    review:str
    date: datetime = datetime.now()

class Products(BaseModel):
    productName:str
    description:str
    amount:int
    rating:float

# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }