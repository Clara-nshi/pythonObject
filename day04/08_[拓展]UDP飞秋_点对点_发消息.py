import socket
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 飞秋服务器地址和端口号
server = ('192.168.40.128', 2425)
content = '1:'
udp_client_socket.sendto(content.encode('gbk'), server)
