import json
import requests
"""
遇到问题;
1.在写send_post和send_get函数时，入参是否需要注明data=None和header=None
解答：看视频中的代码是需要再次声明的，只对有可能为None的进行声明
但是最后实践证明，从以下代码证明是不需要重复声明为None的
2.在run_main函数中如何调用send_post和send_get函数
我是利用实例化类去调用这个函数的，看视频里利用self即可
这也就引入了一个新的问题
在一个类中实例方法调用另一个实例方法，利用self.方法名即可  此问题待验证
3.不要在多个函数中对res做json转化操作，在主函数中转化一次即可
"""


# 定义一个发送请求类
class SendRequest():
    # 定义一个发送post请求的方法
    def send_post(self, url, data, header):
        res = None
        # 判断传入的header值是否为空
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        # res = json.dumps(res, ensure_ascii=False, indent=2)
        return res

    # 定义一个发送get请求的方法
    def send_get(self, url, data, header):
        res = None
        # 判断传入的header值是否为空
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        # res = json.dumps(res, ensure_ascii=False, indent=2)
        return res

    # 定义一个运行函数
    def run_main(self, method, url, data=None, header=None):
        res =None
        if method == 'post':
            # res = SendRequest().send_post(url, data, header)
            res = self.send_post(url, data, header)
        else:
            # res = SendRequest().send_get(url, data, header)
            res = self.send_get(url, data, header)
        res = json.dumps(res, ensure_ascii=False, indent=2)
        return res


# 以下为验证代码
# if __name__ == '__main__':
#     url = 'http://127.0.0.1:8000/login/'
#     url1 = 'http://127.0.0.1:8000/loginout/?username=humingyue&password=56'
#     data = {
#         'username': 'hu',
#         'password': '123'
#     }
#     run = SendRequest()
#     print(run.run_main('post', url, data))
#     print(run.run_main('get', url1, data))

