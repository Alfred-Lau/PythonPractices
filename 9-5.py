# -*- coding: UTF-8 -*-

# 如何在类中定义装饰器

import logging
from time import localtime, time, strftime, sleep


class CallingInfo(object):
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')
        log.addHandler(fh)
        log.info('start'.center(50, '-'))
        self.log = log
        self.formatter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'

    def setFormatter(self, formatter):
        self.formatter = formatter

    def turnOn(self):
        self.log.setLevel(logging.INFO)

    def turnOff(self):
        self.log.setLevel(logging.WARN)

    def info(self, func):
        def wrapper(*args, **kargs):
            wrapper.ncalls += 1
            lt = localtime()
            start = time()
            res = func(*args, **kargs)
            used = time() - start

            info = {}
            info['func'] = func.__name__
            info['time'] = strftime('%x %x', lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res

        wrapper.ncalls = 0
        return wrapper


cinfo1 = CallingInfo('mylog1')
cinfo2 = CallingInfo('mylog2')

cinfo1.formatter = '%(func)s -> [%(time)s - %(ncalls)s]'
cinfo2.turnOff()


@cinfo1.info
def f():
    print('in f')


@cinfo1.info
def g():
    print('in g')


@cinfo2.info
def h():
    print('in h')


from random import choice

for _ in range(50):
    choice([f, g, h])()
    sleep(choice([0.5, 1, 1.5]))
