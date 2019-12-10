# 函数:分为自定义函数和内置函数 内置函数如:print(),round(),如何快速查看内置函数
# 的功能可使用help(round)查看帮助文档
# 其中,round(a,2)表示对变量a保留2位小数,并且会四舍五入
a = 1.1314527
result1 = round(a, 2)
result2 = round(a, 4)  # 会四舍五入
print(result1, result2)  # print打印多个变量时可采用此种方法,在同一行打印
help(print)  # 查看帮助文档
# 函数的好处:1.功能性  2.隐藏细节 3.避免编写重复写代码

# 自定义函数,函数需要先定义再调用
# 函数基本结构,注:def是定义函数关键字,parameter_list可省略,代码块可以使用return返回结果,若不加return则代表返回的是None
# def funcname(parameter_list):
#    pass
# 1.实现两个数字的相加   2.打印输入参数
# 遇到问题:代码报提示PEP:8 expected 2 blank lines ，found 1"
# 解决办法:这句话的意思是“有两个空白行，但是没有发现。”,在声明函数的那一行的上方必须有两行的空行，否则便出现这个情况


def add(x, y):
    result = x + y
    return result  # 此处必须有return语句,否则这段代码没有意义
# 调用函数


# add(1, 2)  # python传入参数的方式按照入参的顺序来,不会打乱
# print(result)  #这段代码会报错
# 解决办法
a = add(1, 2)
print(a)

"""
以上代码可以简化为
def add(x, y):
    return x + y


print(add(1,2))
"""


# def print(code):
#    print(code)  # 此处不需要return,因为本身就是打印,没必要使用return返回结果


# print('Python') # 这段代码运行是会报错的,因为自己调用自己,递归次数最大987次,根本原因是定义了一个与内置函数一样的自定义函数
# 解决办法,修改函数名即可
def print_code(code):
    print(code)


print_code('Python')
# 引入小知识点,如何设置最大的递归次数
# import sys
# sys.setrecursionlimit(10000)


# 两段代码结合使用
def add(x, y):
    result = x + y
    return result


def print_code(code):
    print(code)


a = add(1, 2)
b = print_code('Python')
print(a, b)
# 返回结果是Python
# 3 None  思考为什么返回这个结果,先调用print_code方法,里面有一个打印,所以先返回Python,随后a = 3,b没有return所以返回None
# 以前print都是打印一个结果,其实print可以传多个参数,不换行打印,
# 如:print(a,b,c ,d,.....)


# 实验能否使用input()函数接收用户输入的变量,可以,用以下函数即可
def add(x, y):
    result = x + y
    return result


c = int(input('please input num x:'))
d = int(input('please input num y:'))


a = add(c, d)
print(a)


# return语句的补充说明,当函数代码内部一旦遇到return,return后面的语句将不会被执行
def print_code(code1, code2):
    print(code1)
    return
    print(code2)


print_code('hello', 'world')  # world不会被打印


# return多个参数时,用逗号隔开即可
def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 3 + 10
    return damage1, damage2


# 当你用一个变量接收到元组之后,如何使用结果
def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 3 + 10
    return damage1, damage2


damages = damage(2, 3)
print(type(damages))  # <class 'tuple'>
print(damages[0], damages[1])  # 这种依靠序号来访问变量的方法是非常非常不推荐的


# 可以采用序列解包的方式
def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 3 + 10
    return damage1, damage2


damages_sill1, damages_skill2 = damage(2, 3)
print(damages_sill1, damages_skill2)


# 序列解包
a = 1
b = 2
c = 3
# 以上代码可以简化成如下代码
a, b, c = 1, 2, 3
# 以上代码是否可以简化成一行,是可以的
d = 1, 2, 3
print(type(d))  # tuple
a, b, c = d  # 这就叫一个序列解包
# 注:序列解包时元素要相等
a = 1
b = 1
c = 1
# 简化 a,b,c = 1 ,还可以简化成以下代码
a = b = c = 1

"""
函数的参数列表种类
1.必须参数:在参数列表中定义的参数,在调用时必须传入参数
2.关键字参数:可以告诉函数明确指定参数值给哪个参数,无序,意义在于方便,增强代码的可读性
3.默认参数:
必须参数与关键字参数的区别在于函数的调用而不在于函数的定义上
函数在定义时传入的参数叫做形参,在调用时传入的参数叫做实参
"""


def add(x, y):  # x,y叫做形参
    result = x + y
    return result


a = add(1, 2)  # 1,2叫做实参
print(a)
b = add(y=3, x=4)  # 关键字参数
print(b)


# 若参数列表需要传递15个参数,引入默认参数(实际操作中不可取,可将15个参数封装成对象,此处仅举例)引出默认参数
def print_student_file(name, age=7, sex='男', college='人民小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+sex+'生')
    print('我在'+college+'上学')


print_student_file('小张')
print('------------------')
# 只改变年龄
print_student_file('小胡', age=6)
# 改变年龄和性别,并且不按照默认顺序传递,是否可行,实验证明不可行
# print_student_file('小胡', '女', 7)
print('------------------')
print_student_file('小胡', 7, '女',)
print('------------------')
print_student_file('小胡', 7, sex='女',)
# print_student_file('小胡', age=7, '女', college = '光明小学')  代码报错,因为在调用时同样不能非默认参数在默认参数后面
"""
默认参数用法总结
1.在定义的时候不能将非默认参数放在默认参数后面
比如:def print_student_file(name, age=7, sex='男', college='人民小学',teacher)这种写法是错误的
2.在调用的时候必须参数必须要传,默认参数可以不传
3.在调用时若不使用关键字参数,必须按照默认参数顺序传递参数,是按照形参和实参一一对应的
4.在调用时可以使用关键字参数,可以不遵守顺序
5.在调用时同样不能非默认参数在默认参数后面
比如:print_student_file('小胡', age=7, '女', college = '光明小学')
"""











