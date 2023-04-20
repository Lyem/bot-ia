from telebot import types
from .buttons import Buttons

class Menus:

    def __init__(self, bot) -> None:
        self.bot = bot
        self.buttons = Buttons(bot)

    def send_main_menu(self, message):
        menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_markup.row('Planos')
        menu_markup.row('Suporte', 'Boletos')
        menu_markup.row('Cancelar atendimento')
        self.bot.send_message(chat_id=message.chat.id, text='Escolha uma opção:', reply_markup=menu_markup)

    def process_choice(self, message) -> bool:
        if message.text == 'Planos':
            self.buttons.planos(message)
            return True
        elif message.text == 'Suporte':
            self.bot.send_message(chat_id=message.chat.id, text='Você selecionou a suporte')
            return True
        elif message.text == 'Boletos':
            self.bot.send_message(chat_id=message.chat.id, text='Você selecionou a boletos')
            return True
        elif message.text == 'Cancelar atendimento':
            return True
        return False
