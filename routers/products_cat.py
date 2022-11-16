from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy import select

from models import Products, Category
from models.bd_config import async_session

router = APIRouter(prefix="/v1")

@router.get("/all", response_class=JSONResponse)
async def all_prod(request: Request):
    async with async_session() as session:
        products_data = await session.execute(select(Products))
        all_tables = products_data.scalars().all()
    return {"products": all_tables}


@router.get("/category", response_class=JSONResponse)
async def all_prod(request: Request):
    async with async_session() as session:
        products_data = await session.execute(select(Category))
        all_tables = products_data.scalars().all()
    return {"category": all_tables}

@router.get("/pair", response_class=JSONResponse)
async def all_prod(request: Request):
    result = []
    async with async_session() as session:
        products_data = await session.execute(select(Products))
        all_tables = products_data.scalars().all()
    for product in all_tables:
        for category in product.category:
            result.append({product.name: category.name})
    return {"pairs": result}