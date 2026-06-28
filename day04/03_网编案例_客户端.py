# 导入socket包
import socket

# 1. 创建客户端Socket对象. ipv4 tcp
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器.
client_socket.connect(("127.0.0.1", 10086))
# 3. 接收数据
data = client_socket.recv(1024).decode("utf-8")
print(f"客户端收到消息 {data}")
# 4. 发送数据
client_socket.send("hello, server".encode("utf-8"))
# 5. 释放资源.
client_socket.close()
print("客户端已退出")
