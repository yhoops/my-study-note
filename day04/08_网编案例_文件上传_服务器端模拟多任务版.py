"""
案例：文件上传案例，服务器端

回顾：网编服务器端实现流程
    1. 创建服务器端Socket对象
    2. 绑定IP地址和端口号
    3. 设置最大监听数
    4. 等待客户端申请建立连接
    5. 读取客户端上传的文件数据
    6. 把读取到的数据写到目的地文件中
    7. 释放资源.
"""

# 导包
import socket

# 1. 创建服务端Socket对象 ipv4 tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定IP地址和端口号
server_socket.bind(("127.0.0.1", 6666))

# 3. 设置最大监听数
server_socket.listen(5)

# 新增：通过无限循环模拟多线程的任务，给每个上传的文件进行命名
count = 0
while True:
    count += 1
    file_name = f"day04/data/my_{count}.txt"
    try:
        # 4. 等待客户端建立连接
        accept_socket, client_info = server_socket.accept()

        # 5. 读取客户端上传的文件数据
        # 5.4 把读取到的数据写入到目的地文件中,关联目的地文件.
        with open(file_name, 'wb') as f:
            # 5.1 循环读取数据
            while True: 
                # 5.2 接收客户端上传的文件数据
                data = accept_socket.recv(8192)    # 8192字节 = 8kb
                # 5.3 判断是否读取到数据，无数据说明客户端断开连接，结束即可
                if not data:
                    break
                # 5.5 把读取到的数据写入到目的地文件中
                f.write(data)
        # # 6. 返回文件上传成功
        # accept_socket.send("文件上传成功！".encode('utf-8'))
        # 7. 释放资源
        accept_socket.close()
    except Exception as e:
        pass


