from core.__seedwork.application.use_cases import UseCase
from core.audio_to_text.infra.speech_recognition import SpeechRecognitionService

class AudioToTextUseCase(UseCase):
    def execute(self, file: str) -> str:
        return SpeechRecognitionService(file).execute()
