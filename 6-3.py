# -*- coding: UTF-8 -*-

# 如何解析XML文档

from xml.etree.cElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()
print(root, root.tag, root.attrib, root.text)

for item in root:
    print(item.get('id'))


# 支持XPath语法
# find, findall, iterfind, iter
