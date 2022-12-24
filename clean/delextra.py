import os

# Set the directory to scan
directory = '.'

# Initialize empty lists for the .txt and .wav files
txt_files = []
wav_files = []

# Use os.listdir() to get a list of all the files in the directory
files = os.listdir(directory)

# Iterate through the list of files
for file in files:
    # If the file is a .txt file, add it to the txt_files list
    if file.endswith('.txt'):
        txt_files.append(file)
    # If the file is a .wav file, add it to the wav_files list
    elif file.endswith('.wav'):
        wav_files.append(file)

# Iterate through the txt_files list
for txt_file in txt_files:
    # Get the prefix of the .txt file
    prefix = txt_file.split('.')[0]
    # Iterate through the wav_files list
    for wav_file in wav_files:
        # If the prefix of the .wav file matches the prefix of the .txt file, delete the .txt file
        if wav_file.startswith(prefix):
            os.remove(txt_file)
