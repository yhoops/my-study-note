"""
案例：演示property属性的用法.

property属性介绍：
    概述/目的/作用：
        把 函数 当作 变量 来使用
    实现方式
        1. 装饰器
        2. 类属性

Property的装饰器用法：
    @property               修饰 获取值的函数
    @获取值的函数名.setter  修饰 设置值的函数

Property的类属性用法：
    注意：没有小括号，两个对象名的顺序也不能变
    类属性名 = property(获取值的函数名, 设置值的函数名)

    之后，就可以直接 .上述的函数名 来当作变量直接用

"""


# 需求：定义学生类，私有age属性，通过property充当类属性使用.
# 1. 定义学生类
class Student:
    def __init__(self):
        self.__age = 18

    # 1.1 定义获取值的函数
    def get_age(self):
        return self.__age

    # 1.2 定义设置值的函数
    def set_age(self, age):
        self.__age = age

    # 1.3 通过property充当类属性使用
    # 参1：获取值的函数名 参2：设置值的函数名
    age = property(get_age, set_age)


# 2. 测试
if __name__ == "__main__":
    # 2.1 创建学生对象
    s = Student()
    # 2.2 设置值
    s.age = 20
    # 2.3 获取值
    print(s.age)
