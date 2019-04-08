import socket
from concurrent.futures import ThreadPoolExecutor

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(('127.0.0.1', 6206))


def conn_send(cli):
    while 1:
        msg = input('请输入消息:（输入q退出！）')
        if msg == 'q':
            msg1 = '我断开连接了'
            cli.send(msg1.encode())
            cli.close()
            exit()
        else:
            try:
                cli.send(msg.encode())
            except Exception:
                break


def conn_recv(cli):
    while 1:
        try:
            return_msg = cli.recv(65535)
        except Exception:
            break
        print(return_msg.decode())


pools = ThreadPoolExecutor(max_workers=50)
pools.submit(conn_send, cli)
pools.submit(conn_recv, cli)