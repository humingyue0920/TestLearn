import unittest
from Base.requests_demo_copy import RunMain
import json


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'hu',
            'password': '123'
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        res = json.loads(res)
        print(res)
        # if res['mobile'] == '123':
        #     print("测试通过")
        # else:
        #     print("测试失败")
        self.assertEqual(res['mobile'], '123', '测试失败')

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'mingyue',
            'password': '123456'
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        res = json.loads(res)
        print(res)
        # if res['mobile'] == '123':
        #     print("测试通过")
        # else:
        #     print("测试失败")
        self.assertEqual(res['mobile'], '123', '测试失败')


if __name__ == '__main__':
    unittest.main()
