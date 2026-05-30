#模块级别 , 运行于每个模块（即py文件）的始末，
# 即：每个测试模块只会执行一次
def setup_module():  # 定义模块级别的setup函数，在模块中所有测试用例执行前运行一次
    print("模块级的setup方法")  # 打印提示信息，表明模块级setup已执行

def teardown_module():  # 定义模块级别的teardown函数，在模块中所有测试用例执行后运行一次
    print("模块级的teardown方法")  # 打印提示信息，表明模块级teardown已执行

class TestDemo:  # 定义测试类TestDemo，用于组织相关的测试用例

    def test_demo1(self):  # 定义第一个测试方法test_demo1
        print("test_demo1输出")  # 打印test_demo1的执行输出信息

    def test_demo2(self):  # 定义第二个测试方法test_demo2
        print("test_demo2输出")  # 打印test_demo2的执行输出信息
