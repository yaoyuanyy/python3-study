# python socket coding
# refer to https://liaoxuefeng.com/books/python/network/tcp/index.html

# 创建一个socket服务端

import socket
import threading

# 创建一个socket server

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("create socket server")

socketServer.bind(("127.0.0.1", 8888))
print("binged for port 8888")

# 接收最大5个连接
socketServer.listen(5)
print("Waiting for connection...")


def handleTcpConnection(sock, addr):
    print("开始处理 connection... addr:", addr)
    sock.send(b"Welcome")
    while True:
        data = sock.recv(1024)
        print("我收到了你发来的数据 data:%s data_utf-8:%s" % (data, data.decode("utf-8")))
        if not data or data.decode("utf-8") == "exit":
            print("退出 data:", data)
            break
        sock.send(("我把收到的数据再发回给你 %s" % data.decode("utf-8")).encode("utf-8"))

    sock.close()
    print("sock close addr:", addr)
    socketServer.close()


while True:
    (sock, addr) = socketServer.accept()
    print("收到一个connection...", sock, addr)
    # 创建一个线程来处理这个socket client连接
    t = threading.Thread(target=handleTcpConnection, args=(sock, addr))
    t.start()
    print("thread started... t:", t)


