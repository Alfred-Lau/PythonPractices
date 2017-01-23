# -*- coding: UTF-8 -*-

# 如何使用线程池

from concurrent.futures import ThreadPoolExecutor
import time

excutor = ThreadPoolExecutor(3)


def f(a, b):
    print('f', a, b)
    time.sleep(10)
    return a ** b

future = excutor.submit(f, 2, 3)
print(future.result())


excutor.map(f, [2, 3, 5, 6, 7], [4, 5, 6, 7, 8])
