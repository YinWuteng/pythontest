import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接受数据
buffer = []
while True:
    # 每次最多接受1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
