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

        self.bot.send_message(
            message.chat.id, text='A empresa bot net possui 3 planos de internet, 200Mb no valor de 20 reais por mês, 400Mb no valor de 50 reais ao mês e de 600Mb por 99 reais ao mês', reply_markup=keyboard)

    def is_client(self, message, route):
        no = types.InlineKeyboardButton(
            'não', callback_data=f'not_client#{route}')
        yes = types.InlineKeyboardButton(
            'sim', callback_data=f'is_client#{route}')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        self.bot.send_message(
            message.chat.id, text='já é cliente?', reply_markup=keyboard)

    def support(self, message):
        no = types.InlineKeyboardButton('não', callback_data="support_no")
        yes = types.InlineKeyboardButton('sim', callback_data="support_yes")

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        self.bot.send_message(
            message.chat.id, text='Você escolheu suporte técnico, antes de entrar em contato com nosso suporte técnico, precisamos que você realize alguns procedimentos.', reply_markup=keyboard)

    def supportHelp(self, message, number):
        no = types.InlineKeyboardButton(
            'não', callback_data=f'support_no#{number}')
        yes = types.InlineKeyboardButton('sim', callback_data="support_no")

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        self.bot.send_message(
            message.chat.id, text='Esse procedimento ajudou a restaurar o sinal da sua internet ?', reply_markup=keyboard)

    def helpyou(self, id):
        no = types.InlineKeyboardButton('não', callback_data="help_no")
        yes = types.InlineKeyboardButton('sim', callback_data="help_yes")

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        self.bot.send_message(
            id, text='Posso ajuda-lo em algo mais ?', reply_markup=keyboard)

    def contract_plan(self, message, plan):
        no = types.InlineKeyboardButton('não', callback_data='not_contract')
        yes = types.InlineKeyboardButton(
            'sim', callback_data=f'yes_contract_{plan}')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(no, yes)

        if plan == '200':
            self.bot.send_photo(
                message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098785528213688370/image.png')
        if plan == '400':
            self.bot.send_photo(
                message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098789563280937043/image.png')
        if plan == '600':
            self.bot.send_photo(
                message.chat.id, 'https://media.discordapp.net/attachments/1098759004425040006/1098791122744135821/image.png')
        self.bot.send_message(
            message.chat.id, text=f'deseja contratar o plano de {plan}Mb?', reply_markup=keyboard)
