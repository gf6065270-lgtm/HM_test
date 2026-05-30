#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
#接口测试基础学完
import random

import requests
from HM_jiekou_base.hetong.scripts.config import BASE_URL
from HM_jiekou_base.hetong.scripts.tools import common_assert


class Test_add_coutrce():
    token = None

    def test_add_uuid(self):
        res = requests.get(BASE_URL + "/api/captchaImage")
        uuid = res.json()["uuid"]
        res = requests.post(BASE_URL + "/api/login",
    json={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        })
        assert res.status_code == 200
        assert res.json()["code"] == 200
        assert "成功" in res.json()["msg"]

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
        # assert "成功" in res.json()["msg"]
        common_assert(res)

    # 调用课程列表查询接口
    def test_add_coutrce_list(self, login):
        res=requests.get(BASE_URL + '/api/clues/course/list',
                            headers={'Authorization': login},
                            params={"name": "python基础"}
                            )
        common_assert( res)
        print(res.json())

    # 调用上传课程接口
    def test_add_coutrce_upload(self, login):
        res =requests.post(BASE_URL+'/api/common/upload',
                           headers={'Authorization': login},
                           files={'file': open('./HM_jiekou_base/hetong/scripts/客达天下API文档.pdf', 'rb')}

        )
        print(res.json())
        common_assert(res)
        #新增合同接口
    def  test_add_coutrce_add(self, login):
        res = requests.post(BASE_URL + '/api/contract',
                            headers={'Authorization': login},
                            json={
                                "name": "测试81",  # 联系人姓名
                                "phone": "13612341888",  # 联系电话
                                "C": f"HT6868461{random.randint(1, 999)}",  # 合同编号，后缀为1-999之间的随机数以确保唯一性
                                "subject": "6",  # 科目ID
                                "courseId":588861 ,  # 课程ID
                                "channel": "0",  # 渠道标识
                                "activityId": 77,  # 活动ID
                                "fileName": "客达天下API文档.pdf"  # 关联的文件名称
                            }

                            )
        print(res.json())
        common_assert(res)





