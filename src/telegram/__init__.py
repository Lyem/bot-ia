import os
from telebot import TeleBot
from dotenv import load_dotenv
from .menus import send_main_menu
from .forms import user_data, init_form, save_answer
from core.text_matcher.application.use_cases import Matcher
from core.text_generation.application.use_cases import TextGeneration


class Telegram:
    def execute(self):
        print('iniciando telegram')
        load_dotenv()

        bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))


        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(
                message, '''Olá! Eu sou o BotFelix, o assistente virtual da Cat Net, a empresa de internet que oferece os melhores planos para você. Comigo, você pode ficar por dentro dos preços dos nossos serviços e também gerar PDFs com informações sobre seus pagamentos pendentes. Além disso, se precisar de ajuda, posso direcioná-lo para o nosso suporte para esclarecer qualquer dúvida ou resolver qualquer problema. Estou aqui para ajudá-lo a ter a melhor experiência com nossos serviços. Vamos começar!''')

        @bot.message_handler(commands=['menu'])
        def handle_menu(message):
            send_main_menu(bot, message)
            #bot.register_next_step_handler(message, process_choice)

        @bot.message_handler(func=lambda message: True)
        def listening(message):
            bot.send_chat_action(message.chat.id, 'typing')
            if (str(message.chat.id) not in user_data):
                match = Matcher().execute(message.text)
                if (match == 1):
                    bot.send_message(
                        message.chat.id, 'Por favor, preencha o formulário.')
                    init_form(bot, message)
                elif (match == 2):
                    bot.send_message(
                        message.chat.id, 'Para verificar se o plano está disponivel na sua região por favor preencha o formulário.')
                    init_form(bot, message)
                else:
                    gen = TextGeneration()
                    bot.send_message(
                        message.chat.id, gen.execute(message.text))
            else:
                save_answer(bot, message)

        bot.polling()
