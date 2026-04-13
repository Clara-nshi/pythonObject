# 0. 导包
import socket

# 1. 创建客户端对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器
tcp_client_socket.connect(('127.0.0.1', 8080))
while True:
    # 3. 发送消息给服务器
    data = input('请您输入给服务器消息')
    tcp_client_socket.send(data.encode('utf8'))
    # 4. 接收服务器返回的消息
    server_message = tcp_client_socket.recv(1024)
    if len(server_message) == 0:
        print('服务器已关闭，与它的会话终止！')
        break
    else:
        print(f'服务器回复消息：{server_message.decode("utf8")}')
# 5. 关闭套接字
tcp_client_socket.close()