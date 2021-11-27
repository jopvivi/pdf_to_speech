import os
import glob
import pyttsx3

engine = pyttsx3.init()

file_pattern = '*.txt'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

# speech rate
engine.setProperty('rate', 600)
rate = engine.getProperty('rate')
# speech volume
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
# speech voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.runAndWait() # engine start

for target in file_name_list:
    string_to_parse = ''
    with open(target,'r',encoding='utf-8', errors='ignore') as text_file:
        for i in text_file.readlines():
            string_to_parse = string_to_parse + i
        wav_filename = target.replace('.txt','.wav')
        fullPath = os.path.join(os.getcwd(), wav_filename)
        engine.save_to_file(string_to_parse, fullPath)
        engine.runAndWait()
