"""
第1课
面向对象最核心的概念  1.类  2对象
类名的命名规则:与变量命名稍微有点不同,1.类名的第一个字母最好大写  2.两个组成的首字母大写
变量命名的建议最好是小写,两个单词时建议使用下划线连接
在类的内部我们可以做哪些事情 1.定义若干个变量   2.定义函数
"""


# 定义一个最基本的类,类的关键字class
class Student():
    name = ''
    age = 0

    def print_file(self):    # 此处代码不加self程序会报错
        pass


student = Student()  # 变量student接收实例化的结果
student.print_file()


# 思考:如何调用这个类
# 解决办法:给类实例化  student = Student()
# 思考:如何调用类下面的方法
# 解决办法:实例化对象.方法名 student.print_file()
class Student():
    age = 0
    name = '西'

    def student_information(self):
        print(self.name)
        print(str(self.age))


student = Student()
student.student_information()  # 注:此处一定要用实例化后的变量来调用方法



"""
第2课
总结:类的最基本概念就是封装一些变量和函数
在一个模块中可以定义很多个类,自己举例
类下面的函数叫方法,类下面的实例方法和实例变量一定要加self,否则程序会报错
不要在类的内部调用,类的调用一定要放在类的外部,类负责定义,描述,在做项目的时候推荐类的定义和
调用放在不同的模块
如何在另一个模块中调用类,先import后实例化成对象再调用方法
from 9c import Student
student = Student()
student.student_information()
函数 VS 方法  在模块中定义的函数叫函数,在类中定义的函数叫方法
方法和函数的区别:方法设计层面,函数:程序运行,过程式的一种称谓
变量定义在模块中叫变量,在类中定义叫数据成员

"""

"""
第3课
类和对象的关系
类和对象的关系通过实例化关联在一起的
类:行为和特征
学生类 name,age等
name和age就是特征  数据成员
行为 dohomework 方法
当类被实例化后变成一个具体的对象
"""


"""
第4课 构造函数

"""


# 思考:以下三个实例化对象是否相同
# 解答:从我们的角度或正常的角度来看,这三个对象是一样的,但从机器内部来看是不
# 相同的,可通过验证这三个对象的内存地址来区分
class Student():
    age = 0
    name = ''

    def do_homework(self):
        print('homework')


student1 = Student()
student2 = Student()
student3 = Student()
print(id(student1))
print(id(student2))
print(id(student3))


# 思考:怎样实例化几个从我们的角度来看不相同的对象,此处引入构造函数概念
class Student():
    name = ''
    age = 0

    def __init__(self, name, age):  # 这个函数的名字是固定的  构造函数
        print('我的名字是:'+name)
        print('我的年龄是:' + str(age))

    def do_homework(self):
        print('homework')


student1 = Student('小白', 12)
student2 = Student('小红', 45)
student3 = Student('小黄', 34)
print(id(student1))
print(id(student2))
print(id(student3))
# 注:构造函数的调用是自动执行的,所以不需要再次通过实例化对象.构造函数来调用


# 假如我们通过构造函数来调用,那么返回结果又是什么
class Student():

    def __init__(self):  # 这个函数的名字是固定的  构造函数
        print('我的名字是:')
        print('我的年龄是:')

    def do_homework(self):
        print('homework')


student1 = Student()
a = student1.__init__()
print(a)  # None
print(type(a))  # <class 'NoneType'>
# 返回结果的原因:和之前说的一样,没有return语句所以返回为None


# 思考:我们是否可以为构造函数返回一个值
class Student():

    def __init__(self):  # 这个函数的名字是固定的  构造函数
        print('我的名字是:')
        return 'result'

    def do_homework(self):
        print('homework')


student1 = Student()
a = student1.__init__()
print(a)
print(type(a))  # TypeError: __init__() should return None, not 'str'
# 结论:不能为构造函数指定非None的返回值,与普通函数的区别


class Student():
    name = ''
    age = 0

    def __init__(self, name, age):  # 这个函数的名字是固定的  构造函数
        # 在函数内部初始化对象的属性
        name = name  # 左边的name代表对象的属性,右边的name代表函数的入参
        age = age
        print('我的名字是:'+name)
        print('我的年龄是:' + str(age))

    def do_homework(self):
        print('homework')


student1 = Student('小白', 12)
print(student1.name)  # 这句打印出空字符串,将类变量打印出来了，思考为什么
print(Student.name)
# 说明我们在构造函数中的赋值并没有改变name变量的取值,原因:当局部变量与全局变量同名时,局部变量并不会覆盖全局变量
# 如果这样理解就错了,我们决不能将模块中的全局变量与局部变量之间的关系等同于类下面的变量
# 打印空值真正的原因:类变量和实例变量
"""
类变量和实例变量
类变量和类相关联在一起的
实例变量是和对象相关联在一起的
对象必须要有一个地方保存它的特征值的，如何保存不同对象的特征值，python中利用self
self.name = name
self.age = age   # 定义了两个实例变量，只和对象有关系，和类没有关系
"""


class Student():
    name = 'qiyue'  # 在这里定义的变量叫类变量
    age = 0

    def __init__(self, name, age):
        # 在函数内部初始化对象的属性
        self.name = name  # 在这里定义的变量叫实例变量
        self.age = age

    def do_homework(self):
        print('homework')


student1 = Student('小白', 12)  # 在对象中叫实例变量
student2 = Student('石敢当', 13)
print(student1.name)  # 小白
print(student2.name)  # 石敢当
print(Student.name)  # qiyue
# 思考：在类中定义的name和age变量有没有意义
# name和age属于对象的特有特征，定义在类中并不合适，面向对象的实际意义，在类中定义sum（表示一个班级学生总和）还是比较合适的


"""
1.
name = name 其实这行代码并没有将入参name赋给实例变量name
若想赋值给name必须加self  即 self.name = name 
可通过__dict__(显示当前对象或类下的所有相关变量)内置变量来验证
print（student1.__dict__）
print（Student.__dict__）
加self之后
print（student1.__dict__）

2.当我们尝试去访问实例变量，若没有，python自动去类变量中寻找。若在类中没有找到，它会去父类中寻找

思考两个问题
1.在构造函数中调用实例变量是否需要加self
解答：最好加self，加的时候访问的是实例变量，不加的时候代码不会报错，但是访问的其实是入参，一旦入参名称变化，
再去调用时代码报错
2.在实例方法中操作类变量，比如sum = sum + 1
解答：引入__class__内置属性：实例调用__class__属性时会去调用该对象对应的类，然后再去调用该类的其他属性，
毕竟调用类属性还是由类调用比较好
当不加__class__时其实调用的不是类属性，由以下代码可以看出
"""


class Student():
    sum = 0
    print("类中学生总人数为：" + str(sum))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sum += 1
        print("学生总人数为：" + str(self.sum))

    def do_homework(self):
        print("do english homework")


student1 = Student('石敢当', 18)
student1 = Student('石敢当', 18)
print("----------" + str(Student.sum))
student2 = Student('石敢当2', 18)
print("----------" + str(Student.sum))
"""
不加__class__返回结果为：类中学生总人数为：0
学生总人数为：1
----------0
学生总人数为：1
----------0

"""


class Student():
    sum = 0
    print("类中学生总人数为："+ str(sum))

    def __init__(self, name, age):
        self.name = name
        self.age =age

    def do_homework(self):
        self.sum += 1
        print("学生总人数为：" + str(self.sum))
        print("do english homework")


student1 = Student('石敢当', 18)
student1.do_homework()
print("----------" + str(Student.sum))
student2 = Student('石敢当2', 18)
student2.do_homework()
print("----------" + str(Student.sum))


# 在实例方法中操作类变量正确代码如下
class Student():
    sum = 0
    print("类中学生总人数为：" + str(sum))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print("学生总人数为：" + str(self.sum))

    def do_homework(self):
        print("do english homework")


student1 = Student('石敢当', 18)
print("----------" + str(Student.sum))
student2 = Student('石敢当2', 18)
print("----------" + str(Student.sum))


"""
类的方法
1.实例方法 ：定义时入参必须加self
2.类方法 ：1.增加装饰器@classmethod  2.定义时入参必须加cls
3.静态方法 ：1. 增加装饰器@staticmethod  2.定义时入参不用加关键字
"""


class Student():

    def __init__(self, name , age):
        self.name = name
        self.age = age

    @classmethod
    def plus_sum(cls):
        sum = 0

    @staticmethod
    def do_english_homework():
        print('do english homework')


"""
在实例方法中访问类变量
方法一、用类去访问 Student.sum
方法二、用对象去访问 self.__class__.sum
"""


class Student():
    sum = 0

    def __init__(self, name , age):
        self.name = name
        self.age = age
        print(Student.sum)  # 用类去访问
        print(self.__class__.sum)  # 用对象去访问


student1 = Student('是刚当', '18')


"""
类方法中操作类变量 cls.sum += 1
类外部调用类方法
方法一：通过类名.类方法  Student.plus_sum
方法二：通过对象去访问  student1.plus_sum
类外部调用类变量  通过类名.类变量  Student.sum
类方法与实例方法的区别：类与对象的区别
既然实例方法可以操作类变量，为何还需要类方法
虽然对象可以操作类方法，但是不建议这么做，逻辑不通，操作与对象无关的东西建议还是应该使用类方法
"""


class Student():
    sum = 0

    def __init__(self, name , age):
        self.name = name
        self.age = age

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('学生总数为：'+str(cls.sum))


student1 = Student('是刚当',10)
student1.plus_sum()  # 通过对象去访问类方法
Student.plus_sum()  # 类外部调用类方法
print(Student.sum)  # 类外部调用类变量



"""
静态方法的调用：
方式一：用类名.静态方法去调用 Student.do_english_homework()
方式二：通过对象去调用 student1.do_english_homework()
静态方法内部调用类变量 print(Student.sum)
静态方法与类方法是否可以访问实例变量  不可以
"""


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def do_english_homework():
        print('do english homework')


student1 = Student('是刚当',10)
student1.do_english_homework()
Student.do_english_homework()


"""
1.变量的访问也有类的内部与外部调用之分
2.有些对类或变量的操作不希望在类的外部随意更改，只允许内部更改，此处引入共有和私有

"""


class Student():

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


student1 = Student('是刚当', 10)
student1.score = -1  # 在外部直接对成员变量进行操作这是不安全的


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 初始化变量
        self.score = 0

    def marking(self, score):
        self.score = score
        print(self.name+'同学的分数为：'+str(self.score))


student1 = Student('是刚当', 10)
student1.marking(59)  # 一般不建议在类的外部直接对变量操作，而是通过方法去操作变量，
# 这样安全一点


"""
此处分析直接在类的外部操作变量与通过方法操作变量的区别
所有类方法下面的变量的更改都应该通过方法去操作，不建议直接去更改，方法好控制一点
比如score输入负数的时候，方法可以控制并给出提示
"""


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 初始化变量
        self.score = 0

    def marking(self, score):
        self.score = score
        if self.score < 0:
            return "不能给同学打负分"
        print(self.name+'同学的分数为：'+str(self.score))


student1 = Student('是刚当', 10)
result = student1.marking(-1)
print(result)


"""
上面代码虽然不建议直接在外部对成员变量进行操作，但依然可以进行操作，有没有什么方法阻止在外部操作成员变量
python表示私有的方法：通过方法名或变量名前面加双下划线，比如__marketing
思考构造函数是不是私有的，不是，因为python对于前有双下划线和后有双下划线的都不认为是私有的
"""


# 定义私有方法后去访问,代码报错
class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 初始化变量
        self.score = 0

    def __marking(self, score):
        self.score = score
        if self.score < 0:
            return  "不能给同学打负分"
        print(self.name+'同学的分数为：'+str(self.score))


student1 = Student('是刚当', 10)
result = student1.marking(-1)  # AttributeError: 'Student' object has no attribute 'marking'
print(result)


"""
我们之前说过私有变量既不能赋值也不能调用
看以下代码思考为什么外部调用私有方法时外部调用方法报错，而给变量加上__，外部动态操作私有变量没有报错
因为python是动态语言，student1.__score相当于给对象新加了一个名为__score的变量赋值
此处可通过新实例化一个对象来验证，也可以通过__dict__来验证
其实定义的私有变量python会自动将其变量名转换为_Student__score,如下面代码所示,
若想在外面访问私有变量用该名称访问即可,但不建议那样做
"""


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 初始化变量
        self.score = 0

    def marking(self, score):
        self.__score = score
        if self.score < 0:
            return "不能给同学打负分"
        print(self.name+'同学的分数为：'+str(self.score))


student1 = Student('是刚当', 10)
student2 = Student('shhd',19)
student1.__score = -1
print(student1.__score)
print(student1.__dict__)  # {'name': '是刚当', 'age': 10, 'score': 0, '__score': -1}
student1.marking(59)
student2.marking(60)
print(student1.__dict__)  # {'name': '是刚当', 'age': 10, 'score': 0, '__score': -1, '_Student__score': 59}
# print(student2.__score)
print(student2.__dict__)


"""
面向对象3大特性
1.继承  避免重复定义方法与变量
2.封装
3.多态
人和学生是继承关系,一般建议一个模块只写一个类
子类继承父类的两种方式
1.通过import  此种方法不建议
import folder.paarents9    注:此处一定要包名.模块名
class Student(folder.paarents9.Human):  注:此处的父类一定要包名.模块名.父类名
   print('============')
2.通过from import
from folder.paarents9 import Human
class Student(Human):   父类名即可
    print("==========")
    
python中还可以多继承,即一个子类可以有多个父类
"""

"""
变量的继承性:子类可以继承父类定义的变量,比如sum,父类中定义子类未定义,子类中也可访问该变量
构造函数的继承性:子类实例化对象未入参时代码报错,说明继承了父类的构造函数需入参
实例方法的继承性
"""
from folder.paarents9 import Human


class Student(Human):

    def do_homework(self):
        print("do homework")


# 继承变量与构造函数
# student1 = Student()  # 这段代码报错,报错信息未入参
student1 = Student('石敢当', 19)
print(student1.name)
print(student1.age)
print(student1.sum)
print(Student.sum)  # 继承了父类的sum
# 继承父类实例方法
student1.get_name()


"""
子类中也会有变量与构造函数,当子类有构造函数时,入参需要加上父类的入参,如以下代码所示
如何在子类中将name和age传给父类:
方式一:
Human.__init__(self, name, age)
分析这个地方为什么一定要传入self
解答:python中调用实例方法一般都是用对象去调用的,这个地方用类去调用虽然不符合逻辑
但python也不会强制去限制,所以这个地方需要加self
方式二: super
super(Student,self).__init__(name, age)

当子类与父类方法名同名时,这个在python中是允许的,并且python会优先调用子类的方法
想打印出父类同名的方法  利用super(Student, self).do_homework()
"""
from folder.paarents9 import Human


class Student(Human):

    def __init__(self, school, name, age):  # 需要加上父类的入参
        Human.__init__(self, name, age)  # 这个地方一定要加self
        self.school = school

    def do_homework(self):
        print("do homework")


student1 = Student('人民小学','石敢当', 18)
print(student1.name)
print(student1.age)

# 使用super关键字,并且子类方法名与父类方法名相同
from folder.paarents9 import Human


class Student(Human):

    def __init__(self, school, name, age):
        super(Student, self).__init__(name, age)
        self.school = school

    def do_homework(self):
        print("do homework")


student1 = Student('人民小学', '石敢当', 18)
student1.do_homework()  # do homework 打印出子类方法


# 打印出父类同名的方法
from folder.paarents9 import Human


class Student(Human):

    def __init__(self, school, name, age):
        super(Student,self).__init__(name, age)
        self.school = school

    def do_homework(self):
        super(Student, self).do_homework()
        print("do homework")


student1 = Student('人民小学', '石敢当', 18)
student1.do_homework()
""" 返回结果:do parent homework
do homework
"""