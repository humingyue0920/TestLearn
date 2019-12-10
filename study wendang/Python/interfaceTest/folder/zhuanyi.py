# coding=utf-8
# 读取excel内容
import xlrd


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = self.file_name
            self.sheet_id = self.sheet_id

        else:
            self.file_name = r'E:\python接口自动化测试\interfaceCase\interfaceCase.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_data().nrows)
    print(opers.get_lines())
    print(opers.get_cell_value(1, 3))