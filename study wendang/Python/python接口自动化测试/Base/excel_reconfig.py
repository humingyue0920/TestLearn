# coding = utf-8
# 读取Excel内容
import xlrd


# 定义类 获取Excel路径和表id 判断
class InterfaceCase:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r'..\interfaceCase\interfaceCase.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

# 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

# 获取单元格的行数
    def get_rows(self):
        table_rows = self.data.nrows
        return table_rows
        # tables = self.data
        # return tables.nrows

# 获取某一个单元格的内容
    def get_cell(self, m, n):
        table_cells = self.data.cell_value(m, n)
        return table_cells
        # return self.data.cell_value(m, n)


# 程序的入口,打印以上信息
if __name__ == '__main__':
    opers = InterfaceCase()
    print(opers.get_data())
    print(opers.get_rows())
    print(opers.get_cell(2, 3))


