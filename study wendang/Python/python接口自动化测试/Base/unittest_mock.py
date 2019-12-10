import unittest
from Base.requests_demo_copy import RunMain
import mock


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'hu',
            'password': '123'
        }
        mock_data = mock.Mock(return_value=data)
        print(mock_data)
        self.run.run_main = mock_data
        res = self.run.run_main(url, 'GET', data)
        print(res)
        self.assertEqual(res['password'], '123', '测试失败')

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=mingyue&password=123456'
        data = {
            'username': 'mingyue',
            'password': '123456'
        }
        self.run.run_main = mock.Mock(return_value=data)
        res = self.run.run_main(url, 'GET', data)
        print(res)
        self.assertEqual(res['password'], '123456', '测试失败')


if __name__ == '__main__':
    unittest.main()