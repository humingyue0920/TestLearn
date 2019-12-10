import json
import requests


# 定义一个发送请求类
class SendRequest():
    # 定义一个发送post请求的方法
    def send_post(self, url, data, header):
        res = None
        # 判断传入的header值是否为空
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
            print(res.status_code)
        return res.json()

    # 定义一个发送get请求的方法
    def send_get(self, url, data, header):
        res = None
        # 判断传入的header值是否为空
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    # 定义一个运行函数
    def run_main(self, method, url, data=None, header=None):
        res =None
        if method == 'post':
            res = self.send_post(url, data, header)
        else:
            res = self.send_get(url, data, header)
        res = json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
        return res


# 以下为验证代码
if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/'
    url1 = 'http://127.0.0.1:8000/loginout/?username=humingyue&password=56'
    data = {
        'username': 'hu',
        'password': '123'
    }
    run = SendRequest()
    print(run.run_main('post', url, data))
    print(run.run_main('get', url1, data))