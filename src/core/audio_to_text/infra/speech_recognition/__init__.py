from pathlib import Path
import speech_recognition as sr

class SpeechRecognitionService:
    def __init__(self, file) -> None:
        self.r = sr.Recognizer()
        self.file = file

    def execute(self) -> str:
        with sr.AudioFile(self.file) as source:
            audio = self.r.record(source)
        try:
            return self.r.recognize_google(audio, language="pt-BR")
        except:
            return 'Não consegui entender o que você falou'

