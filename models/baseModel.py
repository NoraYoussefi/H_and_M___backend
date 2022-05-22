from unicodedata import category
from peewee import *
from database import conn
from pydantic.utils import GetterDict
from typing import Any
import peewee



# A BaseModel that will be responsible for associating models with MySQL DB

class BaseModel(Model):
    class Meta:
        database = conn


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