import datetime

class ClientRepository():
    def __init__(self) -> None:
        from .clients_model import Clients
        Clients.create_table()
        self.client = Clients

    def create(self, name, cell, cep, home_number, chat, cpf):
        self.client.create(name=name, cell=cell, cep=cep,
                           home_number=home_number, chat=chat, cpf=cpf)
    
    def update(self, cpf, chat):
        client = self.client.select().where(self.client.cpf == cpf).get()
        client.chat = chat
        client.last_chat = datetime.datetime.now()
        client.save()

    def find_by_chat(self, chat):
        try:
            return self.client.select().where(self.client.chat == chat).get()
        except self.client.DoesNotExist:
            return None

    def find_by_cpf(self, cpf):
        try:
            return self.client.select().where(self.client.cpf == cpf).get()
        except self.client.DoesNotExist:
            return None
