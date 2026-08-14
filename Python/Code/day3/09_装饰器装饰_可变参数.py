"""
细节：
    装饰器的内部函数格式 要和 被装饰的函数 保持一致,
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的
    原函数有参有返回，即 装饰器的内部函数也必须是 有参有返回的
"""

# 需求：定义1个可以计算多个数据和字典value值和的函数，并给其友好提示.

# 1.定义装饰器.
def my_decorator(func):
    # 1.1 定义内部函数，内部函数的格式必须和 被装饰的函数一致
    def fn_inner(*args, **kwargs):
        # 1.2 额外功能
        print('正在努力计算中...')
        # 1.3 有引用，调用被装饰的原函数
        return func(*args, **kwargs)
    # 1.4 返回内部函数
    return fn_inner


# 2.定义原函数.
@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算 数字列表 和 字典value值的和
    :param args: 数字列表 *args -> 接收所有的位置参数，封装到 元组
    :param kwargs: 字典，键是字符串，值是数字, **kwargs -> 接收所有的关键字参数，封装到 字典
    :return: 返回数字列表和字典value值的和
    """
    # 2.1 定义求和变量.
    sum = 0
    # 2.2 遍历元组，获取每个元素，求和.
    for i in args:
        sum += i
    # 2.3 遍历字典，获取每个value值，求和.
    for v in kwargs.values():
        sum += v
    # 2.4 返回和.
    return sum

# 3. 测试
print(get_sum(1, 2, 3, a=4, b=5))  # 15
