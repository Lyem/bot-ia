from core.clients.application.use_cases import ClientCreate, ClientExist
import re

form = {
    "create": [
            {'key': 'name', 'question': 'Qual é o seu nome?', 'validate': None},
            {'key': 'cell', 'question': 'Qual é o seu numero de telefone', 'validate': r"^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$"},
            {'key': 'cep', 'question': 'Qual é o seu cep?', 'validate': r"(\d){5}(\d){3}"},
            {'key': 'home_number', 'question': 'Qual é o numero da sua casa?', 'validate': r"^[0-9]*$"},
            {'key': 'cpf', 'question': 'Qual é o seu cpf?', 'validate': r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"},
        ],
    "is_client": [{'key': 'cpf', 'question': 'Qual é o seu cpf?', 'validate': r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"}]
}

user_data = {}

def save_answer(bot, message):
    step = user_data[str(message.chat.id)]['step']
    key = form[user_data[str(message.chat.id)]['type']][step]['key']
    if(form[user_data[str(message.chat.id)]['type']][step]['validate'] == None):
        user_data[str(message.chat.id)]['form'][key] = message.text
        user_data[str(message.chat.id)]['step'] += 1
    else:
        pat = re.compile(form[user_data[str(message.chat.id)]['type']][step]['validate'])
        if re.fullmatch(pat, message.text):
            user_data[str(message.chat.id)]['form'][key] = message.text
            user_data[str(message.chat.id)]['step'] += 1
        else:
            bot.send_message(
                message.chat.id, 'Valor invalido')
    if user_data[str(message.chat.id)]['step'] < len(form[user_data[str(message.chat.id)]['type']]):
        ask_question(bot, message)
    else:
        if(user_data[str(message.chat.id)]['type'] == 'create'):
            user_form = user_data[str(message.chat.id)]['form']
            ClientCreate().execute(user_form['name'], user_form['cell'], user_form['cep'],
                                    user_form['home_number'], message.chat.id, user_form['cpf'])
            bot.send_message(
                message.chat.id, 'Obrigado por preencher o formulário!')
        elif(user_data[str(message.chat.id)]['type'] == 'is_client'):
            user_form = user_data[str(message.chat.id)]['form']
            ClientExist().execute(user_form['cpf'], message.chat.id)
        user_data.pop(str(message.chat.id))


def ask_question(bot, message):
    step = user_data[str(message.chat.id)]['step']
    question = form[user_data[str(message.chat.id)]['type']][step]['question']
    bot.send_message(message.chat.id, question)

def init_form(bot, message, form_type):
    user_data[str(message.chat.id)] = {}
    user_data[str(message.chat.id)]['form'] = {}
    user_data[str(message.chat.id)]['step'] = 0
    user_data[str(message.chat.id)]['type'] = form_type
    ask_question(bot, message)
