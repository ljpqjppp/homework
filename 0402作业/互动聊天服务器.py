# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,
# 要求实现客户端和服务端
import socket
from threading import Thread

conn_lists = list()


def handle_conn(conn, addr):
    while 1:
        msg = conn.recv(65535)
        return_msg = '地址在{}的用户说:{}'.format(addr, msg.decode())
        for conn in conn_lists:
            conn.send(return_msg.encode())


def conn_server(addr):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(addr)
    ss.listen()
    print('服务器已经启动')
    # 会阻塞 等待链接进来
    
    while 1:
        conn, addr = ss.accept()
        conn_lists.append(conn)
        print('新来链接,地址{}'.format(addr))
        handle = Thread(target=handle_conn, args=(conn, addr))
        handle.start()


if __name__ == "__main__":
    addr = ("127.0.0.1", 9520)
    conn_server(addr)
