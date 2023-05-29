from core.__seedwork.infra.http import Http


class AvailabilityService:

    def __init__(self) -> None:
        self.url = 'https://viacep.com.br'
        self.locales = [{'uf': 'SP', 'localidade': 'Sorocaba'}, {
            'uf': 'SP', 'localidade': 'Itu'}, {'uf': 'SP', 'localidade': 'Votorantim'}]

    def execute(self, cep) -> bool:
        response = Http.get(f'{self.url}/ws/ws/{cep}/json/')
        data = response.json()
        for locale in self.locales:
            if data['uf'] == locale['uf'] and data['localidade'] == locale['localidade']:
                return True
        return False
