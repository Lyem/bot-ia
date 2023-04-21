from core.__seedwork.application.use_cases import UseCase
from core.clients.infra.db.peewee.clients_repository import ClientRepository
from core.payments.infra.db.peewee.payments_repository import PaymentRepository


class CreatePayment(UseCase):

    def execute(self, chatId: str, plan: str):
        payment_repository = PaymentRepository()
        client_repository = ClientRepository()
        client = client_repository.find_by_chat(chatId)
        if plan == '200':
            price = 20
        elif plan == '400':
            price = 50
        else:
            price = 99
        payment_repository.create(client, price, f'{plan}Mb')

class GetAllByClient(UseCase):
    def execute(self, chat_id):
        payment_repository = PaymentRepository()
        client_repository = ClientRepository()
        client = client_repository.find_by_chat(chat_id)
        return payment_repository.find_all_by_user(client.id)
        