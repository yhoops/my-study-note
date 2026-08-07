"""
案例： 演示 带参数的装饰器

记忆：
    1. 1个装饰器的参数有且只能有 1个
    2. 如果装饰器有多个参数，可以在该装饰器的外面再包裹一层，把装饰器当做其内部函数 返回即可.

"""

# 需求：定义1个既能装饰减法，又能装饰加法的装饰器 -> 即：带有参数的装饰器

def logging(flag):
# 1. 定义装饰器
    def my_decorator(func):   # func 原函数名， flag 标记
        # 1.1 定义内部函数，内部函数的格式必须和 被装饰的函数一致
        def fn_inner(a, b):
            # 1.2 增加额外功能
            if flag == '+':  
                print('正在计算 [加法] ...')
            elif flag == '-':
                print('正在计算 [减法] ...')
            # 1.3 执行被装饰的函数
            return func(a, b)
        # 1.4 返回内部函数
        return fn_inner
    # 返回my_decorator
    return my_decorator



# 2. 定义原函数，表示：加法运算
@logging(flag='+')
def add(a, b):
    return a + b

# 3. 定义原函数，表示：减法运算
@logging(flag='-')
def sub(a, b):
    return a - b

# 4. 测试
print(add(10, 20))
print(sub(20, 10))