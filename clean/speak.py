import os
import glob
import pyttsx3

engine = pyttsx3.init()

file_pattern = '*.txt'
file_name_list = []
count = 0

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
    text_file = ''
    with open(target,'r',encoding='utf-8', errors='ignore') as src:
        for i in src:
            text_file = text_file + i
        wav_filename = target.replace('.txt','.wav')
        fullPath = os.path.join(os.getcwd(), wav_filename)
        engine.save_to_file(text_file, fullPath)
        engine.runAndWait()
        count = count + 1
        message = "{}".format(count) + " complete."
        print(message)
