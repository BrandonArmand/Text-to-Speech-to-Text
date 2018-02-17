# Text-to-Speech-With-Python
[![PyPI version](https://badge.fury.io/py/gTTS.svg)](https://badge.fury.io/py/gTTS)

A basic text to speech program built with python

## Requirements
```
pip install gTTS
```

## Usage
###### _Parameters:_
* `text` - String - Text to be spoken.
* `file` - String - File to save the speech to.
* `lang` - String - [ISO 639-1 language code](#lang_list) to speak in.
* `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided).
```
textInput(text, file, language = 'en', slow = False)
```

###### _Parameters:_
* `file` - String - File to save the speech to.
```
playAudio(file)
```

## Example
```
text = input('Text to Speech: ')
if text != exitCode:
	  os.system("TASKKILL /F /IM wmplayer.exe")
		textInput(text, audioFile, language)
		playAudio(audioFile)
```
