"""
第一课   接口自动化测试导学
1.接口的开发 利用django开发get和post接口
2.unittest与接口测试的结合
2.1 unittest的使用
2.2 HtmlTestRuner 报告的生成
2.3 断言
2.4 Case的管理
2.5 Request的引入使用
3.接口自动化测试框架从设计到开发
3.1 设计框架
3.2 工具类封装
3.3 基类封装
3.4 调试错误
3.5 数据处理
3.6 回写测试结果
3.7 解决数据依赖
3.8 结果统计
3.9 邮件服务
3.10 发送报告

"""
"""
第二课 
什么是接口
前后端项目分离,前后端的桥梁,移动端和服务端的桥梁,前台的数据从通过接口从服务端获取,或者向服务端提供数据
接口基础面试题
1.如何理解接口测试
2.接口测试与功能测试的区别
3.接口类型 post get put delete
4.post与get的区别  传参方式不同 get向服务器获取数据,post向服务器提供数据,post的安全性更高

"""

"""
一 如何使用fillder抓包
1.知道自己电脑的ip地址 
cmd中使用命令ipconfig
2.手机与电脑的网络在同一网段
3.filder工具中tools options connects 设置监听端口
4.手机WiFi设置手动http代理,输入IP地址和监听端口

若HTTPS请求抓取不到,输入IP地址:监听端口号 安装证书即可

二 大量重复数据数据模拟以及过滤数据
在fiddler中若想大量模拟数据重复,选中该条请求用replay即可
过滤规则在右边的filters中设置即可并将use filters勾选即可


三、如何模拟接口返回数据 mock
"""

"""
如何去开发一个接口
利用Django开发接口
安装Django命令：Python setup.py install 离线安装
pip install django==2.3 在线安装

开发一个post接口
遇到问题：总是login/login 的调用，不知道问题出在哪里
开发一个get接口
将入参的方式改变，并将post改为get即可
在尝试将中文入参，发现返回回来的接口是乱码，解决办法：https://blog.csdn.net/zer021/article/details/79219943
"""

"""
第三章 如何开发get
---------------------------------------------------------------------------
3.1 开发接口环境的搭建
有两种方法:
1.在pycharm中直接创建Django项目,会自动下载一些相关文件
2. 离线安装  下载Django压缩包,解压到与Python安装目录的同一个目录下
运行命名 python setup.py install
------------------------------------------------------------------------------

3.2 django接口工作原理
1.manage.py文件运行 加上参数runserver 默认地址127.0.0.1:8000
若是在命令行中可以进入该项目的manage.py文件夹所在目录下,运行Python manage.py runserver 127.0.0.1:8000
两种方式都可
2.创建Django项目工程
    有两种方式:
    1.利用命令行创建:python manage.py startapp appname
    2.在pycharm中创建:创建Django项目时,打开倒三角符号,在application name中输入即可
3.在setting.py文件中INSTALLED_APPS加上创建的项目名称
4.在url.py文件中增加跳转路由 该模块导入跳转函数路径
5.在views中编写函数

主要的代码有:
from django.http.response import HttpResponse

# Create your views here.

def Login(request):
    return HttpResponse('this is first text')
-----------------------------------------------------------------------------


3.3 Django之post接口开发
开发一个简单的登录页面:
1.创建登录页面
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>denglu</title>

</head>
<body>
<form action="/login/" method='POST'>
    <h1>用户名：<input name="username"></h1>
    <h1>密码：<input name="password"></h1>
    <input type="submit" value="登录">
</form>

</body>
</html>
2.创建登录函数
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # password = request.POST.get('password')
        return HttpResponse(username)
    else:
        return render_to_response('login.html')

其中:HttpResponse对象
概述：
作用：给浏览器返回数据
HttpRequest对象是由Django创建的，HttpResponse对象是由程序员创建
用法：
不用模板，直接返回数据
语句示例：return HttpResponse("Sunck is a good man")
render_to_response():就是加载指定的页面



------------------------------------------------------------------------------------
3.4 Django之get接口开发
将views.py文件中的post改成get即可,仅仅只需要修改views.py文件,login.html不需要修改
在访问页面以?入参的方式来访问即可,发现将userName返回回来了
若入参加上password,并将password返回回来会怎么样
def Login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        return HttpResponse(username, password)
    else:
        return render_to_response('login.html')
会发现返回乱码,如何解决
http://127.0.0.1:8000/login/?username=%E7%A7%AF%E5%88%86%E5%85%91%E6%8D%A2&password=%E5%A5%BD%E7%9A%84
加起来可以正常返回
return HttpResponse(username+password)
我们希望返回的是一个json,下节课介绍


---------------------------------------------------------------------------------
3.5 Django之接口数据处理
将数据的返回结果格式改为json格式-get接口
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json


def Login(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        password = request.GET.get('password')
        data = request.GET.get('data')
        result['user'] = username
        result['password'] = password
        result['data'] = data
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')


将数据的返回结果格式改为json格式--post接口
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json


def Login(request):
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['user'] = username
        result['password'] = password
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')

"""

"""
第四章
--------------------------------------------------------------------------------------
4.1 requests库的相关使用（本节最主要内容讲了如何安装requests库）
requests即测试的相关地址库
requests库的安装：两种方法
1. pip install requests
2.下载离线包，与python相同目录，进入该目录下，使用命令python manage.py install
可通过 python
import requests
命令查看是否安装成功
-----------------------------------------------------------------------------------------------

4.2 requests的简单使用-post
(本小节主要是讲了如何利用requests库发送一个简单的post请求)
import requests
import json

data = {
    'username':'imooc',
    'password': '123456'
}
res = requests.post(url='http://127.0.0.1:8000/login/', data=data)
print(res.text)
print(type(res.json))  # dict
-------------------------------------------------------------------------------------------

4.3 重构发送post请求
（本小节主要讲了如何封装post请求）
以上代码看起来很lower，不具有复用性，可对以上代码进行封装，使该功能具有复用性
import requests
import json
data = {
    'username':'imooc',
    'password': '123456'
}
url='http://127.0.0.1:8000/login/'


def send_post(url,data):
    res = requests.post(url=url, data=data)
   return res.json()


send_post(url,data)
 ------------------------------------------------------------------------------------------------

 4.4   重构get请求和格式化相应数据
 (本小节主要知识点：如何封装发送get请求，与post请求唯一的区别就是将post换成get，连URL和data的参数都不变)
 (数据格式化：利用json.dumps(res),get接口会多几个参数，比如ident，设置tab空格符，sort_key设置排序，ensure_ascii设置acsii码)
现有如下请求：比如http://127.0.0.1:8000/login?cert=11,如何进行封装和格式化
import requests
import json
url='http://127.0.0.1:8000/login/'
data = {
    'username':'imooc',
    'password': '123456'
}
def send_get(url,data):
    res = requests.get(url=url, data=data).json()
   return json.dumps(res，ident = 2，sort_key = True)


print send_get(url,data)
"""

"""
第五章  unittest的使用

5.1 unittest的使用
python的测试框架：unittest
Java的测试框架：testNG
主要知识点：
1.定义一个类继承unittest.TestCase方法
2.定义一个在测试方法之前执行的函数与之后的执行函数，函数名称固定 setUp tearDown
3.定义的测试方法名必须以test开头，否则不执行
4.注：如果类中有两个测试方法，那么setUp tearDown则会被执行多次
5.对于setUp我们不想每次在测试方法前都执行一次，比如想登陆一次即可，此处引入类方法，名称固定 setUpClass  tearDownClass
6.调用unittest的main方法
--------------------------------------------------------------------------------------

5.2 unittest和requests封装重构
json.dumps() 将字典类型转换为字符串类型
json.dump()将字典类型转换为字符串类型，并写入json文件中
json.loads()将字符串类型转换为字典类型
json.load()用于从json文件中读取文件
本节主要代码见requests_demo_copy和unittest_demo2_copy
注意setUp里的代码
注：
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
------------------------------------------------------------------------------------------

5.3 unittest中assert的使用
先是可以利用if else的判断，后太麻烦，引入assertEqual函数
assertEqual（first,second,third）若第一个参数和第二个参数不相等则返回第三个参数
assertNotEqual() 判断两个参数是否不相等
具体代码见unittest_assert

---------------------------------------------------------------------------------------------

5.4 unittest中case的管理及运用
Python中如何将一个接口的返回结果作为下一个接口的入参
1.在一个接口中将出参赋值,并将该出参返回
2.在setUp函数中接收,self.userid = self.test_01()
3.在另一个接口中打印该参数

这种方法并不好用,引入新的知识点,全局变量
1.在出参的接口设置全局变量 globals()['userid'] = '100090'
2.在入参接口直接打印
实际运用设置全局变量见unittest_case.py 设置类全局变量,将返回结果由json变为字典,获取某一个返回字段,
赋值给全局变量,在另一个用例中调用

在unittest中执行case的顺序是按照数字的顺序来排序执行的
在unittest中我们想跳过某一个用例可采用
@unittest.skip(test_02)

除了使用main()方法执行测试用例还可以使用另一种
1.创建一个容器(放case的集合)
创建一个名称为suite的容器:suite =unittest.TestSuite()
2.往容器里面添加case
suite.addCase(TestDemo('test_01')) TestDemo是类名
3.有多个case时添加多个即可
suite.addCase(TestDemo('test_02')) 
4.运行容器
unittest.TestTestRunner().run(suite) 把容器放进去即可

main()方法执行与容器执行的区别
思考题:不同的case放在了不同的py文件中,该用哪一种方法去执行case呢

------------------------------------------------------------------------------------------

5.5 unittest与HTMLTestRunner生成报告
1.下载安装HTMLTestRunner
2.新建HTMLTestRunner.py  赋值粘贴
3.将该文件赋值到Python安装目录下的lib文件夹下即可
4.利用python  import HTMLTestRunner检查是否安装成功
注:目前对这个HTMLTestRunner.py文件非常讲究,官网的代码是按照Python2语法去写的,不适用Python3
修改后的Python3 HTMLTestRunner文件存在百度云盘,并且study wendang也存了一份

过程中遇到的问题
1.运行后html报告文件并没有生成
解决办法:使用unittest框架去运行，是永远都无法导出测试报告，原因是：
PyCharm会默认使用自带的unittest框架来执行单元测试，不会执行main函数中的代码，所以不生成测试报告
具体可参考如下文章：
https://blog.csdn.net/autotest00/article/details/80747123

2.通过该语句:pathfile = "../report/reportHtml.html"并不能自动生成report文件夹
解决办法:手动创建report文件夹

优化:将测试用例与报告分隔开
https://blog.csdn.net/chenmozhe22/article/details/82888060
按照上面说的方法去操作总是报错;
最后导致的原因是:Windows文件命名规则不允许有冒号,而脚本中的时间格式定义有冒号
最后将格式修改即可:now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
具体代码见manage.py unittest_html_seprate.py
-----------------------------------------------------------------------------------------------------------

5.6 unittest之面试
1.如何利用Python开发测试框架
1.利用requests包去封装函数,模拟发生post,get请求
requests与request的区别
requests.get() requests.post()模拟发送请求,赋值后代表返回回来的整个json结果
request.GET.get()  request.POST.get() 获取接口的入参字段
2.利用unittest框架去管理case
case按照命名规则升序执行,可以跳过,可以指定执行,还可以添加assert断言 case的依赖
3.利用HTMLtestRunner去生成测试报告
4.数据的存储与管理:可以利用Excel或者mysql
5.与Jenkins集合持续集成
2.如何管理case
利用unittest框架去管理case
case按照命名规则升序执行,可以跳过,可以指定执行,还可以添加assert断言 case的依赖
case写在Excel中
3.简述case的执行
case的执行是按照case命名的升序规则去执行的,unittest框架去管理
4.如何解决case的依赖
可以将一个接口的出参结果定义为全局变量,或者可以将该变量写在配置文件中或存储到数据库中,需要时调用
5.如何生成HTML报告
官网下载HTMLtestRunner.py文件,将该文件复制到Python安装目录的lib文件夹下,在模块中导入
最后在模块中指定生成报告的目录,并给该目录赋予读写权限,利用HTMLTestRunner.HTMLTestRunner()函数去生成测试报告


与jmeter相比,jmeter是如何去做接口自动化测试的
1.jmeter如何做接口自动化测试
利用jmeter编写测试脚本,新建线程组,添加http请求,模拟发生post,get请求
可以利用CSV set config数据分离,用Excel与管理测试用例,也可以完全编写http请求
利用jmeter内置函数vars.get()获取接口返回接口,对出参进行断言,也可以之间添加response assert添加响应结果断言
利用jmeter内置函数vars.put()设置全局变量解决接口之间的依赖,或者利用正则表达式提取器,json extract
2.下载插件HTML 
利用ant jmeter Jenkins生成HTML测试报告


"""

"""
第六章 mock服务入门到实战
6.1 mock
mock是模拟接口的返回数据
mock的安装
pip install mock
检查mock是否安装成功 python import mock

6.2 mock的重构封装
"""
