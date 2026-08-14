"""
案例：演示socket对象创建

网络编程介绍：
    概述：
        网络编程也叫网络通信，Socket通信，即：通信双方都有自己的Socket对象
        数据在Socket之间通过 数据包(UDP协议) 或者 字节流(TCP协议) 的形式进行传输
    大白话举例：
        你和你遥远的朋友在聊天，看着是你们两个人在交互，实际上是通过两部手机来交互的
"""

# 导入socket包
import socket

# 创建socket对象
# 参1：ADDRESS_FAMILY 地址族：AF_INET：IPV4 ， AF_INET6：IPV6
# 参2：SOCKET_TYPE Socket类型：SOCK_STREAM：TCP， SOCK_DGRAM：UDP
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print(socket_obj)
