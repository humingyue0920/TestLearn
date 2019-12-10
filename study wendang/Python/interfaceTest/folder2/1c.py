"""
第一课   接口自动化测试导学
1.接口的开发 利用django开发get和post接口
2.unit test与接口测试的结合
2.1 unit test的使用
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
前后端项目分离,前后端的桥梁,移动端和服务端的桥梁,前台的数据通过接口从服务端获取,或者向服务端提供数据
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
2.下载离线包，与python相同目录，进入该目录下，使用命令python setup.py install
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
    res = requests.post(url=url, data=data).json()
   return res.json()
    
    
send_post(url,data)
 ------------------------------------------------------------------------------------------------
 
 4.4   重构get请求和格式化相应数据
 (本小节主要知识点：如何封装发送get请求，与post请求唯一的区别就是将post换成get，连URL和data的参数都不变)
 (数据格式化：利用json.dumps(res),get接口会多几个参数，比如ident，设置tab空格符，sort_key设置排序，ensure_ascii设置acsii码)
现有如下请求：比如http://127.0.0.1:8000/login?cert=11,如何进行封装和格式化
import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {
    'username': 'imooc',
    'password': '123456'
}


def send_get(url, data):
    res = requests.get(url=url, data=data).json()
    return json.dumps(res,indent=2,sort_keys=True)


send_get(url, data)
print(send_get(url, data))
--------------------------------------------------------------------------------

4.5 使用类封装接口测试脚本
知识点:1.使用函数封装post和get方法,run_main()
2.在判断语句中总是return语句,语句优化,采用方法:定义res为none
3.get请求参数在url中写明,则data为空,如何解决
在定义函数的时候默认data=None,在调用的时候data就可以不传了
4.使用类封装函数,实例函数需要加self,调用时加self
5.增加构造函数
import requests
import json


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def send_get(self,url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def run_main(self,url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/?username=胡&password=gud'
    run = RunMain(url, 'GET')
    print(run)
    print(run.res)

    # data = {
    #     'username': 'imooc',
    #     'password': '123456'
    # }

"""