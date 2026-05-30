"""学习演示用途
展示 pytest 测试框架的基本使用方法
演示测试类的命名规范（Test_ 开头）
演示测试方法的命名规范（test_ 开头）
基础功能验证
test_add1()：验证加法运算 2+2=4
test_2()：演示 print 输出功能（无断言）
test_add2()：验证加法运算 1+2=3"""

# 从operator模块导入add函数，用于执行加法运算
from operator import add

# 定义测试类，pytest会自动发现并执行以Test开头的类中的测试方法
class Test_less1:
    # 测试方法1：验证2+2的加法运算结果
    def test_add1(self):
        sum_ = add(2, 2)
        assert sum_ == 4
        print('结果正确', sum_)

    # 测试方法2：演示print输出功能
    def test_2(self):
        print("哈哈哈哈")

    # 测试方法3：验证1+2的加法运算结果
    def test_add2(self):
        sum_ = add(1, 2)
        assert sum_ == 3
        print('结果正确', sum_)
