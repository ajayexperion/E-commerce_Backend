from datetime import datetime
from beanie import Document
from pydantic import BaseModel,Field
from typing import Optional
from beanie import PydanticObjectId
from bson import ObjectId
from ecom_app.apis.product_model import Products

class productReview(Document):
    productImage:str  
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


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}