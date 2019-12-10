from Base import HTMLTestRunner
import unittest
from Base.unittest_html_seprate import TestDemo
import os
import time

current_path = os.getcwd()
cash_path = os.path.join(current_path, "TestCase")
report_path = os.path.join(current_path, "Report")

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))

    # 报告地址&名称
    # report_title = 'Example报告.html'
    report_title = 'Example报告' + now + ".html"
    result_path = os.path.join(report_path, report_title)
    print(report_path)

    # 报告描述
    desc = '用于展示修改样式后的HTMLTestRunner'

    testsuite = unittest.TestSuite()
    testsuite.addTest(TestDemo('test_01'))
    testsuite.addTest(TestDemo('test_02'))

    with open(result_path, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='自动化测试报告', description='详细测试用例结果')
        runner.run(testsuite)

