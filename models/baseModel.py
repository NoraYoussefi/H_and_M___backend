from unicodedata import category
from peewee import *
from database import conn




# A BaseModel that will be responsible for associating models with MySQL DB

class BaseModel(Model):
    class Meta:
        database = conn


