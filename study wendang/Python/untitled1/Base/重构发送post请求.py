import json
import requests


class SendRequests():
    def __init__(self, method, url, data=None):
        self.method = method
        if method == 'post':
            self.send_post(url, data)
        else:
            self.send_get(url, data)

    def send_post(self, url, data=None):
        res = requests.post(url=url,data=data).json()
        res = json.dumps(res,ensure_ascii=False, indent=2)
        print(res)

    def send_get(self, url, data=None):
        res = requests.get(url=url, data=data).json()
        res = json.dumps(res, ensure_ascii=False, indent=2)
        print(res)


data = {
    'username': 'hu',
    'password': '123'
}
requests1 = SendRequests('post', 'http://127.0.0.1:8000/login/', data)
