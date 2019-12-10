"""
封装获取caseExcel中数据的整体思路
1.导入重构封装Excel
2.重构封装获取Excel的表头
3.也许会操作Excel中引入的外部json文件,导入操作json文件

定义类
构造函数,对导入重构封装Excel的对象进行实例化
定义各个函数获取Excel表格中具体的数据,并对一些数据进行判断
"""
from Base.重构封装Excel import InterfaceCase
from Base.封装获取caseExcel中的第一行 import *
from Base.封装操作json文件 import OperateJson


# 定义类,获取Excelcase中的数据
class GetCasedata():
    # 定义构造函数对导入的InterfaceCase类进行实例化
    def __init__(self):
        self.opera_data = InterfaceCase()
        # self.var = GlobalVar()  这个地方不需要实例化了,因为在那个文件中并没有构造函数
        # 思考这个地方是否需要return语句,构造函数不需要return

    # 获取Excel的行数就是case的个数
    def get_case_line(self):
        return self.opera_data.get_line()

    # 获取是否执行
    def get_is_run(self, row):
        # col = self.var.get_is_excute()
        col = GlobalVar.get_is_excute()
        run_model = self.opera_data.get_cell(row, col)
        flag = None
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取是否携带header
    def get_is_header(self, row):
        col = GlobalVar.get_header()
        header = self.opera_data.get_cell(row, col)
        if header == 'yes':
            return GlobalVar.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = GlobalVar.get_request_way()
        request_method = self.opera_data.get_cell(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = GlobalVar.get_url()
        url = self.opera_data.get_cell(row, col)
        return url

    # 获取请求数据
    def get_requestdata(self,row):
        col = GlobalVar.get_parameter()
        request_data = self.opera_data.get_cell(row, col)
        operate_json = OperateJson()
        operate_json.get_value(request_data)

    # 获取预期结果
    def get_expect(self, row):
        col = GlobalVar.get_expection()
        expection = self.opera_data.get_cell(row, col)
        return expection



if __name__ == '__main__':
    se = GetCasedata()
    se.get_case_line()








