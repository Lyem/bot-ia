import os
from chatterbot.trainers import ListTrainer
from .train import train, train2, train3, train4, train5, train6, train7, exclusions
from chatterbot import ChatBot, comparisons, response_selection
from chatterbot.response_selection import get_most_frequent_response

path = os.path.join(os.getcwd(), 'src', 'core',
                    'text_generation', 'infra', 'chatter')
chatbot = ChatBot(
    "FelixBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{os.path.join(path, 'database.sqlite3')}",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': comparisons.LevenshteinDistance,
            'response_selection_method': response_selection.get_first_response,
            'default_response': 'Desculpe eu não entendi',
            'maximum_similarity_threshold': 0.90
        }
    ],
    read_only=True,
)


trainer = ListTrainer(
    chatbot, response_selection_method=get_most_frequent_response, exclusions=exclusions)

trainer.train(train)
trainer.train(train2)
trainer.train(train3)
trainer.train(train4)
trainer.train(train5)
trainer.train(train6)
trainer.train(train7)


class Generate:

    def execute(self, txt: str) -> str:
        return str(chatbot.get_response(txt))
