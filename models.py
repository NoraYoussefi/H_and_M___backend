from mongoengine import Document,StringField
from typing import List, Optional
from uuid import UUID, uuid4
# from pydantic import BaseModel
from enum import Enum

class category(str,Enum):
    male = "male"
    female = "female"
    kids = "kids"

class Product(Document):
    # id: Optional[UUID]=uuid4()
    name: StringField(max_length=100)
    category: Optional[str]

class ProductUpdateRequest(Document):
    name:Optional[str]
    category: Optional[List[category]]

# class Product(BaseModel):
#     id: Optional[UUID]=uuid4()
#     name: str
#     category: Optional[str]

# class ProductUpdateRequest(BaseModel):
#     name:Optional[str]
#     category: Optional[List[category]]