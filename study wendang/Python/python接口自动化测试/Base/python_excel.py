import xlrd

# 利用xlrd.open_workbook()获取excel存放地址
data = xlrd.open_workbook(r'../interfaceCase/interfaceCase.xlsx')
# 利用data.sheets()获取第一个sheet,是一个对象
tables = data.sheets()[0]
# 利用data.sheet_names()获取sheet的名字
print(data.sheet_names())
# 打印行数
print(tables.nrows)
# 打印具体的某一行某一列（都是从0算起）
print(tables.cell_value(2, 3))