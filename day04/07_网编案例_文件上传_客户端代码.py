"""
案例：文件上传案例，客户端

回顾：网编客户端实现流程
    1. 创建客户端Socket对象.
    2. 连接服务器的IP和端口号.
    3. 关联数据源文件，读取内容，写给服务器端.
    4. 接收服务器返回的文件上传成功信息.
    5. 释放资源.
"""

# 导包
import socket

# 1. 创建客户端Socket对象 ipv4 tcp.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 连接服务器的IP和端口号
client_socket.connect(("127.0.0.1", 6666))

# 3. 关联数据源文件，读取内容，写给服务器端
# 3.1 关联数据源文件
with open('day04/data/test_data.txt', 'rb') as f:
    # 3.2 循环读取文件
    while True:
        # 3.3 具体的读取操作.
        data = f.read(8192)
        # 3.4 把读取到的数据写给服务器端.
        client_socket.send(data)
        # 3.5 如果读取到的数据是空，说明文件读取完毕
        if not data:
            break

# # 4. 接收服务器返回的文件上传成功信息
# data = client_socket.recv(1024)
# print(f"客户端收到服务器返回的文件上传成功信息：{data.decode('utf-8')}")

# 5. 释放资源
client_socket.close()

