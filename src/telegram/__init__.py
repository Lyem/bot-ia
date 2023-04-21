import os
from .menus import Menus
from telebot import TeleBot
from .buttons import Buttons
from dotenv import load_dotenv
from .forms import user_data, init_form, save_answer
from core.boleto.application.use_cases import Generate_pdf
from core.clients.application.use_cases import ClientLogged
from core.text_matcher.application.use_cases import Matcher
from core.payments.application.use_cases import CreatePayment
from core.text_generation.application.use_cases import TextGeneration


class Telegram:
    def execute(self):
        print('iniciando telegram')
        load_dotenv()

        bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))

        menu = Menus(bot)

        buttons = Buttons(bot)

        clientLogged = ClientLogged()

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(
                message, 'Oi, tudo bem com você ? Meu nome é Felix Chatbot. Sou o assistente virtual da empresa Catnet em que posso ajuda-lo hoje?')
            menu.send_main_menu(message)
        
        @bot.callback_query_handler(func=lambda call: call.data != "")
        def plan(call):
            if(call.data == "200" or call.data == "400" or call.data == "600"):
                if(clientLogged.execute(call.message.chat.id)):
                    buttons.contract_plan(call.message, call.data)
                else:
                    buttons.is_client(call.message)
            elif(call.data == "not_client"):
                init_form(bot, call.message, 'create')
            elif(call.data == "is_client"):
                init_form(bot, call.message, 'is_client')
            elif(call.data == "not_contract"):
                bot.send_message(
                            call.message.chat.id, 'Contratação do plano cancelada')
            elif("yes_contract_" in call.data):
                plan = call.data.replace('yes_contract_', '')
                CreatePayment().execute(call.message.chat.id, plan)
                pdf = Generate_pdf().execute(str(call.message.chat.id), plan)
                bot.send_document(chat_id=call.message.chat.id, document=open(pdf, 'rb'))
                os.remove(pdf)
                bot.send_message(
                            call.message.chat.id, 'Após o pagamento do boleto a instalação será feita em até 7 dias uteis')

            #bot.answer_callback_query(callback_query_id=call.id)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        @bot.message_handler(func=lambda message: True)
        def listening(message):
            bot.send_chat_action(message.chat.id, 'typing')
            if (str(message.chat.id) not in user_data):
                menuchoice = menu.process_choice(message)
                if(menuchoice == False):
                    match = Matcher().execute(message.text)
                    if (match == 1):
                        buttons.plans(message)
                    elif (match == 2):
                        bot.send_message(
                            message.chat.id, 'Para verificar se o plano está disponivel na sua região por favor preencha o formulário.')
                        init_form(bot, message, 'create')
                    else:
                        gen = TextGeneration()
                        bot.send_message(
                            message.chat.id, gen.execute(message.text))
            else:
                save_answer(bot, message)

        bot.polling()
