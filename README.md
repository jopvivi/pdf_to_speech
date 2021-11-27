A toolkit for converting PDF books into TTS audio books. 

## Setup
* `conda create --name tts_env python=3.7`
* `conda activate tts_env`
* `pip install --upgrade pip`
* `pip install pyttsx3`

## Further reading

https://pypi.org/project/pyttsx3/

## Use

I used to depend on TTSReader to hear text: https://www.majorgeeks.com/files/details/ttsreader.html

I wanted to automate what used to be a manual process. With this, you can convert large groups of files into audio files.

To adjust the speech rate, edit line 16 of ``speech.py``

SAPI5 voice Microsoft Mary recommended. 😎
