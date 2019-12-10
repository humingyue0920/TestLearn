import re
"""
第一课
正则表达式
此处引入index()内置函数：判断是否包含括号内的字符串,大于-1时代表包含
或者可以使用in
或者使用findall（）函数  用法：findall（‘正则表达式’，string, count = 0,模式）  注：匹配常量意义不大
使用findall（）函数的前提是导入re模块，用re去调用该函数
用findall（）返回结果为什么是一个序列
"""

a = ('c', 'c++', 'java', 'c#', 'python')
print('python' in a)
print(a.index('python') > -1)
# print(a.index('pytho') > -1) 此段代码报错 x not in tuple
# a = 'c|python'
b = re.findall('python', a)    # TypeError: expected string or bytes-like object
# 当a是一个元组的时候代码报错，说明findall（）函数只能去匹配一个字符串
print(b)

# 正确代码如下
a = 'c|python'
b = re.findall('python', a)
print(b)  # ['python']
# 思考：返回结果为什么是一个序列
# 解答：这个字符串匹配设定的值可能不止一个
if len(b) > 0:
    print('字符串中包含Python')
else:
    print('不包含')

"""
第二课：元字符与普通字符
题目：a = jdsj9nd777783bdsjja576 将a中所有的数字匹配打印出来
方法一：利用for in循环
方法二：利用元字符\d 匹配0-9
普通字符：'python'
元字符：\d
"""
# 利用for in循环
a = 'jdsj9nd777783bdsjja576'
for x in a:
    if x in '0123456789':
        print(x, end="|")

# 利用元字符\d
a = 'jdsj9nd777783bdsjja576'
b = re.findall(' \d ', a)
print(b)

# 匹配非数字
a = 'jdsj9nd777783bdsjja576'
b = re.findall('\D', a)
print(b)

"""
第三课 字符集
"""
s = 'abc, ffj, fjk,jd,fjd'
# 要求找出中间一个是b或者f的单词，前后分别是a和c
# 使用中括号【】，将我们需要抽象的字符写在中括号里
a = re.findall('ffj', s)
print(a)
b = re.findall('a[bf]c', s)  # 找出中间一个是b或者f的单词，前后分别是a和c
# 左右的a和c是定界
print(b)
# 字符集 中括号里的字符是或的关系
# 非 【^】 取反
# 如果我们要匹配的字符很多的时候，我们可以利用字符顺序来表示或的关系，比如【c-f】


"""
第四课 概况字符集
"""

# 概况字符集 比如\d(表示阿拉伯数字0-9)相当于【0-9】 \D相当于【^0-9】
# \w 只匹配数字和字母和下划线，相当于【A-Za-z0-9_】
# \W 非字母和数字和下划线，包括空格，回车\n,\t
# \s 匹配空白字符，包括空格，制表符\t，回车\n,\r
# \S 匹配非空白字符
# .匹配除换行符\n其他所有字符
# 思考：为什么python将所有的匹配结果拆成了一个一个字母
# 解答：因为不管是字符集也好还是概况字符集也好，都只能匹配一个单一的字母或者字符

"""
第五课 数量词
用{}表示，可以是一个数字，表示匹配这个字符，也可以是两个数字，用逗号隔开，表示最小m个字符，最大n个字符
"""
ss = '1277python73java9php9javascript'
a = re.findall('[a-z]{3}', ss)
print(a)   # ['pyt', 'hon', 'jav', 'php', 'jav', 'asc', 'rip']
b = re.findall('[a-z]{3,6}', ss)
print(b)   # ['python', 'java', 'php', 'javasc', 'ript']

"""
第六课  贪婪与非贪婪
python中默认是贪婪的，如果想非贪婪就要加？
"""
ss = '1277python73java9php9javascript'
b = re.findall('[a-z]{3,6}?', ss)
print(b)   # ['pyt', 'hon', 'jav', 'php', 'jav', 'asc', 'rip']

"""
第七课 匹配0次1次或者无限多次
* 表示匹配*前面的字符0次或者无限多次（包括1次）
+ 表示匹配+前面的字符1次或者无数次
？ 表示匹配？前面的字符0次或者1次
"""
ss = 'pytho1python0pythonn2'
b = re.findall('python*', ss)
print(b)  # ['pytho', 'python', 'pythonn']
c = re.findall('python+', ss)
print(c)  # ['python', 'pythonn']
d = re.findall('python?', ss)
print(d)  # ['pytho', 'python', 'python']
e = re.findall('python{1,2}', ss)
print(e)  # ['python', 'pythonn']
f = re.findall('python{1,2}?', ss)
print(f)  # ['python', 'python']
# 注：注意使用？的返回结果
# 匹配字符？与非贪婪字符的区别：？前面是数量词的时候当非贪婪字符


"""
第八课 边界匹配符
"""
# 现在的场景是qq号是4位到8位，满足该条件则是QQ号否则不是
qq1 = '10000001'
qq2 = '1902349274843'
r1 = re.findall('\d{4,8}',qq1)
print(r1)
r2 = re.findall('\d{4,8}',qq2)
print(r2)
if len(r1) > 0:
    print('qq1是QQ号')
else:
    print('qq1不是QQ号')
if len(r2) > 0:
    print('qq2是QQ号')
else:
    print('qq2不是QQ号')  # qq2是QQ号
# 从返回结果看，这个匹配并不能满足该种情况，引入边界匹配符 ^ $
# ^表示从字符的开头进行匹配，$表示从字符的末尾进行匹配，加入边界匹配符后表示完全匹配

qq2 = '1902349274843'
r2 = re.findall('^\d{4,8}$',qq2)
print(r2)  # []
if len(r2) > 0:
    print('qq2是QQ号')
else:
    print('qq2不是QQ号')  # qq2不是QQ号


"""
第十课 组
此处引入问题，判断a里面是否存在3个Python，引入组的概念
（Python）与【】的区别，（）表示且的关系，【】表示或的关系
"""
a = 'pythonpythonpythonpythonpython'
r = re.findall('(python){3}', a)
print(r)   # ['python']
b =  'pythonpythonpy'
r1 = re.findall('(python){3}', b)
print(r1)  # []
c = 'pythonpythonpythonpythonpython'
r2 = re.findall('(python){3}(js)', c)
print(r2)   # []


"""
第十一课 匹配模式
findall('正则表达式'，常量名，匹配模式)
匹配模式可以是一个，也可以是多个，多个时用|隔开，表示的是且的关系
re.I 表示忽略大小写
re.S表示匹配所有字符，包括换行符\n
"""
a = 'pythonc#\njava'
r1 = re.findall('C#', a, re.I)
r2 = re.findall('C#.{1}', a, re.I | re.S)
print(r1)  # ['c#']
print(r2)   # ['c#\n']


"""
第十二课 re模块的替换函数
re.sub('正则表达式'，‘替换字符’，搜索的原字符串，匹配成功后被替换的最大数量，匹配模式)
匹配成功后被替换的最大数量默认是0，代表全部匹配
此处引入Python的内置函数replace(self,old,new,count)
sub()函数的第二个参数还可以传入函数，定义的函数中value参数表示匹配成功后传入的字符，此处是c#
这个函数中的value并不是一个字符串，而是一个对象，通过print()语句打印出来，返回结果如下
<re.Match object; span=(6, 8), match='c#'>
<re.Match object; span=(12, 14), match='c#'>
<re.Match object; span=(17, 19), match='c#'>
这个地方的（6,8）代表被匹配中的字符前面还有6个字符，真正是从7,8开始，12,14同理，此处不再解释
我们可以利用group（）函数将元组转换为字符串:match = value.group()
如果想要替换将match去除即可
"""
a = 'pythonc#javac#phpc#javascript'
r1 = re.sub('c#', 'GO', a)
print(r1)   # pythonGOjavaGOphpGOjavascript
r2 = re.sub('c#', 'GO', a, 1)
print(r2)  # pythonGOjavac#phpc#javascript
r3 = re.sub('C#', 'GO', a)
print(r3)   # pythonc#javac#phpc#javascript
r4 = re.sub('C#', 'GO', a, re.I)
print(r4)   #pythonc#javac#phpc#javascript
r5 = re.sub('C#', 'GO', a, 0,  re.I)
print(r5)   # pythonGOjavaGOphpGOjavascript
# 对于结果4的返回不是很清楚，难道是匹配模式用错了？明明忽略大小写了啊，后期有时间研究
# 原因：使用匹配模式的时候第四个参数必须要传，否则导致匹配模式不起作用

a = 'pythonc#javac#phpc#javascript'
a.replace('c#', 'GO')
print(a)  # pythonc#javac#phpc#javascript
# 思考：为什么这个地方打印出来的c#没有被替换
# 原因：因为字符串是不可变类型
# 正确写法如下
language = 'pythonc#javac#phpc#javascript'
language = language.replace('c#', 'GO')
print(language)   # pythonGOjavaGOphpGOjavascript


def convert(value):
    pass


a = 'pythonc#javac#phpc#javascript'
language = re.sub('c#', convert, a)
print(language)  # pythonjavaphpjavascript
# 所有的c#被替换成空字符串，因为在convert函数中我们使用pass
# 假如我们想将c#转换成其他字符


def convert(value):
    print(value)
    #return "!!" + value+ "!!"  # 将替换字符前后加！！


a = 'pythonc#javac#phpc#javascript'
language = re.sub('c#', convert, a)
print(language)   # TypeError: can only concatenate str (not "re.Match") to str
# 代码报错，报错原因：value是一个对象


#正确代码如下
def convert(value):
    match = value.group()
    return "!!" + match + "!!"  # 将替换字符前后加！！


a = 'pythonc#javac#phpc#javascript'
language = re.sub('c#', convert, a)
print(language)   # python!!c#!!java!!c#!!php!!c#!!javascript


"""
第十三课  把函数作为参数传递

"""
# 给定一个题目，将s常量中的数字替换，若数字小于6则替换成0，若数字大于6则替换成9
s = 'ABC3721D86'


def convert(value2):
    match = value2.group()
    if int(match) < 6:
        return '0'
    else:
        return '9'


r  = re.sub('[0-9]', convert , s)
print(r)


# 给定另一个题目，凡是单个字符全部去除，凡是两个字符大于50的替换成100，小于50的替换成0
s = 'A5B8C3721D86'


def convert(value):
    match = value.group()
    if 10 <= int(match) < 50:
        return '0'

    elif int(match) >= 50:
        return '100'
    else:
        pass


r = re.sub('[0-9]{1,2}', convert, s)
print(r)


"""
第十四课 re模块的另外两个函数
re.match  从字符串的首字母开始匹配
re.search 搜索整个字符串
都只匹配一次，匹配到后立即停止
"""


"""
第十五课 group分组
group获取分组的匹配
group()函数中是可以传参数的，参数意义代表传入的组号，默认是0
"""
# 给定题目：提取出life和Python之间的所有字符
s = 'life is short, i use python'
r = re.search('life.*python', s)
print(r)
print(r.group())   # life is short, i use python
r1 = re.search('life(.*)python', s)    # 注：此处用的是小括号
print(r1)
print(r1.group(1))  #  is short, i use
# 一般我们不建议用search或者match，因为比较麻烦，用findall省事很多
r2 = re.findall('life(.*)python', s)
print(r2)   # [' is short, i use ']

# 给定题目，提取的字符中存在多个分组
s = 'life is short, i use python, i love python'
r = re.search('life(.*)python(.*)python', s)
print(r.group(0))  # life is short, i use python, i love python
print(r.group(1))  # is short, i use
print(r.group(2))  # , i love
# 可以简化成以下代码
print(r.group(0, 1, 2))  # ('life is short, i use python, i love python', ' is short, i use ', ', i love ')
# 此外还有groups（）函数，仅仅显示出被匹配的字符
print(r.groups())  # (' is short, i use ', ', i love ')


"""
第十六课 json
json是一种轻量级的数据交换格式
字符串是json的表现形式
"""

"""
第十七课 反序列化
导入json模块 import json
json是跨语言的 它在每种语言都能找到对应的数据结构
json字符串 json字符串在Python中的写法
str_json = '{"name":"qiyue","age":18}' 注：大括号里面的内容一定要双引号，json规定，
大括号外面的一定要用单引号，Python中规定，数字类型和布尔类型不需要加引号
json模块提供一种方法：json.loads()把json字符串转换成Python对应的数据结构
json类型有对象和数组，对象在Python中对应dict类型，数组对应Python的list类型
布尔值在json格式中用小写的false表示，你会发现转换成Python类型后会自动转换成大写的False
总之一句话：json有自己的数据类型，json.loads()函数就是将json转换成Python自己的数据类型
反序列化：将json字符串转换成Python数据类型
"""


import json
str_json = '{"name":"qiyue","age":18}'
student = json.loads(str_json)
print(student)  # {'name': 'qiyue', 'age': 18}
# 思考：这个地方返回回来的数据为什么是单引号
# 解答：已经利用了json.reloads()函数将他转换为Python的字典类型了，至于dict用单引号还是双引号取决于Python
print(type(student))   # <class 'dict'>
print(student['name'])
print(student['age'])

# 当json字符串是数组时
str_json1 = '[{"name":"qiyue","age":18, "flag":false},{"name":"bayue","age":19}]'
student1 = json.loads(str_json1)
print(student1)  # [{'name': 'qiyue', 'age': 18, 'flag': False}, {'name': 'bayue', 'age': 19}]
print(type(student1))   # <class 'list'>
print(student1[0]['name'])
print(student1[1]['name'])

"""
第十八课 序列化
序列化：就是利用json.dumps()函数将Python数据类型转换为json
"""
student = [
    {'name': 'qiyue', 'age': 18, 'flag': False},
    {'name': 'bayue', 'age': 19}
]
str_json = json.dumps(student)
print(str_json)
print(type(str_json))  # <class 'str'>
