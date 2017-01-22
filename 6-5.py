# -*- coding: UTF-8 -*-

# 如何读写Excel文件

import xlrd, xlwt


# # read
# book = xlrd.open_workbook('demo.xlsx')
# sheets = book.sheets()
#
# sheet = book.sheet_by_index(0)
# print(sheet)
#
# cell = sheet.cell(0, 0)
# print(cell, sheet.nrows, sheet.ncols)
#
# print(cell.ctype, cell.value)
# print(sheet.row(1))
# print(sheet.row_values(1, 1))
#
# # write
# wbook = xlwt.Workbook()
# wsheet = wbook.add_sheet('sheet1')
# wsheet.write()
# wbook.save('wbook65.xlsx')

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '拷贝', None)
for row in range(1, rsheet.nrows):
    text = rsheet.row_values(row, 1, 2)
    print(text)
    rsheet.put_cell(row, nc, xlrd.XL_CELL_TEXT, text, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output65.xlsx')
