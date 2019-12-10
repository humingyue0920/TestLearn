# while循环
counter = 0
while counter <= 10:
    counter += 1
    print(counter)
# 注：counter要先定义，否则代码会报错
# while与else的结合
counter = 0
while counter <= 10:
    counter += 1
    print(counter)
else:
    print('EOF')


# for循环
a = [1, 2, 3]
for x in a:
    print(x)
# 代码块有一个特性，代码块内部还可以嵌套代码块
# 要求打印出列表的所有元素
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y)
# 此处引入小知识点，如果我们希望打印出列表的所有元素在一行打印出来，该怎么做
# 解决办法：在打印的后面加“，end = ‘’”即可,在python中默认是end = '\n',以什么为结尾
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y, end=',')
# 实验打印列表会怎么样
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    print(x)
# ['apple', 'orange', 'banana', 'grape']
# (1, 2, 3)
# for循环也有和else结合使用的，代表的意思是当列表里的所有元素都被遍历完之后执行该代码块，但在实际情况下很少用到for与else结合使用
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y, end=',')
else:
    print('EOF')  # 最后的EOF被打印

# 强行终止某一段代码 引入break和continue
# 当遍历到2的时候终止循环，break终止当前循环，并且break后的代码不会被执行，continue终止当前条件的循环，继续下面的循环
a = [1, 2, 3]
for x in a:
    if x == 2:
        break
    print(x)  # 只打印1

a = [1, 2, 3]
for x in a:
    if x == 2:
        continue
    print(x)  # 1 3
# for与break和else结合使用，else中的代码块不会被执行,若for循环不是正常退出，而是通过强制退出则不会执行else语句的
a = [1, 2, 3]
for x in a:
    if x == 2:
        break
    print(x)  # 只打印1
else:
    print('EOF')  # 不会被打印
# 思考：如果换成continue，那么else语句是否会被打印出来
# 结果：是会被打印出来的，因为continue相当于正常的将所有元素遍历完
a = [1, 2, 3]
for x in a:
    if x == 2:
        continue
    print(x)  # 只打印1
else:
    print('EOF')  # 会被打印
# 思考：加入break后为什么打印结果是这个
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('EOF')
# 原因：这是一个嵌套循环，break跳出的是内层循环，外层循环还执行，所以打印出1，2，3，相当于正常遍历完所有元素，所以打印出else的代码块

# python中如何像其他语言一样
# for(i= 1,i< 10,i ++){
# }
# python提供range()函数,range(m, n, l)左闭右开,m代表从m开始,n代表结束的元素,l代表步长,其中l可以省略
for x in range(1, 10):
    print(x)  # 从1打印到9
for x in range(1, 10, 2):
    print(x)    # 1,3,5,7,9
# 思考:想打印一个递增的等差数列
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(0, len(a), 2):
    print(x, end=' | ')  # 0|2|4|6|8|
# 由此处可以看出range的第一个元素与序列的起始下标并无关系,仅代表从m开始
# 思考:想打印一个递减的等差数列
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(len(a), 0, -2):
    print(x, end=' | ')
# 打印出a列表相同间隔的元素
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(a), 2):
    print(a[i], end=' | ')  # 1 | 3 | 5 | 7 | 9 |
# 更好的办法,利用切片
b = a[0:len(a):2]
print(b)

# 组织结构
# 暂时理解,包(一个文件夹) -> 模块(一个一个的文件) -> 类 -> 函数,变量(并不是一个组织结构)
# python中如何区分一个普通的文件夹和包呢
# 如果你想让一个文件夹成为包的话,你必须在这个文件夹下面包含一个特定的文件 __init__.py，否则它就是一个普通的文件夹
# 强调__init__.py本身也是一个模块,文件可以为空也可以有代码
# 注:对于一个模块来说命名空间就是包名.模块名，但__init__.py比较特殊，它的命名空间就是folder，就是他的包名
# 从左图结构中可以看出folder，folder2是包，而folder3就是一个普通的文件夹

# 命名空间:为了区分不同包名下相同的模块,一个包下可以有多个模块
# folder.7.py  folder2.7.py
# 一个包下面还可以有子包，包下面还可以建文件夹，如folder -> folder1-1,子包的概念
# 并不是说包下面只能包含包,和包平级的也可以是模块，如：4.py和folder1-1是平级，4.py是模块


# import导入模块
# 在某个模块中定义的变量或函数等,想在其它模块中引用,可用导入,所以通常我们将一些公用的东西,重复的东西放到同一个模块下,使代码具有复用性
# 导入模块有两种方法,方法一:import 包名.模块名(同一个包下的引用,包名可以省略)
# 引用的时候 命名空间.变量名,其中命名空间也可以使用别名,用as即可
# 同一个包下导入，在folder下4.py中定义变量a ,在7.py中引用
# import  4
# print(4.o)
# 遇到问题，代码一直提示错误identifier expected，原因：查看脚本命名是否是纯数字，纯数字的脚本导入会报错（我就是败在这一步）
# import suiji
# print(suiji.o) 这段代码还是报错，原因2019.1.3版本中即使是同一个包下面的模块导入也需要加上包名
print('分割线1----------------')
import folder.hello
print(folder.hello.o)
# 返回结果：(1, 2, 3)  (1, 2, 3)
#  思考：为什么o变量被打印两次，原因import导入的是hello这个模块，会将hello模块所有东西打印一遍
# 有时候会打印两遍，有时候又不会，不知道什么原因，好像是第一次导入是会将整个模块打印，第二次就不会了
# 原因:因为在同一个模块中,包不会重复导入
# 当命名空间过长时，可以使用别名
print('分割线2----------------')
import folder.hello as b
print(b.o)
# import只能导入模块，不能直接导入变量


# 导入方式2  from module import 变量或函数等
# 两者的区别：import导入的是一个模块，from ...import导入的时变量或函数
print('分割线3----------------')
from folder.hello import o
print(o)   # 这个地方就不用再写模块了，可直接引用
# 思考：from .. import的import后面是否仅仅只可以接变量和函数，能否接模块，答案是可以的
print('分割线4----------------')
from folder import hello
print(o)
print(hello.o)  # 这个地方加不加模块名都是可以的
# 思考：当被导入的模块中存在大量的变量，有无简便的方法
print('分割线5----------------')
from folder.hello import *
print(o)
print(h)   # 单独跑这一段代码程序会报错，百思不得其解
# 这个方法并不推荐，推荐方法，在导入模块的首行添加__all__ = [‘’，‘’]里面存放导入的变量名称或函数名称，
# 用这种方法添加的叫内置变量或内置属性
print('分割线6----------------')
from folder import hello
print(o)
print(u)
print(h)
# 在__all__ = [‘’，‘’]中定义的会被打印，若未定义则会报错

# __init__.py作用:当导入包时,python会自动首先执行这个文件
# 包和模块不会被重复导入的,且操作时避免循环导入
