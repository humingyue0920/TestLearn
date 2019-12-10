import unittest
from Base.requests_demo_copy import RunMain
from Base.mock_reconfig import mock_reconfig
import json


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/?username=hu&password=123'
        data = {
            'username': 'hu',
            'password': '123'
        }
        res = mock_reconfig(data, self.run.run_main, url, 'GET', data)
        # res = self.run.run_main(url, 'GET', data)
        self.assertEqual(res['password'], '123', '测试失败')

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=mingyue&password=123456'
        data = {
            'username': 'mingyue',
            'password': '123456'
        }
        res = self.run.run_main(url, 'GET', data)
        print(res)
        res = json.loads(res)
        self.assertEqual(res['password'], '123456', '测试失败')


if __name__ == '__main__':
    unittest.main()
