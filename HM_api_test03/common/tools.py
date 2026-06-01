import uuid

from HM_api_test03.api.course import Course
from HM_api_test03.api.login import Login


def common_assert(res, status_code=200, code=200, msg="成功"):
    assert res.status_code == status_code
    assert res.json().get("code") == code
    assert msg in res.json().get("msg")


def get_token():
    login = Login()
    uuid = login.get_captchaImage().json().get("uuid")
    res = login.login(json_data={
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid": uuid
    })
    return res.json().get("token")
def get_id():
    course = Course()
    token=get_token()
    res=course.get_course_list(token,params={"name":"python基础"})
    rows = res.json().get("rows", [])
    return rows[0].get("id")



