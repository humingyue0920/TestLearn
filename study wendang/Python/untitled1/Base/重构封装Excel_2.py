import xlrd


# 定义用例类
class InterfaceCase():
    # 定义构造方法,判断是否传入sheet_id和Excel文件地址
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'E:\python接口自动化测试\interfaceCase\interfaceCase.xlsx'
            self.sheet_id = 0
        self.data = self.get_sheet()

    # 定义函数获得表格的所需要的sheet表格,是一个对象
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取所传入表格的行数
    def get_line(self):
        tables_line = self.data.nrows
        return tables_line

    # 获取所传入表格具体的某一行某一列
    def get_cell(self, row, cell):
        tables_cell = self.data.cell_value(row, cell)
        return tables_cell


if __name__ == '__main__':
    run = InterfaceCase()
    print(run.get_sheet())
    print(run.get_line())
    print(run.get_cell(2,3))



