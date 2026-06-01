from HM_api_test03.api.course import Course
from HM_api_test03.api.login import Login
from HM_api_test03.common.tools import get_token, common_assert


class Test_course:#创建添加课程类
    course=Course()#创建课程实例
    def test_add_course01(self):
        token=get_token()#tools里方法获取token, tools模块通常存放通用的工具函数和辅助方法。
        res=self.course.add_course(token,json_data={#添加课程数据
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        })
        common_assert(res,status_code=200, code=200, msg="成功")

        """
self.course.add_course(token, json_data={...})
│    │      │          │       │
│    │      │          │       └─ 第二个参数：课程数据字典(course.py里方法名的另一个参数)
│    │      │          └──────── 第一个参数：认证token(course.py里方法名的参数)
│    │      └─────────────────── 方法名(course.py里方法名)
│    └────────────────────────── Course 实例(course.py里)
└────────────────────────────── 当前测试类实例(self优点,避免每个测试方法都创建新实例, Course 实例是无状态的（不保存数据），可以安全共享)
        """


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
from HM_api_test03.api.course import Course
from HM_api_test03.common.tools import get_token, common_assert


class Test_list:#查询测试列表接口
    course=Course()
    def test_list01(self):
        token=get_token()
        res=self.course.get_course_list(token,params={"name":"python基础"})
        # print(res.json())
        common_assert(res,status_code=200, code=200, msg="成功")
    def test_list02(self):
        token=get_token()
        res=self.course.get_course_list(token,params={"price":100})
        # print(res.json())
        common_assert(res,status_code=200, code=200, msg="成功")
    def test_list03(self):
        token=get_token()
        res=self.course.get_course_list(token,params={"price":100000000000000})
        # print(res.json())
        common_assert(res,status_code=200, code=500, msg="Failed")

"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""

from HM_api_test03.api.course import Course
from HM_api_test03.common.tools import get_token, get_id
class Test_info:#查询课程详情测试类
    course=Course()
    def test_info01(self):
        token = get_token()
        id=get_id()
        res=self.course.get_course_by_id(token,course_id=id)
        print(res.json())


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""

from HM_api_test03.api.course import Course
from HM_api_test03.common.tools import get_token, common_assert
class Test_update_course5:#修改课程测试类
    course=Course()
    def test_update_course05(self):
        token=get_token()
        res=self.course.update_course(token,json_data={
            "id": 588890,
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 89,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        })
        common_assert(res,status_code=200, code=200, msg="成功")

"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
class Test_delete_course6:#删除课程测试类
    course=Course()
    def test_delete_course06(self):
        token=get_token()
        res=self.course.delete_course(token,588890)
        common_assert(res,status_code=200, code=200, msg="成功")