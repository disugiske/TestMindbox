import random
from faker import Faker
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy import select
from models import Products, Category
from models.db_config import async_session
from routers.products_cat import router as prod_cat_router

fake = Faker()
app = FastAPI()

app.include_router(prod_cat_router)


@app.get("/add", response_class=JSONResponse)
async def index(request: Request, cat: int = 0, prod: int = 0):
    if cat == 0 and prod == 0:
        return JSONResponse("please add arguments like: /add?cat=5&prod=10")
    async with async_session() as session:
        for i in fake.words(cat):
            session.add(Category(name=i))
        for i in fake.words(prod):
            session.add(Products(name=i))
        prod = await session.execute(select(Products))
        prod = prod.scalars().all()
        cat = await session.execute(select(Category))
        cat_res = cat.scalars().all()
        for i in prod:
            i.category.append(cat_res[random.randrange(0, len(cat_res))])
        await session.commit()
    return JSONResponse({"append": "OK"})
