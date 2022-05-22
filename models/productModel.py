from mongoengine import Document,StringField
from typing import List, Optional
from uuid import UUID, uuid4
# from pydantic import BaseModel
from enum import Enum
from peewee import *
from database import conn
from .baseModel import BaseModel

# A BaseModel that will be responsible for associating models with MySQL DB
# class BaseModel(Model):
#     class Meta:
#         database = conn

class category(str,Enum):
    male = "male"
    female = "female"
    kids = "kids"

class Product(BaseModel):
    # id: Optional[UUID]=uuid4()
    name: CharField(max_length=100)
    category: Optional[str]
    class Meta:
        db_table = 'products'

class ProductUpdateRequest(BaseModel):
    name:Optional[str]
    category: Optional[List[category]]

# class Product(BaseModel):
#     id: Optional[UUID]=uuid4()
#     name: str
#     category: Optional[str]

# class ProductUpdateRequest(BaseModel):
#     name:Optional[str]
#     category: Optional[List[category]]

