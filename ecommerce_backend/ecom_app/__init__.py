from fastapi import FastAPI
from ecommerce_database import init_db
from fastapi.middleware.cors import CORSMiddleware

from ecom_app.apis.product_review import router as Router

app=FastAPI()

origins=['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)


app.include_router(Router,tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}   