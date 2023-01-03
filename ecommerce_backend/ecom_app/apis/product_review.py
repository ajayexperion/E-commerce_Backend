from beanie import PydanticObjectId
from fastapi import APIRouter,Depends
from bson import ObjectId
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products,ResponseModel
from ecommerce.product import add_product_data,get_products_details,get_filter_products
from typing import List
from fastapi import  Header
router=APIRouter()


# API to add product
@router.post('/addproduct', response_description="Review added to the database")
async def add_product(review:Products):
    await add_product_data(review)
    return {"message":"Review added succesfull"}
         
# API to get product details
# @router.get("/productlist",response_description="Review records retrieved")
# async def get_products():
#     reviews:list= await get_products_details()
#     print(reviews)
#     return reviews
      
# API to filter product 

# async def get_header_values(productName: str = Depends(Header()), minAmount: str = Depends(Header())):
#     print(productName)
#     return productName,minAmount

@router.get("/product/", response_description="Review records retrieved")

async def get_product(minAmount:int=Header(default=None),maxAmount:int=Header(default=None),productName:str=Header(default=None))->Products:
    
    reviews=await get_filter_products(productName,minAmount,maxAmount)
    return reviews

    
      

