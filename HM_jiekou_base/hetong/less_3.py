import requests
# 定义全局变量
URL="http://kdtx-test.itheima.net"
res=requests.get("http://kdtx-test.itheima.net/api/captchaImage")
# 获取uuid
uuid=res.json().get("uuid")
# 登录
url=f"{ URL}/api/login"
# 构建json数据
json ={
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":uuid
}
# 发送POST请求
res=requests.post(url,json=json)
print(res.status_code)
print(res.json())