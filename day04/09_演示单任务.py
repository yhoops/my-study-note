"""
案例：演示单任务，前边不执行完毕，后边绝对无法执行,
"""


# 1. 定义函数A，输出10次 hello world
def func_A():
    for i in range(10):
        print("hello world")

# 2. 定义函数B，输出10次 hello python
def func_B():
    for i in range(10):
        print("hello python")

# 3. 调用函数A
func_A()
print('-' * 20)
# 4. 调用函数B
func_B()

"""
1. 进程是什么？
    进程是操作系统CPU资源分配的最小单位
2. 多进程的作用是什么？
    多进程是Python程序中一种实现多任务的一种方式，使用多进程可以大大提高程序的执行效率
3. Python中多进程的基本工作方式？
    程序运行起来形成主进程；在主进程上创建子进程
"""