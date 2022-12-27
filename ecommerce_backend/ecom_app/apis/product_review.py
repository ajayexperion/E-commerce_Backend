from beanie import PydanticObjectId
from fastapi import APIRouter
from typing import List
from bson import ObjectId
from ecommerce_database.models import productReview

router=APIRouter()

@router.post('/', response_description="Review added to the database")
async def add_product(review: productReview)->dict:
    await review.create()
    return{'message':'Review added succesfully'}        


