# python socket coding
# refer to https://liaoxuefeng.com/books/python/network/tcp/index.html

# 创建 python socket client 实例

# 引入 socket
import socket


# 创建 socket client 对象实例
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=-1, fileno=None)


# 使用 socket 连接 baidu.com 服务器
s.connect(("www.baidu.com", 80))

# 使用 socket 请求 baidu.com 服务器
i = s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
print("send result i:", i)

buffer = []
while True:
    # 使用 socket 接收服务器的数据
    # 每次最多接收1024个字节
    byteList = s.recv(1024)
    if byteList:
        buffer.append(byteList)
    else:
        break

data = b"".join(buffer)

# 关闭 socket
s.close()
print("socket close")
print("baidu server data：", data)


# 返回的data是长长的字符串，这些字符串是页面的html信息，把他们写入baidu.html文件
(header, content) = data.split(b"\r\n\r\n", 1)
print("baidu server header:", header)

with open("baidu.html", "wb") as f:
    f.write(content)





