import random
import string
import time

from faker import Faker
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy import select
from models import Products, Category
from models.db_config import async_session
from routers.products_cat import router as prod_cat_router
from config_log.logger_config import logger

fake = Faker()
app = FastAPI()

app.include_router(prod_cat_router)


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#     logger.info(f"rid={idem} start request path={request.url.path}")
#     start_time = time.time()
#
#     response = await call_next(request)
#
#     process_time = (time.time() - start_time) * 1000
#     formatted_process_time = '{0:.2f}'.format(process_time)
#     logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
#
#     return response


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
