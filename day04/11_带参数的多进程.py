"""
案例：演示带参数的多进程.

进程传参有两种方式：
    1. 方式1：args方式，接受所有的 位置参数.
    2. 方式2：kwargs方式，接受所有的 关键字参数.
"""

# 导包
import multiprocessing
# 为了看出来抢CPU资源
import time

# 需求：小明一边敲代码，一边听音乐.
# 1. 定义函数 表示 编写代码.
def coding(name, num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在编写代码{i}小时...")

# 2. 定义函数 表示 听音乐.
def music(name, count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐...")

# 3. 创建两个进程对象，分别对应关联上述两个目标函数
p1 = multiprocessing.Process(target=coding, args=("小明", 10))
p2 = multiprocessing.Process(target=music, kwargs={"name": "小红", "count": 10})

# 4. 启动进程. 大白话：表示进程启动了，就可以开始抢CPU资源了 必须要在main函数中使用
if __name__ == "__main__":
    p1.start()
    p2.start()

"""
1. 说出使用多进程完成多任务步骤？
    1. 导包
    2. 创建进程对象，关联目标函数
    3. 启动进程

2. 进程传参的两种方式是什么？
    1. args方式，接受所有的位置
    2. kwargs方式，接受所有的关键字参数
"""