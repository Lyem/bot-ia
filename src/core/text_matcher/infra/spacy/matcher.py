from spacy.matcher import Matcher
import spacy
from core.text_matcher.domain.matcher import IMatcher

hire_plan_pattern = [[{'LOWER': 'contratar'}, {
    'LOWER': 'plano'}], [{'LOWER': 'contratar'}]]

availability_pattern = [
    [{'LOWER': 'disponivel'}, {'LOWER': 'na'}, {'LOWER': 'região'}], [{'LOWER': 'disponivel'}], [{'LOWER': 'disponibilidade'}]]


class TextMatcher(IMatcher):

    nlp = spacy.load('pt_core_news_sm')
    plan_matcher = Matcher(nlp.vocab)
    availability = Matcher(nlp.vocab)

    plan_matcher.add('plan_matcher', hire_plan_pattern)
    availability.add('availability', availability_pattern)

    def execute(self, text: str) -> int:
        doc = self.nlp(text)
        plan = self.plan_matcher(doc)
        avali = self.availability(doc)
        if plan:
            return 1
        elif avali:
            return 2
        else:
            return 0
