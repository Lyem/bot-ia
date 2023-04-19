from core.__seedwork.infra.db.peewee.base import BaseModel
from peewee import TextField, DateTimeField
import datetime


class Clients(BaseModel):
    name = TextField()
    cell = TextField()
    cep = TextField()
    home_number = TextField()
    cpf = TextField()
    chat = TextField()
    last_chat = DateTimeField(default=datetime.datetime.now)
