"""
第七章 从接口自动化框架设计到开发
7.1 导言
unittest与HTMLTestRunner结合使用的是一种小型的测试框架，并不适用与成千上万条测试用例
接口测试需要的点
1.接口地址  2.请求数据  3.接口类型  4.预期结果  5.header（登陆状态）  6.数据依赖


7.2 python使用excel导入测试用例（如何操作excel）
有一个类或者方法方法去操作这个excel
1.安装两个安装包 xlrd  2.
data = xlrd.open_workbook()  # 获取excel文件的存放地址
tables = data.sheet()[0]  # 获取第一个表格对象
table_name = data.sheet_names()  # 获取Excel的名称
table_rows = tables.nrows  # 获取第一个表格对象的行数
tables_cell_value = tables.cell_value(m,n)


7.3 重构封装Excel方法
具体代码见excel_reconfig即可


7.4 学习操作json文件
1.请求数据是字典,请求数据字典里嵌套字典
2.请求数据字典数据较多,在Excel表格中看起来比较乱
如何去把这些请求数据处理一下呢,这里只是提供一个新的方法,并不一定好用,如果有更好的方法并不一定建议使用此方法
excel表格中请求数据用login代替,在文件目录下创造login.json文件
login.json文件中数据可以
{
"login":{"username":"木吃吃","password":"123456"},
"loginout":{"username":"木吃吃","password":"123456"},
"addcut":{"username":"木吃吃","password":"123456"}
}
若请求数据在json文件中,我们该如何操作这个json文件
1.新建opration_json.py
利用open函数打开json文件所在目录
利用json.load()将json文件中的数据转换为字典格式
获取字典中的某一个键值
遇到问题:未对打开的文件做字符说明,代码一直报UnicodeDecodeError: 'gbk' codec can't decode byte 0x83 in position 32: illegal multibyte sequence错误
加上encoding='utf-8'即解决
Python3之json文件操作:https://www.cnblogs.com/xiehong/p/9050301.html


7.5 封装操作json文件
在使用open命令时,我们还需要将文件关闭close
Python提供命令 with open() as fp即用完后会自动关闭


7.6 封装获取常量方法
Excel表中有很多表头,获取Excel表中的常量
方法是:定义一个类
在类中定义若干个变量,变量的值分别从0开始,相当于下标,顺序按照Excel表中Excel表头顺序
在类的外部定义若干个方法,每个方法获取一个变量


7.7 封装获取接口数据
封装获取caseExcel中数据的整体思路
1.导入重构封装Excel
2.重构封装获取Excel的表头
3.也许会操作Excel中引入的外部json文件,导入操作json文件

定义类
构造函数,对导入重构封装Excel的对象进行实例化
定义各个函数获取Excel表格中具体的数据,并对一些数据进行判断
注：在使用类名调用实例方法时，虽然没有定义构造函数，但调用时类名后面一定要加小括号，否则代码报错


7.8 post和get的基类封装
与原来封装的不同不过是加了一个入参header
遇到问题;
1.在写send_post和send_get函数时，入参是否需要注明data=None和header=None
解答：看视频中的代码是需要再次声明的，只对有可能为None的进行声明
但是最后实践证明，从以下代码证明是不需要重复声明为None的
2.在run_main函数中如何调用send_post和send_get函数
我是利用实例化类去调用这个函数的，看视频里利用self即可
这也就引入了一个新的问题
在一个类中实例方法调用另一个实例方法，利用self.方法名即可  此问题待验证


7.9 主流程封装及错误解决调试
遇到的问题：
1.为什么程序只运行了一行
解答：因为在for循环语句中加了return语句，return语句后面的代码将不被执行，循环也不被执行
解决办法：将return语句放在与循环语句同等位置即可
2.思考get方法该如何入参 Excel
当不修改get请求方法的url时，代码一直报json格式错误
解决办法：Excel中get请求的url以http://127.0.0.1:8000/loginout/?username=humingyue&password=156这种格式填写


7.10 返回数据格式处理及调试
本章节最主要的内容就是对post_get基类封装的格式进行调整
我自己本身以前在写的时候已经进行过数据处理，但是代码具有一些冗余性
此次新建对post_get基类封装改良版.py进行改良，以前的代码也需要看
改良版主要改动的几个地方
1.调用时都采用self
2.对返回结果格式化只在run_main函数中体现
3. return时return res.json 不再在每次返回结果后面加.json()函数


7.11 获取接口返回状态
在发送post或get请求的函数中添加res.status_code即可
前提是接口的出参中有该字段


7.12 通过预期结果判断case是否执行成功
1.新建文件 结果对比封装.py
2.定义类
3.在类中定义对比函数
4.在封装程序入口.py文件中导入结果对比封装.py包  并在构造函数中实例化
5.在封装程序入口.py获取Excel表中的预期结果
6.利用实例化对象调用对比函数 写出判断函数 打印出测试成功或测试失败



7.13  将返回结果写入Excel文件中
操作步骤：
1.在重构Excel.py 脚本中新增写入函数
2.在封装获取caseExcel中的数据.py文件中新增方法 将实际结果写入Excel文件中
3.在封装程序入口.py文件中调用封装获取caseExcel中的write_result方法即可
注意的点
1.在操作Excel文件时，该文件不要打开，会报权限错误
2.Excel文件被写入后，扩展名会默认变成xls，修改扩展名文件才可打开，或者在一开始建文件时就将扩展名修改



7.14  数据依赖设计思路
Excel表中字段解释
case依赖：依赖case名称，这里我们可以用caseID来代表唯一性
依赖的返回字段：即上一个接口的返回字段（出参字段）的名称
数据依赖字段：即下一个接口的入参字段名称
当上一个接口的出参只有一个返回结果时好解决
若返回结果是一个数组，每一个里面都包含一条返回结果时 data：【0】：name 下标从0开始


7.15 数据依赖问题方法封装之通过caseID获取case数据
1.在重构封装Excel中添加以下代码
2.新建文件，解决依赖问题，定义类和方法
引入知识点：获取整行的内容 self.data.row_values()  获取整列的内容：self.data.col_values()

# 根据对应的caseID找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data


    这个函数我有点不是很明白，这个地方为什么要搞一个col_data
    是否可以直接将这个省去
    后明白，不能将此省去，原因省去后无法将num自加，for col_data in cols_data代表遍历循环这列的每一个数据

    # 根据caseID获取行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1
        return num

    # 根据行号获取该行的内容
    def get_row_value(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一整列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


7.16
"""