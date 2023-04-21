import datetime

class PaymentRepository():
    def __init__(self) -> None:
        from .payments_model import Payments
        Payments.create_table()
        self.payment = Payments

    def create(self, client, price, plan):
        self.payment.create(price=price, client=client, name=plan)

    def find_all_by_user(self, client_id):
        return self.payment.select().where(self.payment.client_id == client_id)
