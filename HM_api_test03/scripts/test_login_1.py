import requests  # 导入requests库，用于发送HTTP请求

from HM_api_test03.api.login import Login  # 从api.login模块导入Login类
from HM_api_test03.common.tools import common_assert  # 从common.tools模块导入通用断言函数
from HM_api_test03.scripts.config import BASE_URL  # 从scripts.config模块导入基础URL配置

class Test_login:  # 定义测试登录的类
    login_api = Login()  # 实例化Login类，创建登录API对象
    def test_login01(self):  
        res = self.login_api.get_captchaImage()  # 调用获取验证码图片接口
        uuid=res.json().get("uuid")  # 从响应JSON中提取uuid字段
        json_data={  # 构造登录请求的数据字典
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":uuid
        }
        res=self.login_api.login(json_data)  # 调用登录接口，传入构造好的数据
        print(res.json())  # 打印登录接口的响应JSON内容
        common_assert(res,status_code=200, code=200, msg="成功")  # 断言响应状态码为200，业务代码为200，消息为成功
    def test_login02(self ):  # 定义第二个测试用例：用户名为空时登录失败
        res = self.login_api.get_captchaImage()  # 调用获取验证码图片接口
        uuid=res.json().get("uuid")  # 从响应JSON中提取uuid字段
        json_data={
            "username":None,
            "password":"HM_2023_test",
            "code":"2",
            "uuid":uuid
        }
        res = self.login_api.login(json_data)  # 调用登录接口，传入构造好的数据
        # print(res.json())  # 注释掉的打印语句
        common_assert(res,status_code=200, code=500, msg="错误")  # 断言响应状态码为200，业务代码为500，消息为错误

    def test_login03(self):  # 定义第三个测试用例：用户名为空时登录失败（与test_login02逻辑相同）

        res = self.login_api.get_captchaImage()  # 调用获取验证码图片接口
        uuid = res.json().get("uuid")  # 从响应JSON中提取uuid字段
        json_data = {  # 构造登录请求的数据字典
            "username": None,  # 设置用户名为None
            "password": "HM_2023_test",  # 设置密码
            "code": "2",  # 设置验证码为2
            "uuid": uuid  # 设置之前获取的uuid
        }
        res=self.login_api.login(json_data)  # 调用登录接口，传入构造好的数据
        # print(res.json())  # 注释掉的打印语句
        common_assert(res, status_code=200, code=500, msg="错误")  # 断言响应状态码为200，业务代码为500，消息为错误

