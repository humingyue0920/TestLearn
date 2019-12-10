import xlrd
from xlutils.copy import copy


# 定义用例类
class InterfaceCase():
    # 定义构造方法,判断是否传入sheet_id和Excel文件地址
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r'C:\Users\13254\PycharmProjects\u\interfaceCase\interfaceCase.xls'
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

    # 添加写入Excel数据方法
    """
    1.利用xlrd.open_workbook读取文件
    2.利用xlutils.copy下的copy方法复制一份文件
    3.获取这份文件中第ID个表格数据
    4.在这个表格下利用write函数写入value值
    5,。将这份文件保存，利用save函数
    """
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseID找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    """
    这个函数我有点不是很明白，这个地方为什么要搞一个col_data
    是否可以直接将这个省去
    后明白，不能将此省去，原因省去后无法将num自加，for col_data in cols_data代表遍历循环这列的每一个数据
    """
    # 根据caseID获取行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1
        return num

    # 根据行号获取该行的内容
    def get_row_value(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一整列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


# if __name__ == '__main__':
#     run = InterfaceCase()
#     # print(run.get_sheet())
#     # print(run.get_line())
#     # print(run.get_cell(2,3))
#     # run.write_value(1, 8, 'pass')
#     print(run.get_rows_data('test_01'))



