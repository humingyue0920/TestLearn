# 组,列表list
# 同一种类型的列表
print([1, 2, 3, 34])
print(type([1, 2, 3]))
# 组合类型列表
print([True, False, 1, 2, "Hello World", 0xfff])
print(type([True, False, 1, 2, "Hello World", 0xfff]))
# 嵌套列表
print([[1, 2, True], [False, "hello"], ["world"]])
print(type([[1, 2, True], [False, "hello"], ["world"]]))
# 列表的基本操作,访问列表
# 注:如果用单一的数字,索引的方式来访问列表,则得到的结果是字符串,如果用冒号
# 去访问则得到的还是一个list
print([True, False, 1, 2, "Hello World", 0xfff][0])
print([True, False, 1, 2, "Hello World", 0xfff][4])
print(type([True, False, 1, 2, "Hello World", 0xfff][4]))
print([True, False, 1, 2, "Hello World", 0xfff][4:])
print([True, False, 1, 2, "Hello World", 0xfff][-1:])
print(type([True, False, 1, 2, "Hello World", 0xfff][-1:]))  # <class 'list'>
# 访问嵌套列表,不管是单一的索引还是冒号,得到的结果类型都是list
print([[1, 2, True], [False, "hello"], ["world"]][0])
print(type([[1, 2, True], [False, "hello"], ["world"]][0]))
print([[1, 2, True], [False, "hello"], ["world"]][0:2])
print(type([[1, 2, True], [False, "hello"], ["world"]][0:2]))
# 列表的加法运算
print([True, False, 1, 2, "Hello World", 0xfff]+['明月'])
# 列表的减法
# 列表不存在减法,程序会报错
# 列表的乘法,同字符串,不能列表与列表相乘
# 表示32个队伍的分组情况
print([1, 2, 3, 4], [2, 2, 3, 4], [3, 2, 3, 4], [4, 2, 3, 4], [5, 2, 3, 4], [6, 2, 3, 4], [7, 2, 3, 4], [8, 2, 3, 4])
# 元组() tuple
print((1, 2, 3))
print(type((1, 2, 3)))
# 奇怪的现象,当元组里只有一个元素时,类型会发生变化
# 思考:为什么会发生变化
# 原因是小括号在Python中不仅仅可以表示元组还可以表示数学运算,
# 所以在Python中规定,默认当做数学运算来处理
# 那如何解释元组中只有一个字符串,str类型呢
print(type((1)))
print(type(('hello')))
# 思考:Python中如何表示只有一个元素是元组呢,用逗号隔开即可
print((1,))
print(type((1,)))
# Python中的空元组,()即可
print(())
print(type(()))
print((1, 2, 3)+(4,))

"""
思考:list与tuple如此相像,两者的区别是什么
list是可变类型,tuple是不可变类型
list可以使用append()函数向末尾增加元素,tuple不可
list可以对元素重新复制,tuple可以获取元素但不可赋值变成另外的元素,tuple类型里的list可以重新复制
"""


# str,list,tuple叫序列
# 序列的共有操作:1.切片[m:n]  2.+,*
# 切片很有意思的用法,切片中含有三个数字,意义和用法自行研究
# 当碰到print(str[0:8:2])
# 得到的却是 ‘hlow’，此时数字0代表的是h ,，数字8代表的是r ，数字2代表的是步长。
# 也就是说输出从h开始每两个字符输出一个字符，所以第二个输出就是l，第三个为o，
# 第四个为w。所以结果就是**‘hlow’**
print('Hello World'[0:8:2])
print('Hello World'[0:9:2])
# 若我想判断一个元素是否在一个序列中,此处引入in和not in
print(3 in [1, 2, 4, 3])
print(10 in [1, 2, 4, 3])
print('h' in('hello world'))
print('H' in('hello world'))
print(3 not in [1, 2, 4, 3])
# 如果想知道一个序列的长度,此处引入len()方法
print(len([1, 2, 3, 4, 5, 6]))
print(len('Hello World'))  # 注:空格也计入长度
print(len(('hello', 'world')))   # 返回结果为2
# 获取序列中最大的元素,此处引入max()函数
print(max(1, 2, 3, 4, 5))
print(max('Hello World'))  # r
print(max(('Hello', 'world')))  # world
# 获取序列中最小的元素,此处引入min()函数
print(min(1, 2, 3, 4, 5))
print(min('Hello World'))  # 返回的是空格
print(min('HelloWorld'))  # 返回H
print(min(('Hello', 'world')))  # 返回Hello
# 当进行字符串字母比较时,计算机会对字符串字母所对应的的ASCII码进行比较,此处引入ord()函数,获取字母的ASCII码
# 在使用ord函数时犯了一个错误,导致程序报错,ord函数中的字母忘记加引号,导致不是字符串,且获取空格的ASCII码时,单引号之间一定要有一个空格
print(ord('r'))
print(ord('H'))
print(ord(' '))

# 集合 set类型 用{}表示
# 集合与序列两个最大的区别 1.无序  2.不重复
print({1, 2, 3, 4, 5, 6})
print(type({1, 2, 3, 4, 5, 6}))
print({1, True, False, "Hello"})  # 此处返回结果{False, 1, 'Hello'}
# 原因:True和1都代表1,集合具有不重复的特点,所以...也证明集合是可以混合类型的
# 证明无序,无法用下标和切片的方式访问集合,程序会报错
# print({1,2,3}[0])
# print({1,2,3}[0:1])
# 证明不重复,会自动去掉集合中重复的元素
print({1, 1, 2, 3, 3})   # 返回结果{1, 2, 3}
# 集合也可以使用len()函数获取集合的长度,其中重复元素不重复计算长度
print(len({1, 1, 2, 3, 3}))
print(len({1, True, False, "Hello"}))
# 判断一个集合是否包含某一个元素 in和not in
print(3 in {1,2,3})
print(3 not in {1,2,3})
# 集合特有的一些操作  1.取两个集合的差集 "-"
# 2.取两个集合的交集 "&" 3.去两个集合的并集 "|"
print({1, 2, 3, 4, 5, 6}-{3, 4})
print({1, 2, 3, 4, 5, 6} & {3, 4})
print({1, 2, 3, 4, 5, 6} | {3, 4, 7})
# 如何定义一个空的集合,下面的方法返回的类型为dict,并不是空集合
print({ })
print(type({ }))
# 正确定义空集合的方法,需要用到set关键字,set()
print(set())
print(type(set()))
print(len(set()))
# 字典:一个字典可以由多个key和value组成 {key1:value1,key2:value2,.....}
print({1: 2, 2: 3, 3: 4})
print(type({1: 2, 2: 3, 3: 4}))
print({'Q': '技能1', 'W': '技能2', 'P': '技能3', 'L': '技能4'})
# 获取字典里的value:通过key来访问,因为不是序列,所以不能用下标来访问
print({'Q': ' 技能1', 'W': '技能2', 'P': '技能3', 'L': '技能4'}['Q'])  # 返回'技能1'
# 字典中的key具有唯一性,不能有重复的key
print({'Q': '技能1', 'Q': '技能2', 'P': '技能3', 'L': '技能4'})  # 返回结果{'Q': '技能2', 'P': '技能3', 'L': '技能4'},只会返回一个Q
# 字典中的key必须是不可变类型,可以是str,int,tuple类型,而value可以是str,number,set,list,tuple,dict
print({'Q': '技能1', 'Q': 1, 'P': True, 'L': {1: 2}, 'U': (3, 4)})
# 思考:字符串1和数字1是否相同,事实证明是不相同的
print({'1': '技能1', 1: '技能2', 'P': '技能3', 'L': '技能4'}['1'])  # 返回结果:技能1
print({'1':'技能1',1:'技能2','P':'技能3','L':'技能4'}[1])   # 返回结果:技能2
# 列表类型的key是不可以的,代码会报错,但是元组类型的却可以
# 思考这是为什么 除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key。
# print({[1,2]:'技能1',1:'技能2','P':'技能3','L':'技能4'})
print({(1,2):'技能1',1:'技能2','P':'技能3','L':'技能4'})
# 空字典
print({ })
print(type({}))


