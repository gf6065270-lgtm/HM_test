import requests
res=requests.get("http://kdtx-test.itheima.net/api/captchaImage")
print(res.status_code)
print(res.json())