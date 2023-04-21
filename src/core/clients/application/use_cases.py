import datetime
from core.__seedwork.application.use_cases import UseCase
from core.clients.infra.db.peewee.clients_repository import ClientRepository


class ClientLogged(UseCase):

    def execute(self, chatId: str) -> bool:
        repository = ClientRepository()
        client = repository.find_by_chat(chatId)
        now = datetime.datetime.now()
        if (client):
            diff = now - client.last_chat
            if(diff.days >= 1):
                return False
            return True
        else:
            return False


class ClientExist(UseCase):

    def execute(self, cpf: str, chat_id) -> bool:
        repository = ClientRepository()
        client = repository.find_by_cpf(cpf)
        if (client):
            repository.update(cpf, chat_id)
            return True
        else:
            return False


class ClientCreate(UseCase):
    
    def execute(self, name, cell, cep, home_number, chat, cpf):
        repository = ClientRepository()
        repository.create(name, cell, cep, home_number, chat, cpf)
