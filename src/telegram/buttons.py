from telebot import types

class Buttons:
    def __init__(self, bot) -> None:
        self.bot = bot

    def plans(self, message):
        internet200 = types.InlineKeyboardButton('200Mb', callback_data='200')
        internet400 = types.InlineKeyboardButton('400Mb', callback_data='400')
        internet600 = types.InlineKeyboardButton('600Mb', callback_data='600')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(internet200)
        keyboard.add(internet400)
        keyboard.add(internet600)

        self.bot.send_message(message.chat.id, text='A empresa cat net possui 3 planos de internet, 200Mb no valor de 20 reais por mês, 400Mb no valor de 50 reais ao mês e de 600Mb por 99 reais ao mês', reply_markup=keyboard)

    def is_client(self, message):
        no = types.InlineKeyboardButton('não', callback_data='not_client')
        yes = types.InlineKeyboardButton('sim', callback_data='is_client')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        self.bot.send_message(message.chat.id, text='já é cliente?', reply_markup=keyboard)
    
    def contract_plan(self, message, plan):
        no = types.InlineKeyboardButton('não', callback_data='not_contract')
        yes = types.InlineKeyboardButton('sim', callback_data=f'yes_contract_{plan}')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        if plan == '200':
            self.bot.send_photo(message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098785528213688370/image.png')
        if plan == '400':
            self.bot.send_photo(message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098789563280937043/image.png')
        if plan == '600':
            self.bot.send_photo(message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098791122744135821/image.png')
        self.bot.send_message(message.chat.id, text=f'deseja contratar o plano de {plan}Mb?', reply_markup=keyboard)
