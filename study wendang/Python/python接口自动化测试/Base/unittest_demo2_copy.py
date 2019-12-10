import unittest
from Base.requests_demo_copy import RunMain
import json


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/?username=hu&password=123'
        # data = {
        #     'username': 'hu',
        #     'password': '123'
        # }
        res = self.run.run_main(url, 'GET')
        print(res)
        # print(type(res))
        # print(json.loads(res))
        # print(type(json.loads(res)))

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=mingyue&password=123456'
        # data = {
        #     'username': 'mingyue',
        #     'password': '123456'
        # }
        res = self.run.run_main(url, 'GET')
        print(res)


if __name__ == '__main__':
    unittest.main()
