import unittest
from Base.unittest与requests封装结合使用_requests import SendRequests
import json


class UnittestCase(unittest.TestCase):
    global user_name

    def setUp(self):
        self.run = SendRequests()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'hu',
            'password': '123'
        }
        res = self.run.run_main('post', url, data)
        res = json.loads(res)
        globals()['user_name'] = res['user_name']

    def test_02(self):
        url = 'http://127.0.0.1:8000/loginout/?username=123&password=455'
        res = self.run.run_main('get', url)
        print(res)
        print('username:'+user_name)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(UnittestCase('test_01','test_02'))
    unittest.TestRunner.run(suite)