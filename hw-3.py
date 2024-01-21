import threading
import logging
import time
from multiprocessing import Pool, cpu_count

def factorize(*numbers):
    result = []
    for num in numbers:
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
    return result

def callback(res):
    print(f'reuslt = {res}')

    # raise NotImplementedError() # Remove after implementation

if __name__ == '__main__':
    start = time.time()
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    a = factorize(128)
    print(f'core: {cpu_count()}')
    with Pool(cpu_count()) as p:
        p.map_async(factorize, [128, 255, 99999, 10651060], callback=callback)
        p.close()
        p.join()
    end = time.time()
    logging.debug(end - start)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]