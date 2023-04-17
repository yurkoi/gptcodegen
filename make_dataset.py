import os
from tqdm import tqdm

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 480
NEWLINE_CHAR = "<N>"

full_paths = []
for dirpath, dirnames, filenames in tqdm(os.walk('repos')):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        full_paths.append(full_path)

print(len(full_paths))

with open("../python_code_text_data.txt", "a") as f:
    for fpath in tqdm(full_paths):
        try:
            d = open(fpath, 'r').read()
            fd = d.replace('\n', NEWLINE_CHAR)

            if MIN_CHAR_LENGTH < len(d) <= MAX_CHAR_LENGTH:
                f.write(fd + "\n")
            else:
                sd = fd.split(f'{NEWLINE_CHAR}{NEWLINE_CHAR}')
                sub_string = ''
                for split in sd:
                    sub_string += split + f'{NEWLINE_CHAR}{NEWLINE_CHAR}'
                    if MIN_CHAR_LENGTH < len(sub_string) <= MAX_CHAR_LENGTH:
                        f.write(sub_string + "\n")
                        sub_string = ""

        except Exception as e:
            print(str(e))

