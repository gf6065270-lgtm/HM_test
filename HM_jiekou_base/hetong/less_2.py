import uuid

import requests
# 定义登录接口URL
url="http://kdtx-test.itheima.net/api/login"
# 准备登录请求数据
json ={
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":uuid
}
# 发送POST请求进行登录
res=requests.post(url,json=json)
# 输出响应状态码和响应数据
print(res.status_code)
print(res.json())