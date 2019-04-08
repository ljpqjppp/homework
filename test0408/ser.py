import socket
from threading import RLock
from concurrent.futures import ThreadPoolExecutor
from functools import partial

conn_lists = []
lock = RLock()


def broadcast_conn(conn, addr):
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

    while 1:
        conn, addr = ss.accept()
        lock.acquire()   # 上锁来保证加入已链接用户列表里的数据完整
        conn_lists.append(conn)
        lock.release()
        print('新来链接,地址{}'.format(addr))
        pools = ThreadPoolExecutor(max_workers=50)
        pools.submit(partial(broadcast_conn, conn, addr))



if __name__ == "__main__":
    addr = ("127.0.0.1", 6206)
    conn_server(addr)