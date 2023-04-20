from telebot import types

class Buttons:
    def __init__(self, bot) -> None:
        self.bot = bot

    def planos(self, message):
        internet200 = types.InlineKeyboardButton('200Mb', callback_data='foo')
        internet400 = types.InlineKeyboardButton('400mb', callback_data='bar')
        internet600 = types.InlineKeyboardButton('600mb', callback_data='a')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(internet200)
        keyboard.add(internet400)
        keyboard.add(internet600)

        self.bot.send_message(message.chat.id, text='Keyboard example', reply_markup=keyboard)

