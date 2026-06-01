from operator import add

def setup_module():  # 定义模块级别的setup函数，在模块中所有测试用例执行前运行一次
    print("模块级的setup方法")  # 打印提示信息，表明模块级setup已执行

def teardown_module():  # 定义模块级别的teardown函数，在模块中所有测试用例执行后运行一次
    print("模块级的teardown方法")  # 打印提示信息，表明模块级teardown已执行
# 定义测试类，pytest会自动发现并执行以Test开头的类中的测试方法
class Test_less1:
    def setup_method(self):
        print("setup_method@#!!#")
    def teardown_method(self):
        print("teardown_method#!!$$!")

    def test_add1(self):
        sum_ = add(2, 2)
        assert sum_ == 4
        print('结果正确', sum_)

    def test_2(self):
        print("哈哈哈哈")

    def test_add2(self):
        sum_ = add(1, 2)
        assert sum_ == 3
        print('结果正确', sum_)

    def test_demo1(self):

        print("test_demo1输出")

    def test_demo2(self):
        print("test_demo2输出")

    def setup_class(self):

        print("setup_class输出")

    def teardown_class(self):# 类级别的清理方法 ,在整个测试类所有用例执行完毕后运行一次
        print("teardown_class输出")

    def test_demo3(self,open_1):

        print("test_demo1输出")

    def test_demo4(self,open_1):

        print("test_demo2输出")