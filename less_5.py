#导包 URL token requests
import requests
from config import BASE_URL
from tools import login
#调用查询课程列表接口
url = BASE_URL+ '/api/clues/course/list'
heard = {"Authorization":login()}
res=requests.get(url =url,headers=heard,params={"name":"python基础"})
print(res.json())