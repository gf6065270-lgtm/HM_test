
import requests

from config import BASE_URL

def login():
    requests.get(url=BASE_URL+'/api/captchaImage').json ().get('uuid')
    res  =requests.post(url=BASE_URL+'/api/login',json={
        'username':'admin',
        'password':'HM_2023_test',
        'code':'2',
        'uuid':requests.get(url=BASE_URL+'/api/captchaImage').json ().get('uuid')
    })
    token = res.json().get('token')
    return token

if __name__ == '__main__':
    print(login())

def cahxun():
    pass