import requests

from HM_jiekou_base_02.heimajinrong.config import URL


class Test_verifty:
    def test_1(self):
        res= requests.get(URL +"/common/public/verifycode1/0.1254")
        assert res.status_code == 200
        assert res.text is not None
    def test_2(self):
        res= requests.get(URL +"/common/public/verifycode1/1254")
        assert res.status_code == 200
        assert res.text is not None
    def test_3(self):
        res= requests.get(URL +"/common/public/verifycode1/")
        assert res.status_code == 404
        assert res.text is not None
    def test_4(self):
        res= requests.get(URL +"/common/public/verifycode1/abc")
        assert res.status_code == 400
        assert res.text is not None
