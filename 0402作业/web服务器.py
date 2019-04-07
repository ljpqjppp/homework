# 书写一个类似于百度的网站服务器,能够使用普通浏览器访问,只用返回简单的hello world即可
import socket
ss = ('0.0.0.0', 5001)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(ss)
listen_socket.listen()
print('服务器运行中')
while 1:
    conn, conn_add = listen_socket.accept()
    msg = conn.recv(65535)
    print(msg)
    msg1 = b"""
	HTTP/1.1 200 OK\r\n
	\r\n
	Helloworld
	"""
    conn.send(msg1)

