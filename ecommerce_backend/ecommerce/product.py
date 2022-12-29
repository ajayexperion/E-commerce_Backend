
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products
from typing import List

# Function to  Add product
async def add_product_data(review:Products)->dict: 
    pro=productReview(
        productName= review.productName,
        description=review.description,
        amount=review.amount,
        rating=review.rating
        )
    await pro.create()
    
# Function to get product Details
async def get_products_details():
    reviews = await productReview.find_all().to_list()
    return reviews

# Function to filter
async def get_filter_products(productName):
    reviews=  await productReview.find(productReview.productName==productName).to_list()
    return reviews