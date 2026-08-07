"""
案例：网编入门案例，服务器端给客户端发送消息，客户端给出回执消息

服务器端开发流程：
    1. 创建服务器端Socket对象.
    2. 绑定IP地址和端口号.
    3. 设置最大监听数.
    4. 等待客户端申请连接.
    5. 给客户端发送消息.
    6. 接收客户端的信息并打印.
    7. 释放资源.

细节：
    客户端和服务器是通过 字节流(bytes) 的形式实现的

"""

# 导包
import socket

# 1. 创建服务器端Socket对象. ipv4 tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号.
server_socket.bind(("127.0.0.1", 10086))
# 3. 设置最大监听数.
server_socket.listen(5)

# 设置端口号重用，目的是：快速重启服务器（服务器关闭后，立即释放端口）
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)


# 添加 while true 循环，模拟多线程聊天室场景
while True:
    try:
        # 4. 等待客户端申请连接.
        print("等待客户端连接...")
        accept_socket, client_info = server_socket.accept()
        # 5. 给客户端发送消息.
        # 加b的原因是将字母转为二进制，只适用于输出的信息中有字母和数字的情况，有中文不行
        accept_socket.send(b"Welcome to Server!")
        accept_socket.send("欢迎来到服务器".encode("utf-8"))
        # 6. 接收客户端的信息并打印.
        data = accept_socket.recv(1024).decode("utf-8")
        print(f"服务器收到来自 {client_info} 的消息：{data}")
        # 7. 释放资源.
        accept_socket.close()
    except Exception as e:
        print(f"客户端请求发生错误：{e}")


# 扩展：设置端口号重用，目的是：快速重启服务器（服务器关闭后，立即释放端口）
# 参1：当前的套接字对象；参2：选项名；参3：该选项的值
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 一般情况下这个是没用的，因为电脑会自动释放端口占用，但是如果需要快速重启服务器，则需要设置这个选项