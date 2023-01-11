from pydantic import BaseModel
from typing import List,Optional
class Products(BaseModel):
    productImage:str  
    productName:str
    description:str
    amount:int
    rating:float

class ResponseModel(BaseModel):
   productImage:str
   productName:str
   description:str
   amount:int
   rating:float
class ResponseList(BaseModel):
    data: Optional[List[ResponseModel]]


        
    


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}
