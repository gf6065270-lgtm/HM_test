#类级别 ,运行于测试类的始末，即：每个测试类只会
# 运行一次setup_class和teardown_class
class Test_class:# 测试类示例，演示 pytest 的类级别 fixture 用法

    def setup_class(self):
        """
        类级别的初始化方法,在整个测试类开始执行前运行一次

        """
        print("setup_class输出")

    def teardown_class(self):# 类级别的清理方法 ,在整个测试类所有用例执行完毕后运行一次
        print("teardown_class输出")

    def test_demo1(self):#测试用例



        print("test_demo1输出")

    def test_demo2(self):

        print("test_demo2输出")