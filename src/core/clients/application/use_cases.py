from core.__seedwork.application.use_cases import UseCase
from core.clients.infra.db.peewee.clients_repository import ClientRepository


class ClientLogged(UseCase):

    def execute(self, chatId: str) -> bool:
        repository = ClientRepository()
        if (repository.find_by_chat(chatId)):
            return True
        else:
            return False


class ClientExist(UseCase):

    def execute(self, cpf: str) -> bool:
        repository = ClientRepository()
        if (repository.find_by_cpf(cpf)):
            return True
        else:
            return False


class ClientCreate(UseCase):
    
    def execute(self, name, cell, cep, home_number, chat, cpf):
        repository = ClientRepository()
        repository.create(name, cell, cep, home_number, chat, cpf)
        return 'a'
