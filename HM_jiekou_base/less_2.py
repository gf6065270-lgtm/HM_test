import uuid

import requests

url="http://kdtx-test.itheima.net/api/login"
json ={
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":uuid
}
res=requests.post(url,json=json)
print(res.status_code)
print(res.json())