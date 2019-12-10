"""
第一课  枚举本质是一个类
如何在Python中创建枚举类型
1.导入enum模块中的枚举类   2.新建类继承Enum父类  3.在类中创建枚举
枚举在Python中的本质还是一个类
枚举类和普通类的区别：通过调用可以看出来
枚举调用得到的是标签，而普通类调用得到的是数值，枚举的意义重在标签而不是数值
枚举类中不能将两个标签定义为同一个数值
"""
from enum import Enum


class VIP(Enum):
    YELLOW = 1   # 建议在枚举中的标签大写
    GREEN = 2
    BLACK = 3
    RED = 4
    BLUE = 4  # 这段代码并不会报错，但是BLUE相当于是RED的别名


class Common():
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)   # VIP.YELLOW
print(Common.YELLOW)  # 1

"""
第二课 枚举类和普通类的区别
"""
# 如果没有枚举类，我们如何表示枚举
yellow = 1
green = 2

a = {'yellow': 1, 'green': 2}


class Common():
    YELLOW = 1
    GREEN = 2

# 以上代码为什么不能表示枚举，只有枚举类能表示枚举，两点非常重要的原因
# 1.可变 其他类型都是可变，枚举类不可变   2.没有防止相同标签的功能


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    # YELLOW = 5  # 这句代码会报错，因为定义了相同标签


a['yellow'] = 3
print(a)  # {'yellow': 3, 'green': 2}
Common.YELLOW = 3
print(Common.YELLOW)  # 3
# VIP.YELLOW = 3  # 这段代码报错，因为是不可变类型
# print(VIP.YELLOW)


"""
第三课 枚举的相关操作
1.如何获取枚举类型下标签的值
print(VIP.Yellow.value)
2.如何获取标签的名字
print(VIP.Yellow.name)
3.VIP.Yellow与VIP.Yellow.name的区别,类型不同
4.枚举类型 枚举标签 枚举值
5.枚举其实是可以遍历的
"""


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(type(VIP.YELLOW))  # <enum 'VIP'>
print(type(VIP.YELLOW.name))  # <class 'str'>


for x in VIP:
    print(x)


"""
第四课 枚举的运算符比较
枚举只能进行等值比较,不支持大小比较,支持身份比较
同一个类下的比较
不同类下的比较
枚举注意事项:枚举下面不能有两个相同的标签名,标签名对应的值可以相同,其实相当于是
别名
当枚举类中包含标签名的数值相同时,遍历时不会将别名打印
假如我们想要将别名打印出来可以利用__members__.item(),打印出来结果的类型是元组
"""


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP1(Enum):
    YELLOW = 1
    GREEN = 1


# 同一个类下的比较
result1 = VIP.YELLOW == VIP.BLACK
result2 = VIP.GREEN == VIP.GREEN
result3 = VIP.GREEN == 2
# result4 = VIP.YELLOW < VIP.GREEN  # TypeError: '<' not supported between instances of 'VIP' and 'VIP'
result5 = VIP.GREEN is VIP.GREEN
print(result1, result2, result3, result5) # False True False True

# 不同类下的比较
result = VIP.YELLOW == VIP1.YELLOW
print(result)  # False
print(VIP1.GREEN)  # VIP1.YELLOW
# 说明Green = 1 相当于是yellow的别名 等价于 Yellow_alise = 1


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    Blue = 1


for x in VIP:
    print(x)  # VIP.Blue不会被打印

for y in VIP.__members__.items():
    print(y)
    print(type(y))
"""
('YELLOW', <VIP.YELLOW: 1>)
<class 'tuple'>
('GREEN', <VIP.GREEN: 2>)
<class 'tuple'>
('BLACK', <VIP.BLACK: 3>)
<class 'tuple'>
('RED', <VIP.RED: 4>)
<class 'tuple'>
('Blue', <VIP.YELLOW: 1>)
<class 'tuple'>
"""

for z in VIP.__members__:
    print(z)
    print(type(z))
"""
YELLOW
<class 'str'>
GREEN
<class 'str'>
BLACK
<class 'str'>
RED
<class 'str'>
Blue
<class 'str'>
"""


"""
第五课 枚举转换
假如数据库想要存储枚举值 就需要进行枚举转换,利用枚举类(变量)即可
假如我们想枚举类型下面的值只能是数字类型的,可利用 from Enum import intenum
假如我们希望每个枚举类型不能有相同的值,可利用from Enum import intenum,unique
对于枚举我们不能实例化,单例模式
"""
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


a = 1
print(VIP(a))  # VIP.YELLOW 用此种方法即可


"""
闭包
一个函数的参数可以传递到另外一个函数里
把一个函数当做另外一个函数的返回结果
"""


def a():
    pass


print(type(a))  # <class 'function'>


def a():
    def b():
        print('-----------')
    return b  # 把一个函数当做另外一个函数的返回结果，注：不要加小括号


# b()  #NameError: name 'b' is not defined
# 直接在外部调用内部函数，代码报错,b()函数的作用域仅仅在a()函数内部
f = a()  # 将一个函数赋值给变量
# 这句代码的逻辑是：调用a函数，得到return语句中的b
f()  # 相当于b（）
print(f())


def current_crb():
    a = 25  # 环境变量，必须定义在内部函数外部

    def curve(x):
        return a * x * x
    return curve


a = 10  # a的值不受这行代码影响 闭包
f = current_crb()
f(2)
print(f(2))
print(f.__closure__)
print(f.__closure__[0].cell_contents)

# 闭包 = 函数 + 环境变量 封闭后不受外部变量影响
# 闭包的环境变量实际上保存在__closure__内置变量中


"""
一个事例卡闭包  闭包的经典误区
闭包的意义保留现场
注意以下代码的返回结果，搞懂
闭包函数内部对a重新复制，值会被改变吗   不会，局部变量不会影响到外部变量
思考：以下代码是闭包吗，利用__closure__变量可查看，不是的原因，在内部定义了相同名称的环境变量
"""


def f1():
    a = 10

    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)


f1()
"""
10
20
10
"""


def f1():
    a = 10

    def f2(y):
        a = 20
        y = a * x
    return f2


f = f1()
print(f.__closure__)


"""
一个问题用非闭包来解决
注意：global origin
"""


origin = 1


def go(step):
    global origin
    new_pos = step + origin   # 这段代码报错，表示局部变量没有定义，但是如果我们将origin = new_pos注释后代码就不报错了
    # 思考这是为什么
    # 暂时理解为在局部变量调用全局变量时无所谓，但一旦需要操作全局变量时，需要先将它声明为全局变量
    # origin = new_pos
    origin = new_pos
    return origin


# 或者用这种方法
class Origin():
    origin = 1

    def go(self, step):
        self.step = step
        new_pos = step + self.__class__.origin
        self.__class__.origin = new_pos
        return self.__class__.origin


result1 = Origin()
print(result1.go(2))
print(result1.go(3))
print(result1.go(6))


"""
用闭包的方法来解决
注意;nonlocal
"""


def start():
    origin = 0

    def go(step):
        nonlocal origin
        new_step = step + origin
        origin = new_step
        return origin
    return go


f = start()
f = start()
print(f(2))
print(f.__closure__[0].cell_contents)
print(f(3))
print(f.__closure__[0].cell_contents)
print(f(6))
print(f.__closure__[0].cell_contents)

# 另一种方法
origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))