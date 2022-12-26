from fastapi import FastAPI
from ecommerce_database import init_db

from ecom_app.apis.product_review import router as Router

app=FastAPI()


app.include_router(Router,tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}   