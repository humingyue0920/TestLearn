# 变量
# 来看一个变量的例子,注意Python非常注意缩进,此处曾多一个空格导致代码报错
a = 1
print(id(a))  # 140726049989264
b = a
print(id(b))   # 140726049989264
a = 3
print(id(a))  # 140726049989328
print(b)  # 1
# 对比看以下结果:b被改变
a = [1, 2, 3, 4, 5]
print(id(a))
b = a
a[0] = '1'
a.append(6)
print(id(a))
print(b)  # 此处打印的结果是['1',2,3,4,5, 6]
# 思考:为什么会是这样
# 原因:因为int是值类型,list是引用类型
# 值类型,a重新赋值后指向新的值,而list类型重新赋值后还是指向原来的被改变过的值
# 其中值类型包括:int str tuple(不可改变),引用类型包括list,set,dict(可改变)
# 有些非保留关键字虽然也可以作为变量名,不会报错,但是在你用到这个名字的时候会被当成变量来处理导致报错
# 比如type和print
type = 1
# print(type(1))  #系统报错:TypeError: 'int' object is not callable

# 既然说字符串是不可改变的,为什么a没有报错,此处不是改变,而是定义了一个新的字符串
# 可以通过id()函数来证明,获取变量的内存地址
a = 'Hello'
print(id(a))
a = a +'python'
print(a)
print(id(a))
# 同理验证不可变类型tuple
a = (1, 2, 3)
print(id(a))
a = (1, 2, 3) + (4,)
print(id(a))

# 此处会报错,因为str是不可改变类型
a = 'Hello'
# a[0] = 'o'
# print(a)
# tuple和list去区别 1.list是可变类型,tuple是不可变类型
a = [1, 2, 3]
a[0] = '1'  # 这是可行的
a = (1, 2, 3)
# a[0] = '1' #这会导致代码报错,因为这是不可变类型
# 此处引入新的知识点.append 向列表末尾添加一个元素,可以给列表追加元素,但是不能给元组追加元素
a = [1, 2, 3]
print(id(a))
a.append(4)
print(id(a))
print(a)
# 此处出现警告是因为前面代码中有append

d = [1, 2, 3, 4]
d.append(5)
print(d)
# 元组不可改变类型的优势,多个人共同写代码,有些是不可以让人改变的

# 如何访问到4
a = (1, 2, 3, [1, 2, 4])
print(a[3][2])
# 如何访问到b
a = (1, 2, 3, [1, 2, ['a', 'b', 'c']])
print(a[3][2][1])
# 思考下面的元组为什么可以被修改
# 猜测:修改的是元组中的列表,列表是可改变类型
# 猜测得到验证,将列表改为元组后,代码报错
a = (1, 2, 3, [1, 2, 4])
a[3][2] = '4'
print(a)
a = (1, 2, 3, (1, 2, 4))
# a[3][2] = '4'

# 关系运算符,不仅仅可以进行数字的比较,且字符串,列表,元组等等都可以进行比较
print(1 == 1)
print([1, 2, 3] < [2, 3, 4])
print((1, 2, 3) > (2, 3, 4))
print({1, 2, 3} >= {1, 2, 3})
# print({1,2,3} >= (1,2,3)) #不同类型比较报错
# 注:关系运算符中==与!=可以进行不同类型进行比较,但是>,>=,<,<=必须比较同类型
# print('1'>1)    #报错信息:TypeError: '>' not supported between instances of 'str' and 'int'
b = 1
b += 1 >= 1
print(b)  # 2

b = 1
b += 1 > 1
print(b)  # 1

b = 1
b += 1 < 1
print(b)  # 1

b = 1
b += 1 <= 1
print(b)  # 2
# 验证关系运算符比较的时候,字符串比较,是按照和来比较还是按照一个一个字母去比较
# 事实证明并不是按照字符串ASCII码的和来比较,而是按照一个一个字母的ASCII码比较
print('abc' > 'bca')
print('abc' < 'bca')
# 成员运算符 in not in
# 可以是str,list,tuple,set,dict,在字典类型判断的key
a = 'h'
print(a in 'hello')
a = 1
print(a in [1, 2, 3])
print(a in(1, 2, 3))
print(a in {1, 2, 3})
print(a in {1: 2, 2: 3})   #True
print(a in {2: 1, 2: 3})  #False
print(a in {'c': 2})
# 身份运算符 is和not is
# 此处需要引入对象的概念,后期详细介绍
# 最终的返回结果也是bool
# is和==的区别,关系运算符==比较的是两个变量的值,is比较的是两个变量的内存地址
# ==相当于java中的equal()和==

# is比较的是两个变量的内存地址
a = 1
b = 1.0
print(a == b)  # True
print(a is b)  # False
print(id(a))
print(id(b))
# 思考题:以下 a==b ,a is b ,c ==d, c is d
a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)   # True  猜测set是无序的
print(a is b)   # False,要完全相等才会是True
print(id(a))
print(id(b))
c = (1, 2, 3)
d = (2, 1, 3)
print(c == d)   # False  猜测tuple是有序的
print(c is d)   # False 要完全相等才会是True
print(id(c))
print(id(d))
# 判断类型,推荐方法,引入函数isinstance()
# 用法:isinstance(变量,变量类型),且第二个参数可以接受元组,元组中传入多个类型
a = 1
print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a, set))
print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, (str, int, list)))
