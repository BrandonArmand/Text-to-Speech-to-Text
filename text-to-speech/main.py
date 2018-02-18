from audio import *

audioFile = 'audio.mp3'
exitCode = ':exit'

while True:
	language = input('language = ')
	text = ''
	while text != exitCode:
		text = input('Text to Speech: ')
		if text != exitCode:
			os.system("TASKKILL /F /IM wmplayer.exe")
			textInput(text, audioFile, language)
			playAudio(audioFile)
