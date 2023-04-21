import openai
import pandas as pd
from dotenv import load_dotenv
import os
import numpy as np
import json

load_dotenv()


class Generate:

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_TOKEN")

    def embedding(self, txt):
        res = openai.Embedding.create(
            model='text-embedding-ada-002',
            input=txt
        )
        return res['data'][0]['embedding']

    def similar_vector(self, v1, v2):
        return np.dot(np.array(v1), np.array(v2))

    def execute(self, txt: str) -> str:
        path = os.path.join(os.getcwd(), 'src', 'core',
                            'text_generation', 'infra', 'openia')
        df = pd.read_csv(os.path.join(path, 'catnet_embedding.csv'))
        question_embedding = self.embedding(txt)
        df['similarity'] = df['embedding'].apply(
            lambda v: json.loads(v)
        ).apply(
            lambda v: self.similar_vector(v, question_embedding)
        )
        context = df.nlargest(1, 'similarity').iloc[0]['resume']
        p = f'''Responda a pergunta abaixo, somente se você tiver 100% de certeza e não responda com informações ou palavras que não foram passadas nessa mensagem.
                Context: {context}
                Q: {txt}
                A:'''
        response = openai.Completion.create(
            prompt=p, max_tokens=200, model='text-davinci-003')
        return response['choices'][0]['text']

    def generate_csv_embedding(self):
        path = os.path.join(os.getcwd(), 'src', 'core',
                            'text_generation', 'infra', 'openia')
        df = pd.read_csv(os.path.join(path, 'catnet.csv'))
        df['embedding'] = df['resume'].apply(self.embedding)
        df.to_csv(os.path.join(path, "catnet_embedding.csv"), index=False)


if __name__ == "__main__":
    gen = Generate()
    gen.generate_csv_embedding()
