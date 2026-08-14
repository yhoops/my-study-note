"""
互斥锁的使用流程：
    1. 创建互斥锁对象.
    mutex = threading.Lock()
    2. 上锁.
    mutex.acquire()
    3. 释放锁.
    mutex.release()

细节：
    使用互斥锁的时候要在合适的时机释放锁，否则可能出现死锁或者锁不住的情况.
    死锁：等待对方释放锁，对方一直不释放锁/没有在合适的时机释放锁.
    锁不住：有两把或以上的锁，锁不住.

进程和线程的区别：
    1. 线程依赖进程，进程是CPU分配资源的基本单位，线程是CPU调度资源的基本单位.
    2. 进程更消耗资源，不能共享全局变量，相对更稳定.
    3. 线程更轻量级，可以共享全局变量，相对更灵活.
"""

# 导包
import threading

# 1. 定义全局变量.
global_num = 0

# 创建线程锁.
mutex = threading.Lock()


# 2. 定义目标函数1，对全局变量累加100W次.
def target_func1():
    # 上锁
    mutex.acquire()
    print("---start target_func1---")
    # 2.1 声明为全局变量
    global global_num
    for i in range(1000000):  # 100W
        global_num += 1
    print(f"target_func1执行结果：{global_num}")
    # 释放锁
    mutex.release()


# 3. 定义目标函数2，对全局变量累加100W次.
def target_func2():
    # 上锁
    mutex.acquire()
    print("---start target_func2---")
    global global_num
    for i in range(1000000):  # 100W
        global_num += 1
    print(f"target_func2执行结果：{global_num}")
    # 释放锁
    mutex.release()


# 4. 测试.
if __name__ == "__main__":
    # 4.1 创建两个线程，分别关联上述的两个目标函数.
    t1 = threading.Thread(target=target_func1)
    t2 = threading.Thread(target=target_func2)
    # 4.2 启动线程
    t1.start()
    t2.start()
