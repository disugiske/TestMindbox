from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.bd_config import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("products_id", ForeignKey("products.id"), primary_key=True),
    Column("category_id", ForeignKey("category.id"), primary_key=True),
)


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = relationship("Category", secondary=association_table, back_populates="products", lazy='subquery')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Products", secondary=association_table, back_populates="category", lazy='subquery')
