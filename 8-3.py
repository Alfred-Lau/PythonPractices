# -*- coding: UTF-8 -*-

# 如何在线程间进行事件通知


import csv
from xml.etree.cElementTree import Element, ElementTree, tostring
import requests
from io import StringIO
from queue import Queue
from threading import Thread, Event
import tarfile
import os


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


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
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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

        pretty(root)
        et = ElementTree(root)
        et.write(fxml)

    def run(self):
        count = 0
        while True:
            sid, data = self.queue.get()
            print('convert', sid)
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                self.csvToXml(data, fname)
                count += 1
                if count == 5:
                    self.cEvent.set()

                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0


class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        # 创建守护线程
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 11)]
    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q, cEvent, tEvent)
    tThread = TarThread(cEvent, tEvent)
    tThread.start()

    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()

    q.put((-1, None))
    print('main thread')
