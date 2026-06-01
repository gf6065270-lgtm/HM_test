import pytest
import requests

from HM_jiekou_base_02.hetong.scripts.config import BASE_URL


@pytest.fixture(scope="class")
def login():
    res = requests.get(BASE_URL + "/api/captchaImage")
    uuid = res.json()["uuid"]
    res = requests.post(BASE_URL + "/api/login",
    json={
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": uuid
    })
    return res.json()["token"]

