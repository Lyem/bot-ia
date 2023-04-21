from core.clients.application.use_cases import ClientCreate, ClientExist

form = {
    "create": [
            {'key': 'name', 'question': 'Qual é o seu nome?'},
            {'key': 'cell', 'question': 'Qual é o seu numero de telefone'},
            {'key': 'cep', 'question': 'Qual é o seu cep?'},
            {'key': 'home_number', 'question': 'Qual é o numero da sua casa?'},
            {'key': 'cpf', 'question': 'Qual é o seu cpf?'},
        ],
    "is_client": [{'key': 'cpf', 'question': 'Qual é o seu cpf?'}]
}

user_data = {}

def save_answer(bot, message):
    step = user_data[str(message.chat.id)]['step']
    key = form[user_data[str(message.chat.id)]['type']][step]['key']
    user_data[str(message.chat.id)]['form'][key] = message.text
    user_data[str(message.chat.id)]['step'] += 1
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
