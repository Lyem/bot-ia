class ClientRepository():
    def __init__(self) -> None:
        from .clients_model import Clients
        Clients.create_table()
        self.client = Clients

    def create(self, name, cell, cep, home_number, chat, cpf):
        self.client.create(name=name, cell=cell, cep=cep,
                           home_number=home_number, chat=chat, cpf=cpf)

    def find_by_chat(self, chat):
        return self.client.select().where(self.client.chat == chat).get()

    def find_by_cpf(self, cpf):
        return self.client.select().where(self.client.cpf == cpf).get()
