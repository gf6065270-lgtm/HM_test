
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


def common_assert(res, status_code=200, code=200, msg='成功'):
    """
    通用的接口响应断言函数

    用于验证API响应的状态码、业务代码和消息内容是否符合预期。

    Args:
        res: requests库的Response对象，包含API响应数据
        status_code (int): HTTP状态码，默认为200
        code (int): 业务状态码，默认为200
        msg (str): 期望包含在响应消息中的文本，默认为'成功'

    Returns:
        None: 如果所有断言通过则无返回值，否则抛出AssertionError

    Raises:
        AssertionError: 当任一断言条件不满足时抛出异常
    """
    assert res.status_code == status_code
    assert res.json()["code"] == code
    assert msg in res.json()["msg"]
