import subprocess
class TtsSpeak():
    def __init__(self, message):
        self.message = message
    def speak(self):
        subprocess.call(["espeak", self.message])