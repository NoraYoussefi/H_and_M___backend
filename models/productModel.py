from mongoengine import Document,StringField
from typing import List, Optional
from uuid import UUID, uuid4
# from pydantic import BaseModel
from enum import Enum
from peewee import *
from database import conn
from .baseModel import BaseModel
from pydantic.utils import GetterDict
from typing import Any
import peewee

# A BaseModel that will be responsible for associating models with MySQL DB
# class BaseModel(Model):
#     class Meta:
#         database = conn

# class category(str,Enum):
#     male = "male"
#     female = "female"
#     kids = "kids"

class Product(BaseModel):
    # id: Optional[UUID]=uuid4()
    name: CharField(max_length=100)
    category: Optional[str]
    class Meta:
        db_table = 'products'

async def create_product(name: str, category: str):
    product_object = Product(
        name=name,
        category=category
       
    )
    product_object.save()
    return product_object


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class ProductModel(BaseModel):
    id:int
    name:str
    category:str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        
# class ProductUpdateRequest(BaseModel):
#     name:Optional[str]
#     category: Optional[str]

# class Product(BaseModel):
#     id: Optional[UUID]=uuid4()
#     name: str
#     category: Optional[str]

# class ProductUpdateRequest(BaseModel):
#     name:Optional[str]
#     category: Optional[List[category]]

