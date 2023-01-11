import logging
from logging.config import dictConfig
from fastapi import APIRouter, Depends
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products, ResponseModel, ResponseList
from ecommerce.product import add_product_data, get_products_details, get_filter_products
from typing import List
from fastapi import Header
from conf_logger import logging
# import logging
# FORMAT = "%(levelname)s:%(message)s"
# logging.basicConfig(format=FORMAT, level=logging.DEBUG)


router = APIRouter()


# API to add product
@router.post('/addproduct', response_description="Review added to the database")
async def add_product(review: Products):
    """"create a function to add product details to database"""

    logging.debug("Program to add product  starts")

    

    await add_product_data(review)
    return {"message": "Review added succesfull"}
    # return{"productImage":ResponseModel.productImage,"productName":ResponseModel.productName,"description":ResponseModel.description,"amount":ResponseModel.amount,"ratiing":ResponseModel.rating}


# Api to filter product from database
@router.get("/product/", response_description="Review records retrieved",
            response_model=ResponseList)
async def get_product(productName: str = None, minAmount: int = None,
                      maxAmount: int = None, sortAmount: int = None) -> Products:
    """create a function to filter product by name and min and max amount"""

    logging.debug("Program to filter product  starts")
    

    reviews = await get_filter_products(productName, minAmount, maxAmount, sortAmount)
    return {"data": reviews}
