"""
案例：nonlocal关键字介绍

nonlocal：
    它是Python内置的关键字，可以实现在内部函数中修改外部函数的变量值.
"""

# 需求：编写一个1闭包，让内部函数访问外部函数的参数 a = 100, 并观察结果
# 1. 定义外部函数
def fn_outer():
    # 2. 定义外部函数的(局部)变量 a = 100
    a = 100

    # 3. 定义内部函数
    def fn_inner():
        # 4. 使用nonlocal关键字声明要修改的外部函数变量 a
        nonlocal a
        a = a + 1

        # 5. 打印外部函数的变量 a
        print(a)
        

    # 6. 返回内部函数名(对象)
    return fn_inner

# 7. 测试
if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner() # 101
    fn_inner() # 102
    fn_inner() # 103