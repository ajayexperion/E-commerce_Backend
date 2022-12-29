from pydantic import BaseModel

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


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}
