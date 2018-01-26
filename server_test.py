import socket
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waitting for connection...')


def tcplink(socket, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8' == 'exit'):
            break
        socket.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    socket.close()
    print('Connection from %s:%sclosed.' % addr)


# 创建永久循环来接受客户端的连接，
while True:
    # 接收一个新连接
    socket, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(socket, addr))
    t.start()
