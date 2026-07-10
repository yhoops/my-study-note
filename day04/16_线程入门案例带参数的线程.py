"""
概念：
    1. 什么是线程？
        线程依附于进程执行，是CPU调度的基本单元.
    2. 线程的作用是什么？
        线程用来实现多任务编程.

线程创建的步骤
    1. 导入模块
    import threading

    2. 通过线程类创建线程对象
    线程对象 = threading.Thread(target=目标函数, args=参数元组)

    3. 启动线程执行任务.
    线程对象.start()

线程和进程的关系：
    1. 进程是CPU分配资源的基本单位，线程是CPU调度资源的最小单位.
    2. 线程是依附于进程的，每个进程至少有一个线程(主线程).
    3. 进程间数据相互隔离，(同一个进程的)线程间数据可以共享.

案例：一边听音乐，一边写代码
"""

# 导包.
import threading
import time


# 1. 定义函数，表示：敲代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}次代码...")


# 2. 定义函数，表示：听音乐
def music(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐...")


# 3. 测试
if __name__ == "__main__":
    # 4. 创建线程对象
    t1 = threading.Thread(target=coding, args=("yhoops", 20))
    t2 = threading.Thread(target=music, kwargs={"num": 20, "name": "yhoops"})
    # 自定义线程没有启动之前，没有资格跟主线程争夺资源
    t1.start()
    t2.start()
