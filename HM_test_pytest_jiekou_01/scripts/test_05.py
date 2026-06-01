import pytest  # 导入pytest测试框架

@pytest.fixture(scope="module")  # 定义一个模块级别的fixture，确保在整个模块中只初始化和清理一次
def open_1():  # 定义名为open_1的fixture函数
    print("打开计算器")  # 在测试开始前执行，模拟打开计算器的操作
    yield  # 暂停执行，将控制权交给测试用例，测试结束后继续执行yield之后的代码
    print("关闭计算器")  # 在测试结束后执行，模拟关闭计算器的操作

class Test_05:  # 定义测试类Test_05
    def test_demo(self, open_1):  # 定义测试方法test_demo，并注入open_1 fixture
        print("测试用例哈啊哈")  # 执行具体的测试逻辑，此处仅为打印示例


"""

"""