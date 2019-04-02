# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,
# 要求实现客户端和服务端
import socket
from threading import Thread

def conns(conn, conn_addr):
    while 1:
        try:
            msg = conn.recv(65535)
            if not msg:
                break
            msg = msg.decode()
            print('客户端说{}'.format(msg))
            msg = str(input('服务器说：'))
            conn.send(msg.encode())
        except Exception:
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
server.bind(server_addr)
print('服务器已经开启')
server.listen(10)
while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break
    t1 = Thread(target=conns, args=(conn, conn_addr))
    t1.start()
server.close()
print('服务器已经结束')
