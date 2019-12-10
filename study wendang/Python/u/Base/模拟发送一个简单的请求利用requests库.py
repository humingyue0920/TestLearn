import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {
    'username':'hu',
    'password':'123'
}
# result = requests.post(url=url, data=data)
res = requests.post(url=url, data=data).json()
res = json.dumps(res, ensure_ascii=False, indent=2)

print(type(res))
print(res)
