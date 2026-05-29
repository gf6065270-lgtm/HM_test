
# 导入必要的库和模块
import requests
from config import BASE_URL  # 从配置文件中导入基础URL
from tools import login       # 从工具模块中导入登录函数以获取认证令牌
import random                 # 导入随机数模块，用于生成唯一的合同号

# 构建API请求的完整URL
url = BASE_URL + '/api/contract'

# 设置请求头，包含通过login()函数获取的Authorization令牌和内容类型
headers = {"Authorization": f"{login()}",
           "Content-Type": "application/json"
           }

# 构造POST请求所需的JSON数据 payload
json = {
    "name": "测试81",                          # 联系人姓名
    "phone": "13612341888",                    # 联系电话
    "contractNo": f"HT6868461{random.randint(1,999)}",  # 合同编号，后缀为1-999之间的随机数以确保唯一性
    "subject": "6",                            # 科目ID
    "courseId": 588862,                        # 课程ID
    "channel": "0",                            # 渠道标识
    "activityId": 77,                          # 活动ID
    "fileName": "客达天下API文档.pdf"          # 关联的文件名称
}

# 发送POST请求创建合同
res = requests.post(url=url, headers=headers, json=json)
# 打印响应状态码
print(res.status_code)
# 打印响应的JSON数据内容
print(res.json())
