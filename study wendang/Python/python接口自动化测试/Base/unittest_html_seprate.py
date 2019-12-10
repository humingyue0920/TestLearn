import unittest
from Base.requests_demo_copy import RunMain
import json
from Base import HTMLTestRunner


class TestDemo(unittest.TestCase):
    global password

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/?username=hu&password=123'
        res = self.run.run_main(url, 'GET')
        print(res)
        res = json.loads(res)
        globals()['password'] = res['password']

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=mingyue&password=123456'
        res = self.run.run_main(url, 'GET')
        print("pass:"+password)
        print(res)



