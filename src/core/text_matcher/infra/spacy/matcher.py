from spacy.matcher import Matcher
import spacy
from core.text_matcher.domain.matcher import IMatcher

hire_plan_pattern = [[{'LOWER': 'contratar'}, {
    'LOWER': 'plano'}], [{'LOWER': 'contratar'}]]

plan_pattern = [[{'LOWER': 'quais'}, {'LOWER': 'são'}, {'LOWER': 'os'}, {
    'LOWER': 'planos'}], [{'LOWER': 'planos'}], [{'LOWER': 'planos'}, {'LOWER': 'disponiveis'}]]

availability_pattern = [
    [{'LOWER': 'disponivel'}, {'LOWER': 'na'}, {'LOWER': 'região'}], [{'LOWER': 'disponivel'}], [{'LOWER': 'disponibilidade'}], [{'LOWER': 'disponível'}]]


class TextMatcher(IMatcher):

    nlp = spacy.load('pt_core_news_sm')
    plan_matcher = Matcher(nlp.vocab)
    plans_matcher = Matcher(nlp.vocab)
    availability = Matcher(nlp.vocab)

    plans_matcher.add('plans_matcher', plan_pattern)
    plan_matcher.add('plan_matcher', hire_plan_pattern)
    availability.add('availability', availability_pattern)

    def execute(self, text: str) -> int:
        doc = self.nlp(text)
        plan = self.plan_matcher(doc)
        avali = self.availability(doc)
        plans = self.plans_matcher(doc)
        if plan:
            return 1
        elif avali:
            return 2
        elif plans:
            return 3
        else:
            return 0
