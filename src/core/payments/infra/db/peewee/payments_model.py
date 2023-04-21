from core.__seedwork.infra.db.peewee.base import BaseModel
from peewee import TextField, DateTimeField, FloatField, ForeignKeyField, BooleanField
from core.clients.infra.db.peewee.clients_model import Clients
import datetime
from datetime import timedelta

def get_seven_days():
    return datetime.datetime.now() + timedelta(days=7)

class Payments(BaseModel):
    name = TextField()
    price = FloatField()
    create_at = DateTimeField(default=datetime.datetime.now)
    payment_date = DateTimeField(default=get_seven_days)
    is_pay = BooleanField(default=False)
    client = ForeignKeyField(Clients, backref='clients')
