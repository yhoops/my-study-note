"""
案例：获取进程的编号.

进程的编号解释：
    概述：
        在设备中每个程序都有自己的唯一进程ID
        当程序释放的时候，该进程ID也会释放
        即：进程ID是可以重复使用的
    目的：
        1. 查看子进程和父进程的关系，方便管理
        2. 例如：杀死指定进程，创建子进程...
    格式：
        查看当前的进程PID：
            os模块(oprating system)中的 os.getpid() 函数.
            multiprocessing模块中的current_process().pid 属性
        查看当前进程的ppid：
            os.getppid() 函数.

细节：
    main中创建的进程，如果没有特殊指定，它的父进程都是main进程.
    main进程的父进程是当前使用编译器(例如我使用的是PyCharm)的PID
"""

# 导包
import multiprocessing
import os

# 为了看出来抢CPU资源
import time


# 需求：小明一边敲代码，一边听音乐.
# 1. 定义函数 表示 编写代码.
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f"{name}正在编写代码{i}小时...")
    print(
        f"当前项目的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为: {os.getppid()}"
    )


# 2. 定义函数 表示 听音乐.
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐...")
    print(
        f"当前项目的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为: {os.getppid()}"
    )


# 3. 创建两个进程对象，分别对应关联上述两个目标函数
p1 = multiprocessing.Process(target=coding, args=("小明", 10))
p2 = multiprocessing.Process(target=music, kwargs={"name": "小红", "count": 10})

# 4. 启动进程. 大白话：表示进程启动了，就可以开始抢CPU资源了 必须要在main函数中使用
if __name__ == "__main__":
    # 5. 开启子线程
    p1.start()
    p2.start()

    # 6. 查看主进程的信息.
    print(
        f"main进程的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为: {os.getppid()}"
    )
