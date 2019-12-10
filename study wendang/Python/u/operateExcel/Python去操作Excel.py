import xlrd
# 获取Excel用例的存放地址
data = xlrd.open_workbook('E:\python接口自动化测试\interfaceCase\interfaceCase.xlsx')

# 获取表格名称
tables_name = data.sheet_names()

# 获取第一个sheet的名称
tables = data.sheets()[0]

# 获取表格的行数
tables_line = tables.nrows

# 获取具体的某一行某一列
tables_cell = tables.cell_value(2, 3)

print(tables_name, tables_line, tables_cell, tables)
