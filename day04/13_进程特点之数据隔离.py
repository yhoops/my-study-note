"""
案例：演示进程的特点.

进程的特点：
    1. 进程之间是相互隔离的.
        因为子进程相当于父进程的"副本"，会将父进程的main外资源拷贝一份，即：各是各的
    2. 默认情况下主进程会等待子进程结束再结束.
"""

# 需求：定义1个公共的容器 my_list = [],一个进程往里面写数据，一个进程往里面读数据，看是否能读取到
import multiprocessing
import time

# 1. 创建一个公共容器 my_list = []
my_list = []


# 2. 定义函数，往容器中添加数据
def add_data():
    for i in range(1, 6):
        my_list.append(i)
        print(f"添加了数据：{i}")

    # 走到这里，说明添加完毕，打印即可
    print(f"add_data函数：{my_list}")


# 3. 定义函数，往容器中读取数据
def read_data():
    time.sleep(3)
    print(f"read_data函数：{my_list}")


print("我是main外资源，看我执行了几次")

# 4. 测试.
if __name__ == "__main__":
    # 创建进程对象
    p1 = multiprocessing.Process(target=add_data)
    p2 = multiprocessing.Process(target=read_data)

    # 启动进程
    p1.start()
    p2.start()

    # print("我是main内资源，看我执行了几次")
