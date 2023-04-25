import os
from telebot import types
from .buttons import Buttons
from core.boleto.application.use_cases import Generate_pdf
from core.clients.application.use_cases import ClientLogged
from core.payments.application.use_cases import GetAllByClient

class Menus:

    def __init__(self, bot) -> None:
        self.bot = bot
        self.buttons = Buttons(bot)

    def send_main_menu(self, message):
        menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_markup.row('Planos')
        menu_markup.row('Suporte', 'Boletos')
        self.bot.send_message(chat_id=message.chat.id, text='Selecione uma opção:', reply_markup=menu_markup)

    def process_choice(self, message) -> bool:
        if message.text == 'Planos':
            self.buttons.plans(message)
            return True
        elif message.text == 'Suporte':
            self.bot.send_message(chat_id=message.chat.id, text='Entre em contato com o nosso especialista')
            self.bot.send_contact(message.chat.id, '5511942007799', 'Suporte do', last_name='vasco')
            return True
        elif message.text == 'Boletos':
            if(ClientLogged().execute(message.chat.id)):
                self.bot.send_message(chat_id=message.chat.id, text='Verificando boletos', reply_markup=types.ReplyKeyboardRemove())
                payments = GetAllByClient().execute(message.chat.id)
                if(len(payments) < 1):
                    self.bot.send_message(chat_id=message.chat.id, text='Você não tem pagamentos pendentes')
                for pay in payments:
                    if(pay.is_pay == False):
                        self.bot.send_message(chat_id=message.chat.id, text=f'boleto do plano {pay.name}')
                        pdf = Generate_pdf().execute(str(message.chat.id), pay.name.replace('Mb', ''))
                        self.bot.send_document(chat_id=message.chat.id, document=open(pdf, 'rb'))
                        os.remove(pdf)
                self.send_main_menu(message)
            else:
                self.buttons.is_client(message)
            return True
        return False
