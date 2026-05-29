import requests
from config import BASE_URL
from tools import login

url = BASE_URL +'/api/common/upload'
heard = {"Authorization":f"{login()}"}
res = requests.post(url =url,headers=heard,files={'file': open('客达天下API文档.pdf', 'rb')})
print(res.status_code)
print(res.json())

# import requests
#
# from config import BASE_URL
# from tools import login
#
# url = BASE_URL+'/api/common/upload'
# header = {
#     "Authorization": f"{login()}"
# }
# # print(open("客达天下API文档.pdf","rb").read())
# res = requests.post(url=url, headers=header, files={"file": open("客达天下API文档.pdf","rb")})
# print(res.status_code)
# print(res.json())