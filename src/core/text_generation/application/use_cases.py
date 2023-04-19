from core.__seedwork.application.use_cases import UseCase
from core.text_generation.infra.chatter.generate import Generate


class TextGeneration(UseCase):

    def execute(self, txt: str) -> str:
        gen = Generate()
        return gen.execute(txt)
