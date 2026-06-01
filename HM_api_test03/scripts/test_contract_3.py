import os
import random

from pydantic_settings.sources.providers import json

from HM_api_test03.api.contract import Contract
from HM_api_test03.api.course import Course
from HM_api_test03.api.login import Login
from HM_api_test03.common.tools import get_token, common_assert


class Test_upload_contract:
    contract=Contract()
    couese=Course()
    login=Login()
    def test_upload_contract01(self):
        token = get_token()
        # 2. 定义文件路径
        file_path = "./HM_api_test03/客达天下API文档.pdf"
        # 3. 构造 files 参数并发送请求
        with open(file_path, 'rb') as f:
            # files = {'file': f}
            res = self.contract.contract(token, files=f)
        # print(res.json())
        common_assert(res,status_code=200, code=200, msg="成功")

"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
class Test_add_contract:
    contract=Contract()
    couese=Course()
    login=Login()
    def test_add_contract01(self):
        token = get_token()
        json_data={
            "name": "测试88",
            "phone": "13612341888",
            # "contractNo": f"HT1001200{random.randint(100,999)}",
            "contractNo": f"HT10012004",
            "subject": "6",
            "courseId": 588725,
            "channel": "0",
            "activityId": 77,
            "fileName": "./HM_api_test03/客达天下API文档.pdf"
        }
        res=self.contract.contract_add(token,json=json_data)
        print(res.json())
        common_assert(res,status_code=200, code=200, msg="操作成功")
    def test_add_contract02(self):
        pass

"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
class Test_info_contract:#查询合同列表
    contract=Contract()
    couese=Course()
    login=Login()
    def test_contract_info01(self):
        token = get_token()
        params={"phone": "13612341889"}
        res=self.contract.contract_info(token,params=params)
        print(res.json())
    def test_contract_info02(self):
        pass
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
class Test_delete_contract:
    contract=Contract()
    couese=Course()
    login=Login()

    def test_delete_contract01(self):
        token = get_token()
        data={
            "id":23510836085568046
        }
        res = self.contract.contract_delete(token, data)
        print(res.text)


