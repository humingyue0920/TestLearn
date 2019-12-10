"""
第一课 匿名函数
由普通函数引出匿名表达式
使用关键词lambda parameters_list: expression
注：expression部分只能使用表达式，不能使用完整的代码语句
注：此处只是引入匿名函数的概念，故举出此列子，实际使用中完全不推荐这么用，未体现匿名函数的优势
"""


# 普通函数
def add(x, y):
    return x + y


print(add(1, 2))


# 匿名函数
f = lambda x, y: x + y  # 将结果赋值给变量
# f = lambda x, y:a = x + y   这段代码报错
print(f(1, 2))


"""
题目:取两个数中的最大值
题目:取三个数中最小的值
题目:比较n个数中最大值

"""


# 题目:取两个数中的最大值
def maxnum(x, y):
    if x > y :
        print(x)
    else:
        print(y)


maxnum(3, 4)


# 题目:取三个数中最小的值
def minnum(x, y, z):
    if x < y:
        min1 = x
        if z > min1:
            print("最小的数为-----"+str(min1))
        else:
            print("最小的数为-----"+str(z))
    else:
        min1 = y
        if z > min1:
            print("最小的数为-----" + str(min1))
        else:
            print("最小的数为-----" + str(z))


minnum(1,2,3)


# 题目:比较n个数中最大值
x = [1, 2, 3, 4, 5]
j = 0
max1 = 0
for j in range(0, len(x)):
    if x[j] > max1:
        max1 = x[j]
print("最大的值为======="+str(max1))


"""
三元表达式
其它语言中的三元表达式 x > y ? x : y
python中的三元表达式 条件为真时的返回结果 if 判断语句 else 条件为假时的返回结果
三元表达式经常会用在lambda表达式中
"""


x = 1
y = 2
# x if x > y else y  # 这仅仅是一个表达式,不是语句
r = x if x > y else y
print(r)


"""
函数式编程
map(function, iterable, ...)
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次
function 函数返回值的新列表
map与lambda结合使用
"""
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x  # 注：此处要有返回值


r = map(square, list_x)  # map的作用就是将list_x中每个元素都执行一遍square函数，这里的函数不要加小括号
print(r)
print(list(r))  # 将r由对象转换为list

# 以上代码可以简化为
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = map(lambda x: x * x, list_x)
print(list(r))

# 当lambda的入参为两个时,map的参数用逗号隔开即可
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

# 当map的两个入参的长度不一致时,最后的结果取决于较短的那一个参数
list_x = [1, 2, 3, 4, 5, 6]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

"""
reduce函数
使用前需先导入 from functools import reduce
reduce 的作用:连续计算,连续调用lambda
注:reduce函数中的lambda必须要有两个入参
"""
from functools import reduce
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x + y, list_x)
print(r)
# 在以上代码中,程序并没有报错,最开始以为lambda中的参数有两个,reduce函数中的参数列表也必须有两个,其实不然
# reduce的逻辑其实是将list_x前两个参数分别当成x,y,计算得出的结果再作为x,第3个参数作为y,以此类推
# reduce函数还有一个参数初始值,默认是0,我们可以未其赋值,注意运行的逻辑
# 第一个计算的初始值就是设定的值
# 从以下代码可以看出
list_x = ['1', '2', '3', '4', '5', '6', '7', '8']
r = reduce(lambda x, y: x + y, list_x, 'aaa')
print(r)  # aaa12345678


"""
filter
filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个序列，函数 f 的作用是对每个元素进行判断，
返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新的序列Iterator
题目一:去除一个序列中的偶数
题目二:剔除所有小写字母

"""


# 题目一:去除一个序列中的偶数,方法一
list_x = [1, 4, 6, 7, 9, 12, 17]


def is_odd(x):
    return x % 2 == 1


r = filter(is_odd, list_x)
print(list(r))


# 题目一:去除一个序列中的偶数,自己写的改了很多遍
# 注意事项 1.定义的函数要有返回值,否则打印的结果为空 2.filter调用ou()函数时,不要加小括号
list_x = [1, 4, 6, 7, 9, 12, 17]


def ou(x):
    if x % 2 == 1:
        return x


r = filter(ou, list_x)
print(r)
print(list(r))


# 题目一:去除一个序列中的偶数,方法三
list_x = [1, 4, 6, 7, 9, 12, 17]
r = filter(lambda x: x % 2 == 1, list_x)
print(list(r))


# 题目二:剔除所有大写字母
list_x = ['a', 'A', 'B', 'c']
r = filter(lambda x: x.islower(), list_x)
print(list(r))


"""
函数式编程与命令式编程
装饰器
"""
# 打印当前时间 导入time模块,调用该模块下的time()函数
import time


def f1():
    print(time.time())  # 打印出来的结果是时间戳
    print('this is function')


def f2():
    print(time.time())  # 打印出来的结果是时间戳
    print('this is function')


f1()
f2()

# 要求所有的函数都带有打印时间的函数该如何操作
# 对修改是封闭的,对扩展是开放的
import time


def f1():
    print('this is function1')


def f2():
    print('this is function2')


def print_time(func):
    print(time.time())
    func()


print_time(f1)  # 注:此处的调用f1不能加小括号,原因是print_time里写了func()
print_time(f2)
# 这样的代码是并不推荐的.相当于是强行给f1和f2加一个打印时间,与以下代码并没有什么区别
print(time.time())
f1()
print(time.time())
f2()
# 那么如何可以实现业务功能又可以简化代码呢,此处引入装饰器
import time


def decorater(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper()  # 这个地方return的是wrapper(),假如return的是wrapper,见以下代码


def f1():
    print('this is function')


decorater(f1)

# 返回的是wrapper
import time


def decorater(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


def f1():
    print('this is function')


f = decorater(f1)
f()
# 以上代码还是非常的麻烦,有没有什么方法可以实现我们调用f1后直接打印时间呢
# 有,在调用函数前加@加装饰器名称即可
# 加入装饰器后的第一种代码,不推荐此种方法,加入
import time


def decorater(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper()  # 这个地方return的是wrapper(),假如return的是wrapper,见以下代码


@decorater
def f1():
    print('this is function')


f1

# 第二种方法
import time


def decorater(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorater
def f1():
    print('this is function')


f1()


# 当被装饰的函数中有入参,以下代码看似解决了问题，但若有两个入参或者更多，此种方法就不适用了
# 此处引入可变参数列表*args
import time


def decorater(func):
    def wrapper(fun_name):
        print(time.time())
        func(fun_name)
    return wrapper

@decorater
def f1(fun_name):
    print('this is function: '+fun_name)


f1('dj')


# 当被装饰函数的入参有多个时
import time


def decorater(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper


@decorater
def f1(fun_name):
    print('this is function: '+fun_name)


@decorater
def f2(func_name1, func_name2):
    print('this is function: ' + func_name1)
    print('this is function: ' + func_name2)


f1('dj')
f2('类方法','实例方法')


# 当被装饰函数的入参包含关键字参数时
# 当被装饰函数入参包含关键字参数时，不加@decorator时，打印的结果是不包错的，但加上@decorator后，代码报错，说明*args是
# 不支持关键字参数的，所以我们需要在入参中也加入关键字参数,代码如下
import time


def decorater(func):
    # key word
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorater
def f1(fun_name):
    print('this is function: '+fun_name)


@decorater
def f2(func_name1, func_name2):
    print('this is function: ' + func_name1)
    print('this is function: ' + func_name2)


@decorater
def f3(func_name1, func_name2, **kw):
    print('this is function: ' + func_name1)
    print('this is function: ' + func_name2)
    print(kw)


f1('dj')
f2('类方法', '实例方法')
f3('类方法', '实例方法', a=1, b=2)
