from core.__seedwork.application.use_cases import UseCase
from core.availability.infra.viacep import AvailabilityService

class AvailabilityUseCase(UseCase):
    def execute(self, cep: str) -> bool:
        return AvailabilityService().execute(cep)
