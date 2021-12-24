import os
import re
import glob

cwd = os.getcwd()
file_pattern = '*.txt'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))
elif os.path.isfile(file_pattern):
    file_name_list.append(file_pattern)
else:
    raise ValueError('{} is not a valid pattern or file!'.format(file_pattern))

file_path_list = [
    os.path.join(cwd, file_name)
    for file_name in file_name_list
]

re_exp_list = [
    re.compile(r'[0-9]'),  # removes numbers
    re.compile(r'[^\x00-\x7F]+'),  # removes any character not in ASCII character set 0-127 (0x0 to 0x7F)
    re.compile(r'\x0C'),  # removes Form Feed U+000C
    re.compile(r'\u2014', '-'), # removes Em dash U+2014
    re.compile(r',{2,3}'),  # removes consecutive commas
    re.compile(r'([.,/#!$%^&*;:{}=_`~()-])[.,/#!$%^&*;:{}=_`~()-]+'),  # removes consecutive punctuation
    re.compile(r'(  +)'),  # removes extra spaces
    (re.compile(r'[ \t]{2,}'), '   '),  # removes more than two tabs
]

for file_path in file_path_list:
    file_dir, file_name = os.path.split(file_path)
    clean_file_path = os.path.join(file_dir, 'clean', file_name)
    clean_file_dir = os.path.dirname(clean_file_path)
    if not os.path.isdir(clean_file_dir):
        os.makedirs(clean_file_dir)

    with open(file_path, 'r', encoding='utf-8',errors='ignore') as src, open(clean_file_path, 'w') as dst:
        while True:
            chunk = src.read(5096)
            if not chunk:
                break

            for re_exp in re_exp_list:
                if isinstance(re_exp, tuple):
                    re_sub_pattern = re_exp[0]
                    replace = re_exp[1]
                else:
                    re_sub_pattern = re_exp
                    replace = ''
                chunk = re_sub_pattern.sub(replace, chunk)
            dst.write(chunk)
