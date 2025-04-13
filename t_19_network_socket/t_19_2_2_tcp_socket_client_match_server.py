# python socket coding
# refer to https://liaoxuefeng.com/books/python/network/tcp/index.html

# 客户端
import socket


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 连接douban
s.connect(("127.0.0.1", 8888))

text = s.recv(1024).decode("utf-8")
print("recv text:", text)

for data in [b"aaa", b"bbb", b"ccc"]:
    s.send(data)
    print("sent data:%s " % data)

    recvData = s.recv(1024).decode("utf-8")
    print("recv data:", recvData)


print("发送数据:exit")
s.send(b"exit")
s.close()




