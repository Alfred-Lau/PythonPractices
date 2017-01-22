# -*- coding: UTF-8 -*-

# 如何线程间通信

import csv
from xml.etree.cElementTree import Element, ElementTree, tostring
import requests
from io import StringIO
from queue import Queue
from threading import Thread

# 全局,线程间通信


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content.decode('utf-8'))

    def run(self):
        print('download', self.sid)
        # 1.
        data = self.download(self.url)
        # 2. (sid, data)
        self.queue.put((self.sid, data))


class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def pretty(self, e, level=0):
        if len(e) > 0:
            e.text = '\n' + '\t' * (level + 1)
            for child in e:
                pretty(child, level + 1)
            child.tail = child.tail[:-1]
        e.tail = '\n' + '\t' * level

    def csvToXml(self, scsv, fxml):
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

        self.pretty(root)
        et = ElementTree(root)
        et.write(fxml)

    def run(self):
        while True:
            sid, data = self.queue.get()
            print('convert', sid)
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                self.csvToXml(data, fname)

q = Queue()
dThreads = [DownloadThread(i, q) for i in range(1, 11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()

q.put((-1, None))

