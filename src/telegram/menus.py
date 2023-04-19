from telebot import types

def send_main_menu(bot, message):
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.row('Opção 1', 'Opção 2')
    menu_markup.row('Opção 3', 'Opção 4')
    bot.send_message(chat_id=message.chat.id, text='Escolha uma opção:', reply_markup=menu_markup)
