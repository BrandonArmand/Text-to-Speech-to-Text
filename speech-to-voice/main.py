import speech_recognition as sr
from audio import *

audioFile = 'audio.mp3'

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = None
        audio = r.listen(source)
        try:
            os.system("TASKKILL /F /IM wmplayer.exe")
            print(r.recognize_google(audio))
            textInput(r.recognize_google(audio), audioFile)
            fileExist = True
            playAudio(audioFile)
        except sr.UnknownValueError:
            print("Could not understand.")
