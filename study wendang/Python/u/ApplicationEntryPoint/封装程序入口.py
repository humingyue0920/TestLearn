# coding:utf-8
from operateExcel.封装获取caseExcel中的数据 import GetCasedata
from Base.post_get基类封装改良版 import SendRequest
from Base.结果对比封装 import CommonComparision
from operateExcel.重构封装Excel import InterfaceCase


# 定义一个主函数入口类
class EntryPoint():
    # 定义一个构造函数对导入的类实例化成对象
    def __init__(self):
        self.get_casedata = GetCasedata()
        self.send_request = SendRequest()
        self.comm_comparision = CommonComparision()
        self.write_data = InterfaceCase()

    # 定义程序入口主函数
    def run_main(self):
        res = None
        # 获取Excel中用例的行数
        rows_count = self.get_casedata.get_case_line()
        # 定义一个循环函数，获取整个函数的数据
        for i in range(1, rows_count):
            url = self.get_casedata.get_url(i)
            request_method = self.get_casedata.get_request_method(i)
            request_data = self.get_casedata.get_json(i)
            header = self.get_casedata.get_is_header(i)
            is_run = self.get_casedata.get_is_run(i)
            expection = self.get_casedata.get_expect(i)
            if is_run:
                # method, url, data=None, header=None
                res = self.send_request.run_main(request_method, url, request_data, header)
                # print(res)
                # return res
                if self.comm_comparision.is_contain(expection, res):
                    self.get_casedata.write_result(i, 'pass')
                else:
                    self.get_casedata.write_result(i, 'fail')

        return res


if __name__ == '__main__':
    run = EntryPoint()
    run.run_main()
