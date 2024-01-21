import os
import logging
from pathlib import Path
import time
from threading import Thread
import shutil
import sys

# a = Path(r"C:\Users\swgon\OneDrive\Рабочий стол\Hlam")
a = Path(sys.argv[1])

folders = []

def sort(a):
    for i in os.listdir(a):
        w = os.path.join(a, i)
        if os.path.isdir(w):
            folders.append(w)
            sort(w)


def sort_file(a):
    for i in a.iterdir():
        if i.is_file():
             sfx = i.suffix

for i in folders:
        sort_file(i)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    times = time.time()
    t1 = Thread(target=sort, args=(a,))
    t2 = Thread(target=sort_file, args=(a,))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    finish_time = end_time - start
    logging.debug(finish_time)
    with open("text.txt", "w") as file:
            file.write(f"time: {finish_time} sec\n")
            for i in folders:
                file.write(f"{i}\n")