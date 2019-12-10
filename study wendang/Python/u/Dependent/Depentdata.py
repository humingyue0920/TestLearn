# 定义一个类解决数据依赖问题
from operateExcel.重构封装Excel import InterfaceCase
from Base.post_get基类封装改良版 import SendRequest
from operateExcel.封装获取caseExcel中的数据 import GetCasedata


class DependentData():
    def __init__(self, case_id):
        self.case_id = case_id
        self.operate_excel = InterfaceCase()
        self.run_main = SendRequest()
        self.get_data = GetCasedata()

    # 定义一个方法，通过Excel中case依赖字段获取依赖的整行内容
    def dependent_data(self, case_id):
        row_data = self.operate_excel.get_rows_data(case_id)
        return row_data

    # 定义一个方法，执行依赖行
    def excute_dependent(self, case_id):
        row = self.operate_excel.get_row_num(case_id)
        url = self.get_data.get_url(row)
        request_method = self.get_data.get_request_method(row)
        request_data = self.get_data.get_json(row)
        header = self.get_data.get_is_header(row)
        res = self.run_main.run_main(request_method, url, request_data, header)
        return res



# if __name__ == '__main__':
#     run = DependentData()
#     print(run.dependent_data('test_01'))
