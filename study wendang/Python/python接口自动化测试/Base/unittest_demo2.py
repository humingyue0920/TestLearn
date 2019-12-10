import unittest
from Base.requests_demo import RunMain
import json


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/?username=护肤&password=护肤'
        data = {
            'username': 'hu',
            'password': '123'
        }
        res = RunMain(url, 'post', data)
        res = json.loads(res,ensure_ascii=False, indent=2, sort_keys=True)
        print(res)

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=护肤&password=护肤'
        data = {
            'username': 'mingyue',
            'password': '123456'
        }
        res = RunMain(url, 'post', data)
        res = json.loads(res, ensure_ascii=False, indent=2, sort_keys=True)
        print(res)


if __name__ == '__main__':
    unittest.main()
