__all__ = ['o', 'u', 'h']

name = input('please enter your name:')
print('hello,', name)
print('1024 * 768 =', 1024 * 768)

if 99 > 100:
    print(True)
else:
    print(False)
print(99 > 100)
print(255 == 0xfff)
print("I\'m mingyue, \nnice to meet you")
print('''hi
mingyou
world is wonderful''')
# print(r'\\\t\\\I\'m mingyue')
# 多行代码中包括单引号或双引号
print('''
hello alise
I'm mingyou
nice to meet you''')
print('Hello %s' % 'world')
print('Hell0 %s ,your score is %d' % ('Alise',100))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# int类型,包括正数和负数
print(type(1))
print(type(-1))
# Python的数字类型只有int和float,即使精度很高的时候也是float
print(type(1.1))
print(type(1.1111111))
# 当整数和浮点数进行混合运算时,结果为浮点数
print(type(1 + 1.0))
# python中的除法,/运算出来的是浮点数,要想得到整形,需要用到地板除或取余
print(type(9/3))
print(type(9//3))
print(bin(10))
print(int(0b10))
print(hex(10))
print(oct(0xfff))
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
print(bool(-1.123))
print(bool('abc'))
print(bool(''))
print(bool([1,2,3]))
print(bool([]))
print(bool({1,1,3}))
print(bool({}))
print(bool(None))
print(bool(0b10))
print(r'hello\\\t\\n, I\'m mingyue')

o = (1, 2, 3, 4)
print(o)
h = [1, 2, 3]
print(h)
u = [1, 2, 3, 4]
print(u)
