import speech_recognition as sr
import sounddevice as sd
from PyQt6.QtCore import QThread, pyqtSignal


class VoiceInput(QThread):
    finished_text = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        fs = 16000
        seconds = 7

        try:
            recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            audio_data = sr.AudioData(recording.tobytes(), fs, 2)
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            return self.finished_text.emit(text)
        except Exception:
            return self.finished_text.emit("Не расслышала... Повтори еще раз.")
