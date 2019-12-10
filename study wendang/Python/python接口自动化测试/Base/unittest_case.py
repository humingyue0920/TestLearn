import unittest
from Base.requests_demo_copy import RunMain
import json


class TestDemo(unittest.TestCase):
    global password

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
        res = json.loads(res)
        globals()['password'] = res['password']

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=mingyue&password=123456'
        # data = {
        #     'username': 'mingyue',
        #     'password': '123456'
        # }
        res = self.run.run_main(url, 'GET')
        print("pass:"+password)

        print(res)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestDemo('test_01'))
    # suite.addTest(TestDemo('test_02'))
    suite.addTest(TestDemo('test_01', 'test_02'))  # 也可以采用这种方式
    unittest.TestRunner().run(suite)

