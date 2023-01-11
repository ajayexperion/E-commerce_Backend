
from ecommerce_database.models import productReview
from ecom_app.apis. product_model import Products
from typing import List


async def add_product_data(review: Products) -> dict:
    """Function to  Add product"""

    pro = productReview(
        productImage=review.productImage,
        productName=review.productName,
        description=review.description,
        amount=review.amount,
        rating=review.rating
    )
    await pro.create()

# Function to get product Details


async def get_products_details():
    reviews = await productReview.find_all().to_list()
    return reviews


# async def get_filter_products(productName, minAmount, maxAmount, sortAmount):
#     """Function to filter"""

#     if (minAmount) and (maxAmount) and (productName) and (sortAmount):
#         reviews = await productReview.find(
#             {"productName": productName,
#              "amount": {"$gte": minAmount, "$lte": maxAmount}}
#         ).sort([("amount", sortAmount)]).to_list()

#     elif (minAmount) and (maxAmount) and (productName):
#         reviews = await productReview.find({"productName": productName,
#                                             "amount": {"$gte": minAmount, "$lte": maxAmount}}
#                                            ).to_list()

#     elif (productName) and (sortAmount):
#         reviews = await productReview.find({"productName": productName}
#                                            ).sort([("amount", sortAmount)]).to_list()

#     elif productName:
#         reviews = await productReview.find({"productName": productName}).to_list()

#     elif minAmount and maxAmount:
#         reviews = await productReview.find({"amount": {"$gte": minAmount, "$lte": maxAmount}}).to_list()

#     elif sortAmount:
#         reviews = await productReview.find().sort([("amount", sortAmount)]).to_list()

#     else:
#         reviews = await productReview.find_all().to_list()
#     return reviews



# async def get_filter_products(productName, minAmount, maxAmount, sortAmount):
#     """Function to filter"""

#     query = []

#     if productName:
#         query.append({"productName": productName})

#     if minAmount and maxAmount:
#         query.append({"amount": {"$gte": minAmount, "$lte": maxAmount}})

#     if sortAmount:
#         sort = [("amount", sortAmount)]
#     else:
#         sort = []

#     if len(query) > 1:
#         reviews = await productReview.find({"$and": query}).sort(sort).to_list()
#     elif query:
#         reviews = await productReview.find(query[0]).sort(sort).to_list()
#     else:
#         reviews = await productReview.find().sort(sort).to_list()

#     return reviews


async def get_filter_products(productName, minAmount, maxAmount, sortAmount):
    """Function to filter and sort products"""
    query = {}
    if productName:
        query["productName"] = productName
    if minAmount and maxAmount:
        query["amount"] = {"$gte": minAmount, "$lte": maxAmount}
    sort = []
    if sortAmount:
        sort = [("amount",sortAmount)]

    reviews = await productReview.find(query).sort(sort).to_list()
    return reviews

