import unittest
from Base.unittest与requests封装结合使用_requests import SendRequests


class UnittestCase(unittest.TestCase):

    def setUp(self):
        self.run = SendRequests()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'hu',
            'password': '123'
        }
        res = self.run.run_main('post', url, data)


    def test_02(self):
        url = 'http://127.0.0.1:8000/loginout/?username=123&password=455'
        res = self.run.run_main('get', url)
        print(res)


if __name__ == '__main__':
    unittest.main()
