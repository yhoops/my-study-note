"""
案例：演示多进程入门案例.

多进程目的：
    它属于多任务的一种实现方式，目的是充分利用CPU资源，提高程序执行效率.

实现方式：
    1. 导包
    2. 创建进程对象，关联目标函数.
    3. 启动进程.
"""


# 导包
import multiprocessing
from statistics import median

# 1. 定义函数 表示 编写代码.
def coding():
    for i in range(1,11):
        print(f"正在编写代码{i}小时...")

# 2. 定义函数 表示 听音乐.
def music():
    for i in range(1,11):
        print(f"正在听音乐{i}小时...")

# 3. 创建两个进程对象，分别对应关联上述两个目标函数
# 3.1 进程p1关联 coding函数，p1进程抢到cpu资源了，就会执行这个函数
p1 = multiprocessing.Process(target=coding)
# 3.2 进程p2关联 music函数，p2进程抢到cpu资源了，就会执行这个函数
p2 = multiprocessing.Process(target=music)


# 4. 启动进程. 大白话：表示进程启动了，就可以开始抢CPU资源了 必须要在main函数中使用
if __name__ == "__main__":
    p1.start()
    p2.start()

