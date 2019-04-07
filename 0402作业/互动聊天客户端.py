import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
client.connect(server_addr)
while 1:
    try:
        msg = input('客户端说:')
        client.send(msg.encode())
        msg = client.recv(65535)
        print('服务器说:', msg.decode())
    except Exception:
        break
client.close()
print('链接已经完成')
