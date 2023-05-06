import os
import io
from .menus import Menus
from telebot import TeleBot
from .buttons import Buttons
from dotenv import load_dotenv
from pydub import AudioSegment
from core.__seedwork.infra.http import Http
from .forms import user_data, init_form, save_answer
from core.boleto.application.use_cases import Generate_pdf
from core.clients.application.use_cases import ClientLogged
from core.text_matcher.application.use_cases import Matcher
from core.payments.application.use_cases import CreatePayment
from core.text_generation.application.use_cases import TextGeneration
from core.audio_to_text.application.use_cases import AudioToTextUseCase


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
                    buttons.is_client(call.message, 0)
            elif(call.data == "not_client#0"):
                init_form(bot, call.message, 'create', 0)
            elif(call.data == "is_client#0"):
                init_form(bot, call.message, 'is_client', 0)
            elif(call.data == "not_client#1"):
                init_form(bot, call.message, 'create', 1)
            elif(call.data == "is_client#1"):
                init_form(bot, call.message, 'is_client', 1)
            elif(call.data == "not_client#2"):
                init_form(bot, call.message, 'create', 2)
            elif(call.data == "is_client#2"):
                init_form(bot, call.message, 'is_client', 2)
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
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        def answer(bot, message, text):
            bot.send_chat_action(message.chat.id, 'typing')
            if (str(message.chat.id) not in user_data):
                menuchoice = menu.process_choice(message)
                if(menuchoice == False):
                    match = Matcher().execute(text)
                    if (match == 1):
                        buttons.plans(message)
                    elif (match == 2):
                        bot.send_message(
                            message.chat.id, 'Para verificar se o plano está disponivel na sua região por favor preencha o formulário.')
                        init_form(bot, message, 'availability', 1)
                    elif (match == 3):
                        buttons.plans(message)
                    else:
                        gen = TextGeneration()
                        bot.send_message(
                            message.chat.id, gen.execute(text))
            else:
                save_answer(bot, message)

        @bot.message_handler(func=lambda message: True)
        def listening(message):
            answer(bot, message, message.text)
            
        
        @bot.message_handler(content_types=['voice'])
        def handle_audio(message):
            file_id = message.voice.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path
            audio_url = f'https://api.telegram.org/file/bot{bot.token}/{file_path}'
            response = Http.get(audio_url)
            path = os.path.join(os.getcwd(), 'src', 'core',
                            'audio_to_text', 'infra', f'{file_id}.wav')
            if response.status == 200:
                audio_segment = AudioSegment.from_ogg(io.BytesIO(response.content))
                audio_segment.export(path, format='wav')
                text = AudioToTextUseCase().execute(path)
                os.remove(path)
                if(text == 'Não consegui entender o que você falou'):
                    bot.send_message(message.chat.id,text)
                else:
                    answer(bot, message, text)

        bot.polling()
