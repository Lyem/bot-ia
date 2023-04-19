from core.__seedwork.application.use_cases import UseCase
from core.text_matcher.infra.spacy.matcher import TextMatcher


class Matcher(UseCase):

    def execute(self, txt: str) -> int:
        return TextMatcher().execute(txt)
