#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
import requests
from HM_jiekou_base.hetong.scripts.config import BASE_URL
from HM_jiekou_base.hetong.scripts.tools import common_assert


class Test_add_coutrce():
    token = None
    # def test_add_uuid(self):
    #     res = requests.get(BASE_URL + "/api/captchaImage")
    #     uuid = res.json()["uuid"]
    #     res = requests.post(BASE_URL + "/api/login",
    # json={
    #         "username": "admin",
    #         "password": "HM_2023_test",
    #         "code": "2",
    #         "uuid": uuid
    #     })

        # Test_add_coutrce.token = res.json()["token"]
        # assert res.status_code == 200
        # assert res.json()["code"] == 200
        # assert "成功" in res.json()["msg"]
        # common_assert(res)

    # 调用新增课程接口
    def test_add_course(self,login):
        res = requests.post(BASE_URL + '/api/clues/course',
                            headers={'Authorization': login},
                            json={
                                "name": "测试开发提升课01",
                                "subject": "6",
                                "price": 899,
                                "applicablePerson": "2",
                                "info": "测试开发提升课01"
                            }
                            )
        print(res.json())
        # assert res.status_code == 200
        # assert res.json()["code"] == 200
        # assert "操作成功" in res.json()["msg"]
        common_assert(res)


