from core.text_matcher.infra.spacy.matcher import TextMatcher

class TestMatcher():

    def test_returns(self):
        assert TextMatcher().execute('criar conta') == 0