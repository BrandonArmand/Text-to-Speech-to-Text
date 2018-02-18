from gtts import gTTS
import os

def textInput(text, file, language = 'en', slow = False):
	myobj = gTTS(text=text, lang=language, slow=False)
	myobj.save(file)

def playAudio(file):
	os.system('clear')
	os.system('cls')
	os.system(file)
	os.remove(file)
