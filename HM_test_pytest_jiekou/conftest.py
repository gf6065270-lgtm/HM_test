import pytest
@pytest.fixture(scope="class")  # 定义一个模块级别的fixture，确保在整个模块中只初始化和清理一次
def open_1():  # 定义名为open_1的fixture函数
    print("打开计算器")  # 在测试开始前执行，模拟打开计算器的操作
    yield  # 暂停执行，将控制权交给测试用例，测试结束后继续执行yield之后的代码
    print("关闭计算器")  # 在测试结束后执行，模拟关闭计算器的操作

"""
conftest.py：是 pytest 的一个特殊配置文件，用于定义全局或局
部的 fixture。它可以让你在不同的测试文件中共享 fixture，避免
代码重复。
⚫ 使用场景
⚫ 共享 fixture：当多个测试文件需要使用相同的 fixture 时，可以将这些
fixture 定义在 conftest.py 中。
⚫ 全局配置：可以在 conftest.py 中定义一些全局的配置，如日志设置、
环境变量等。测试方法中引用fixture装饰器定义函数名作为形参传入
作用域
function（默认值）：每个测试函数执行一次 fixture。
⚫ class：每个测试类执行一次 fixture。
⚫ module：每个测试模块执行一次 fixture。
⚫ session：整个测试会话执行一次 fixture。

"""
