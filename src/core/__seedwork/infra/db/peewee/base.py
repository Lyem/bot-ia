from peewee import SqliteDatabase, Model

db = SqliteDatabase('notas.db')

class BaseModel(Model):

    class Meta:
        database = db