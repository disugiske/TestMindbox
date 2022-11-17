import os

from dotenv import load_dotenv
from sqlalchemy.orm import (
    declarative_base, sessionmaker,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

load_dotenv()
SQLALCHEMY_DB_URI = os.getenv('SQLALCHEMY_DB_URI')

engine = create_async_engine(
    url=os.getenv('SQLALCHEMY_DB_URI'),
    echo=False
)
Base = declarative_base(bind=engine)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
