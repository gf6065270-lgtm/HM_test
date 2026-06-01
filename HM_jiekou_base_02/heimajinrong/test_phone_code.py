import time
from logging import NullHandler

import requests
from HM_jiekou_base_02.heimajinrong.config import URL
class Test_phone_code:
    def setup_method(self):
        self.senn = requests.session()
        res = self.senn.get(URL+"/common/public/verifycode1/12154")

    def test_1(self):
        res=self.senn.post(URL+"/member/public/sendSms",
                           data={
                               "phone":"13488661001",
                               "imgVerifyCode":"8888",
                               "type":"reg"
                           }
                           )
        assert res.status_code == 200
        assert "短信发送成功" in res.json()["description"]


    def test_2(self):
        res=self.senn.post(URL+"/member/public/sendSms",
                           data={
                               "phone":"",
                               "imgVerifyCode":"8888",
                               "type":"reg"
                           } )
        print(res.json())
        assert res.status_code == 200
        assert  res.json()["status"]==100
        assert "号码" in res.json()["description"]

    def test_3(self):
        res=self.senn.post(URL+"/member/public/sendSms",
                           data={
                               "phone":"13488661001",
                               "imgVerifyCode":"",
                               "type":"reg"
                           } )
        print(res.json())
        assert res.status_code == 200
        assert  res.json()["status"]==100
        assert "错误" in res.json()["description"]
    def test_4(self):
        res=self.senn.post(URL+"/member/public/sendSms",
                           data={
                               "phone":"13488661001",
                               "imgVerifyCode":"8899",
                               "type":"reg"
                           } )
        print(res.json())
        assert res.status_code == 200
        assert  res.json()["status"]==100
        assert "错误" in res.json()["description"]
    def test_5(self):
        res = self.senn.post(URL + "/member/public/sendSms",
                             data={
                                 "phone": "13488661001",
                                 "imgVerifyCode": "8888",
                                 "type": "reg"
                             })
        print(res.json())
        time.sleep(601)
        assert res.status_code == 200
        assert res.json()["status"] == 100
        assert "过期" in res.json()["description"]
    def test_6(self):
            res = self.senn.post(URL + "/member/public/sendSms",
                                 data={
                                     "phone": "13488661001",
                                     "imgVerifyCode": "8888",
                                     "type": None
                                 })
            print(res.json())
            assert res.status_code == 200
            assert res.json()["status"] == 100
            # assert "空" in res.json()["description"]
    def test_7(self):
        res = self.senn.post(URL + "/member/public/sendSms",
                             data={
                                 "phone": "13488661001",
                                 "imgVerifyCode": "8888",
                                 "type": "abc"
                             })
        print(res.json())
        assert res.status_code == 200
        assert res.json()["status"] is None
        assert None in res.json()["description"]