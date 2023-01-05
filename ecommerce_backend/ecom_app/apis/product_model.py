from pydantic import BaseModel

class Products(BaseModel):
    productImage:str  
    productName:str
    description:str
    amount:int
    rating:float

class ResponseModel(BaseModel):
   
   productName:str
   description:str
   amount:int
   rating:float
        
    


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}
