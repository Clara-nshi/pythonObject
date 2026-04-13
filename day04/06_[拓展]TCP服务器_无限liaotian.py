# 0. 导包
import socket
# 1. 创建服务器对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定服务器的ip 和端口号 注意：放到元组中包裹
tcp_server_socket.bind(('', 8080))
# 3. 设置监听个数
tcp_server_socket.listen(128)
# 4. 一直阻塞等待任意客户端连接，直到连接成功并返回新的连接对象为止
# 注意：有返回参数需要接收
# 此处直接用拆包，参数1：连接通的 tcp_server_socket 对象
# 参数2：客户端地址
while True:
    conn_tcp_server_sock, client_addr = tcp_server_socket.accept()
    print(f'{client_addr[0]}客户端访问了~')
    while True:
        # 5. 先接收客户端消息
        client_message = conn_tcp_server_sock.recv(1024)
        if len(client_message) == 0:
            print('客户端已关闭')
            break
        print(f'{client_addr[0]}客户端发来消息：{client_message.decode("utf8")}')
        # 6. 给客户端回复消息
        data = input('请您输入给客户端回复的消息：')
        conn_tcp_server_sock.send(data.encode('utf8'))

    # 7. 先关闭连接对象
    conn_tcp_server_sock.close()
