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

    ※重点：
    例如：
        @property
        def age(self):
            return self.__age
        这是一个获取值的函数

        那么设置值的函数应该这么写(.setter前面的 内容是 获取值函数的 函数名 不是类名)
        @age.setter
        def age(self, age):
            self.__age = age

    之后，就可以直接，上述的函数名 来当作变量使用

    从某方面来说可以提高安全
"""


# 需求：定义学生类，私有属性 age ，通过property实现简化调用
# 1. 定义学生类
class Student:
    # 1.1 定义私有属性
    def __init__(self):
        self.__age = 18

    # 1.2 提供公共的访问方式
    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, age):
        # 可以在这里对传入的age值进行判断，但是一般不做，重要字段才会做判断.
        # 因为实际开发中数据是从前端传过来的，已经做过判断了，这里做属于二次校验.
        self.__age = age


# 2. 测试
if __name__ == "__main__":
    # 2.1 创建学生对象
    s = Student()
    # 2.2 设置值
    # s.set_age(20)
    s.age = 20
    # 2.3 获取值
    print(s.age)
