import requests
from HM_api_test03.scripts.config import BASE_URL
#把获取验证码接口封装成函数
# def get_captchaImage():
#     return requests.get(BASE_URL+'/api/captchaImage')
# #把登录接口封装成函数
# def login(jeson_data):
#     return requests.post(BASE_URL+'/api/login',json=jeson_data)

class Login:
    def get_captchaImage(self):
        return requests.get(BASE_URL + '/api/captchaImage')

    # 把登录接口封装成函数
    def login(self,json_data):
        return requests.post(BASE_URL + '/api/login', json=json_data)

"""
get_captchaImage()：发送 GET 请求获取验证码图片及 UUID
login(json_data)：发送 POST 请求执行登录，参数为包含用户名、密码、验证码的字典
"""