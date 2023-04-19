from core.clients.application.use_cases import ClientCreate

form = [
            {'key': 'name', 'question': 'Qual é o seu nome?'},
            {'key': 'cell', 'question': 'Qual é o seu numero de telefone'},
            {'key': 'cep', 'question': 'Qual é o seu cep?'},
            {'key': 'home_number', 'question': 'Qual é o numero da sua casa?'},
            {'key': 'cpf', 'question': 'Qual é o seu cpf?'},
        ]

user_data = {}

def save_answer(bot, message):
    step = user_data[str(message.chat.id)]['step']
    key = form[step]['key']
    user_data[str(message.chat.id)]['form'][key] = message.text
    user_data[str(message.chat.id)]['step'] += 1
    if user_data[str(message.chat.id)]['step'] < len(form):
        ask_question(bot, message)
    else:
        user_form = user_data[str(message.chat.id)]['form']
        ClientCreate().execute(user_form['name'], user_form['cell'], user_form['cep'],
                                user_form['home_number'], message.chat.id, user_form['cpf'])
        user_data.pop(str(message.chat.id))
        bot.send_message(
            message.chat.id, 'Obrigado por preencher o formulário!')

def ask_question(bot, message):
    step = user_data[str(message.chat.id)]['step']
    question = form[step]['question']
    bot.send_message(message.chat.id, question)

def init_form(bot, message):
    user_data[str(message.chat.id)] = {}
    user_data[str(message.chat.id)]['form'] = {}
    user_data[str(message.chat.id)]['step'] = 0
    ask_question(bot, message)
