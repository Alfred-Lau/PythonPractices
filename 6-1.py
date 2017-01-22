# -*- coding: UTF-8 -*-

# 如何读写csv数据
#
# # 注意python3.x对urllib做出的重新规划
# # from urllib.request import urlretrieve
#
# # urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')
#
# import csv
#
# # csv reader
# # 注意此处的打开方式
# rf = open('pingan.csv', 'r')
# reader = csv.reader(rf)
# # 注意此处的调用方法
# print(reader.__next__())
#
#
# # csv writer
# wf = open('pigan_copy.csv', 'w')
# writer = csv.writer(wf)
# writer.writerow(['2017-01-09', '9.13', '9.17', '9.11', '9.15', '36108100', '9.15'])
# writer.writerow(reader.__next__())
# wf.flush()


import csv

with open('pingan.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'w') as wf:
        writer = csv.writer(wf)
        headers = reader.__next__()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)
print('end')
