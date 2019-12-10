import unittest


class TestDemo(unittest.TestCase):  # 此处需继承unittest.TestCase
    # 在类开始之前执行，只执行一次
    @classmethod
    def setUpClass(cls):
        print('在整个类中开始之前只执行一次\n')

    @classmethod
    def tearDownClass(cls):
        print('在整个类中结束时只执行一次')

    # 在每一个测试方法执行之前，都执行该方法
    def setUp(self):
        print('setup---------->，每次方法之前执行')

    # 每次测试方法之后执行
    def tearDown(self):
        print('teardown------------->，在测试方法结束的时候执行')

    def test_01(self):   # 注：此处的方法名命名必须以test开头
        print('这是第一个测试方法')

    def test_02(self):
        print('这是第二个测试方法')


if __name__ == '__main__':
    unittest.main()
