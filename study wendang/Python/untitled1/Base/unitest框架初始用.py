import unittest


class UnittestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('程序开始前只执行一次')

    @classmethod
    def tearDownClass(cls) -> None:
        print('程序结束时执行一次')

    def setUp(self):
        print('每个case之前执行')

    def tearDown(self):
        print('每个case结束时执行')

    def test_01(self):
        print('这是第一个case')

    def test_02(self):
        print('这是第二个case')


if __name__ == '__main__':
    unittest.main()


