import os
from curtsies.fmtfuncs import yellow
import time
from tqdm import tqdm

d = 'repos'

for dirpath, dirnames, filenames in tqdm(os.walk(d)):
    for f in filenames:
        full_path = os.path.join(dirpath, f)
        if full_path.endswith(".py"):
            pass
        else:
            if d in full_path:
                os.remove(full_path)
            else:
                print(yellow("something is wrong"))
                time.sleep(60)
