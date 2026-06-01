"""
模块说明：文件路径配置与测试
功能：定义API基础URL，构建PDF文档的文件路径，并验证文件读取功能
"""
import os

# API服务基础URL配置
BASE_URL = 'https://kdtx-test.itheima.net/'

# 获取当前脚本所在目录的绝对路径
path = os.path.dirname(os.path.abspath(__file__))

# 构建两种不同方式的PDF文档路径
file_name1 = path + "/HM_jiekou_base_02/hetong/scripts/客达天下API文档.pdf"
file_name2 = path + "/客达天下API文档.pdf"

# 以二进制模式读取PDF文件内容并输出，用于验证文件路径是否正确
print(open(file_name2, "rb").read())