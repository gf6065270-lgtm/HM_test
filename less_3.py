import requests
URL="http://kdtx-test.itheima.net"
res=requests.get("http://kdtx-test.itheima.net/api/captchaImage")
uuid=res.json().get("uuid")
url=f"{ URL}/api/login"
json ={
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":uuid
}
res=requests.post(url,json=json)
print(res.status_code)
print(res.json())