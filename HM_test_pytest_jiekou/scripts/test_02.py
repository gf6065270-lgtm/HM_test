#方法级别,总结：运行于测试方法的始末，即：运行一次测试方法
# 就会运行一次setup_method和teardown_method
class Test_method:
    # 前置处理：在每个测试方法执行前运行
    def setup_method(self):
        print("setup_method@#!!#")
        # 后置处理：在每个测试方法执行后运行
    def teardown_method(self):
        print("teardown_method#!!$$!")

        # 测试用例1：演示基本输出
    def test_demo1(self):

        print("test_demo1输出")

    def test_demo2(self):
        print("test_demo2输出")