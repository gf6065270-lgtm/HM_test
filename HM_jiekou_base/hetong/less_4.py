class Test_add_coutrace():
    import requests

    from config import BASE_URL
    res = requests.get("http://kdtx-test.itheima.net/api/captchaImage")
    uuid = res.json().get("uuid")
    url = f"{BASE_URL}/api/login"
    json = {
        "username": "admin",
        "password": "HM_2023_test",
        "code": "2",
        "uuid": uuid
    }
    token = res.json()["token"]
    res = requests.post(url, json=json)

    url = f"{BASE_URL}/api/clues/course"
    header = {"Authorization": token}
    json = {
        "name": "测试开发提升课01",
        "subject": "6",
        "price": 899,
        "applicablePerson": "2",
        "info": "测试开发提升课01"
    }
    res = requests.post(url=url, headers=header, json=json)
    print(res.json())

