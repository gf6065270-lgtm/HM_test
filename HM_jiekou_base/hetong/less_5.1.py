#查询课程表
import requests
from config import BASE_URL
from tools import login

# 设置课程ID
course_id = "588862"
# 构建请求URL：/api/clues/course/588862
url = BASE_URL + f'/api/clues/course/{course_id}'

# 获取登录token并设置请求头
heard = {"Authorization":login()}
# 发送GET请求，携带查询参数id
res = requests.get(url =url,headers=heard)
# 打印响应结果的JSON数据
print(res.json())
