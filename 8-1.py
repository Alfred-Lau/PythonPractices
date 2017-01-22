# -*- coding: UTF-8 -*-


# 如何使用多线程

# python线程不适合处理cpu密集型的任务, 全局解释器锁存在


import csv
from xml.etree.cElementTree import Element, ElementTree, tostring
import requests
from io import StringIO


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content.decode('utf-8'))


def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.__next__()
    # headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

    pretty(root)
    et = ElementTree(root)
    et.write(fxml)


def handle(sid):
    print('Download...(%d)' % sid)
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None:
        # 此处需要把continue转换为return
        return
    print('convert to xml ... (%d)' % sid)
    fname = str(sid).rjust(6, '0') + '.xml'
    csvToXml(rf, fname)


from threading import Thread

"""
方法一

t = Thread(target=handle, args=(1,))
t.start()

print('in main thread')

"""

# 方法二


class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid
    # 类似于target参数,线程入口

    def run(self):
        handle(self.sid)

threads = []
for x in range(1, 11):
    t = MyThread(x)
    threads.append(t)
    t.start()

# 阻塞主进程,等待子线程执行完成
for t in threads:
    t.join()

print('main thread')
