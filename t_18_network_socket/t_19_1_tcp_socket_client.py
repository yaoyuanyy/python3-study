# python socket coding
# refer to https://liaoxuefeng.com/books/python/network/tcp/index.html

# 客户端
import socket


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 连接douban
s.connect(("www.baidu.com", 80))

# 发送请求
i = s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
print("send result i:", i)

buffer = []
while True:
    byteList = s.recv(1024)
    if byteList:
        buffer.append(byteList)
    else:
        break

data = b"".join(buffer)


s.close()
print("close after data", data)


# 返回的data是长长的字符串，这些字符串是页面的html信息，把他们写入baidu.html文件
(header, content) = data.split(b"\r\n\r\n", 1)
with open("baidu.html", "wb") as f:
    f.write(content)





