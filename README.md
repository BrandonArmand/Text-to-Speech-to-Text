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
* `file` - String - File to load the speech from.
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
## Supported Languages <a name="lang_list"></a>

* 'af' : 'Afrikaans'
* 'sq' : 'Albanian'
* 'ar' : 'Arabic'
* 'hy' : 'Armenian'
* 'bn' : 'Bengali'
* 'ca' : 'Catalan'
* 'zh' : 'Chinese'
* 'zh-cn' : 'Chinese (Mandarin/China)'
* 'zh-tw' : 'Chinese (Mandarin/Taiwan)'
* 'zh-yue' : 'Chinese (Cantonese)'
* 'hr' : 'Croatian'
* 'cs' : 'Czech'
* 'da' : 'Danish'
* 'nl' : 'Dutch'
* 'en' : 'English'
* 'en-au' : 'English (Australia)'
* 'en-uk' : 'English (United Kingdom)'
* 'en-us' : 'English (United States)'
* 'eo' : 'Esperanto'
* 'fi' : 'Finnish'
* 'fr' : 'French'
* 'de' : 'German'
* 'el' : 'Greek'
* 'hi' : 'Hindi'
* 'hu' : 'Hungarian'
* 'is' : 'Icelandic'
* 'id' : 'Indonesian'
* 'it' : 'Italian'
* 'ja' : 'Japanese'
* 'km' : 'Khmer (Cambodian)'
* 'ko' : 'Korean'
* 'la' : 'Latin'
* 'lv' : 'Latvian'
* 'mk' : 'Macedonian'
* 'no' : 'Norwegian'
* 'pl' : 'Polish'
* 'pt' : 'Portuguese'
* 'ro' : 'Romanian'
* 'ru' : 'Russian'
* 'sr' : 'Serbian'
* 'si' : 'Sinhala'
* 'sk' : 'Slovak'
* 'es' : 'Spanish'
* 'es-es' : 'Spanish (Spain)'
* 'es-us' : 'Spanish (United States)'
* 'sw' : 'Swahili'
* 'sv' : 'Swedish'
* 'ta' : 'Tamil'
* 'th' : 'Thai'
* 'tr' : 'Turkish'
* 'uk' : 'Ukrainian'
* 'vi' : 'Vietnamese'
* 'cy' : 'Welsh'
