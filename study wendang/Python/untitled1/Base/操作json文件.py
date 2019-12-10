#conding:utf-8
import json

fp = open('..\interfaceCase\login.json', encoding='utf-8')
data = json.load(fp)
print(data['login'])