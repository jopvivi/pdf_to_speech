A toolkit for converting PDF books into TTS audio books. 

## Setup
* `conda create --name tts_env python=3.7`
* `conda activate tts_env`
* `pip install --upgrade pip`
* `pip install pyttsx3`

## Use

I used to depend on [TTSReader](https://www.majorgeeks.com/files/details/ttsreader.html) to hear text. I wanted to automate what used to be a manual process. 

Use this to convert large groups of files to audio files: ``convert.sh`` > ``clean.py`` > ``split.py`` as needed > ``speak.py``

To adjust the speech rate, edit line 16 of ``speak.py``

SAPI5 voice Microsoft Mary recommended. 😎

## Further reading

[pyttsx3](https://pypi.org/project/pyttsx3/) - Text to Speech (TTS) library for Python 2 and 3
