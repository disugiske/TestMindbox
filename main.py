import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy import select

from models import Products
from models.bd_config import async_session
from routers.products_cat import router as prod_cat_router


app = FastAPI()

app.include_router(prod_cat_router)

@app.get("/", response_class=JSONResponse)
async def index(request: Request,):
    async with async_session() as session:
        products_data = await session.execute(select(Products))
        all_tables = products_data.scalars().all()
    return {"products": json.dumps(all_tables)}