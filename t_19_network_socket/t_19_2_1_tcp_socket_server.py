# python socket coding
# refer to https://liaoxuefeng.com/books/python/network/tcp/index.html

# 创建 python socket server 实例

# 引入socket
import socket
import threading

# 创建 socket server 对象实例
socketServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=-1, fileno=None)
print("created socket server")

# 使用 socket server 绑定ip:port
socketServer.bind(("127.0.0.1", 8888))
print("binded socket server with port 8888")

# 使用 socket server 创建5个监听，即最大等待连接个数
socketServer.listen(5)
print("listened and Waiting for connection...")


def handleTcpConnection(sock, addr):
    print("开始处理 connection... addr:", sock, addr)
    sock.send(b"Welcome")
    while True:
        # 使用 socket server接收最大1024个字节
        data = sock.recv(1024)
        decodeData = data.decode("utf-8")
        print("\r\n\r\n收到的数据 data:%s data_utf-8:%s 处理线程为:%s" % (data, decodeData, threading.current_thread().name))
        if not data or decodeData == "exit":
            print("收到 exit 此线程退出:", threading.current_thread().name)
            break
        reSendData = "数据再发回去 %s" % decodeData
        print("reSendData:", reSendData)
        sock.send(reSendData.encode("utf-8"))

    sock.close()
    print("sock close addr:", addr)


while True:
    (sock, addr) = socketServer.accept()
    print("\r\n\r\n收到一个connection... 创建一个线程处理它", sock, addr)
    # 创建一个线程来处理这个socket client连接
    t = threading.Thread(target=handleTcpConnection, args=(sock, addr))
    print("thread started... t:", t)
    t.start()

socketServer.close()
print("socketServer closed")



