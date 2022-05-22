from peewee import *

# user = 'root'
# password = 'root'
db_name = 'H_and_M'

conn = MySQLDatabase(
    db_name,
    # user=user,
    # password=password,
    host='localhost'
)

class BaseModel(Model):
    class Meta:
        database = conn