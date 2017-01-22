# -*- coding: UTF-8 -*-

# 如何构建xml文档

from util64 import pretty
import csv
from xml.etree.cElementTree import Element, ElementTree


def csv_to_xml(fname):
    with open(fname, 'r') as rf:
        reader = csv.reader(rf)
        headers = reader.__next__()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    pretty(root)
    return ElementTree(root)

et = csv_to_xml('pingan.csv')
print(et)
et.write('pingan.xml')

