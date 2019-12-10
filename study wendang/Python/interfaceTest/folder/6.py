# 表达式
# 表达式的定义:表达式是由一系列运算符和操作符所组成的序列
# 思考题:计算 a + b * c 和 a or b and c
a = 1
b = 2
c = 3
print(a+b * c)  # 7
print(a or b and c)  # 3 按从左到右的顺序计算,若and的优先级高于or则结果1
# 返回的结果为1,实际证明and的优先级高于or,由此引出表达式的优先级
# 表达式的优先级
# 同级表达式之间的优先级自己研究,当not和and及or在一起运算时，优先级为是not>and>or
a = 1
b = 2
c = 2
print(not a or b + 2 == c)
# 此表达式的优先级排序为((not a) or ((b + 2) == c)) #False
# 在Windows下运行python脚本
# 注:用cmd打开,进入相应命令运行脚本,之前一直失败是因为当时直接python解释器打开,所以运行失败
# 注释方式  1.单行注释"#"   2.多行注释 """ ..."""
# 条件语句
# 判断用户输入用户名与密码是否一致,若一致则输出登录成功,否则提示请输入正确的用户名和密码
account = '15555877052'
password = 'hu123456'

user_account = input('please input account:')
user_password = input('please input password:')
if account == user_account and password == user_password:
    print('登录成功')
else:
    print('密码错误')

a = 257
b = 257
print(a is b)  # True
a = 123
b = 123
print(a is b)  # True
# 此处重点解释一下python中is和==(is not和!=)的区别
'''
is用于判断两个变量的引用对象是否为同一个,==用于判断引用变量的值是否相等,类似于java的equal()和==
反之,is not用于判断两个变量是否引用不同的对象,而!=判断两个引用变量的值是否不等
'''
# 整数的比较
x = 5
y = 5
print(x == y)  # True
print(x is y)  # True
print(id(x))
print(id(y))
# 字符串的比较
x = 'abc'
y = 'abc'
print(x == y)  # True
print(x is y)  # True
print(id(x))
print(id(y))
# list列表的比较
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
print(x is y)  # False
print(id(x))
print(id(y))
# tuple元组的比较
x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)  # True
print(x is y)  # False
print(id(x))
print(id(y))
# dict字典的比较
x = {'id': 1, 'name': 'Hu', 'age': 26}
y = {'id': 1, 'name': 'Hu', 'age': 26}
print(x == y)  # True
print(x is y)  # False
print(id(x))
print(id(y))
# set集合的比较
x = {1, 2, 3}
y = {1, 2, 3}
print(x == y)  # True
print(x is y)  # False
print(id(x))
print(id(y))
# 赋值后比较
x = {1, 2, 3}
y = x
print(x == y)  # True
print(x is y)  # True
print(id(x))
print(id(y))
# 总结:如果引用变量为int或str,且值相同,则x is y是True,否则为False
# 当字符串中含有特殊字符时,也是True
x = 'abc$'
y = 'abc$'
print(x == y)  # True
print(x is y)  # True
print(id(x))
print(id(y))

# 嵌套if else
a = input('请输入a的值:')
print(type(a))
if a == 1:
    print('apple')
else:
    if a == 2:
        print('orange')
    else:
        if a == 3:
            print('banana')
        else:
            print('go shopping')
# 解决为什么输入什么,返回的结果都是go shopping
# 原因是因为你输入的虽然是1,但是类型是str,原因是input()函数,其接受任意输入, 将所有输入默认为字符串处理,并返回字符串类型
# 思考如何输入int类型的1,使用int()函数(将变量转换为十进制数,所以此处只能输入数字,否则代码报错)
# 引入elif
a = input('请输入a的值:')
print(type(a))
a = int(a)
print(type(a))
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('bnana')
else:
    print('go shopping')

# 写一段代码要求用户只能输入数字类型
a = input('请输入数字类型的值:')
try:
    a = int(a)
    if a == 1:
        print('apple')
    elif a == 2:
        print('orange')
    elif a == 3:
        print('bnana')
    else:
        print('go shopping')
except ValueError:
    a = input('只能输入数字,请重新输入:')
