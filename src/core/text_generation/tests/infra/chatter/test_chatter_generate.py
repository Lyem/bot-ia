from core.text_generation.infra.chatter.generate import Generate


class TestChatterGenerate:
    def test_chtter_generate_return_text(self):
        gen = Generate()
        response = gen.execute('Quais são os planos da bot net?')
        assert isinstance(response, str)
