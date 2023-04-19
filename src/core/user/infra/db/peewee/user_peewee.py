from peewee import TextField
from core.__seedwork.infra.db.peewee.base import BaseModel

class User(BaseModel):
    name = TextField()
