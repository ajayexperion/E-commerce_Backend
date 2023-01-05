import logging
from logging.config import dictConfig
from fastapi import APIRouter,Depends
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products,ResponseModel
from ecommerce.product import add_product_data,get_products_details,get_filter_products
from typing import List
from fastapi import  Header

import logging
FORMAT = "%(levelname)s:%(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)


router=APIRouter()



# API to add product
@router.post('/addproduct', response_description="Review added to the database")
async def add_product(review:Products):

    logging.debug("Program to add product  starts")

    """"create a function to add product details to database"""

    

    await add_product_data(review)
    return {"message":"Review added succesfull"}
         

# Api to filter product from database
@router.get("/product/", response_description="Review records retrieved")
async def get_product(productName:str=None,minAmount:int=None,
maxAmount:int=None,sortAmount:int=None)->Products:

    logging.debug("Program to filter product  starts")
    """create a function to filter product by name and min and max amount"""

    reviews=await get_filter_products(productName,minAmount,maxAmount,sortAmount)
    return reviews

    
      

