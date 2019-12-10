import json
import requests


class SendRequests():
    def run_main(self, method, url, data=None):
        res = None
        if method == 'post':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        return res

    def send_post(self, url, data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,ensure_ascii=False, indent=2)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, ensure_ascii=False, indent=2)
