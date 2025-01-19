# 两个线程执行一个共享变量
import threading
import time

balance = 0


def changeIt(n):
    # 引用global时刻：内部函数有引用外部函数相同的变量或全局变量，并且对这个变量有修改的时候，此时python会认为它是一个局部变量，而函数中并没有x的定义和赋值，所有报错
    # 声明为global，是告诉python解释器balance为全局变量。修改后依然是全局变量。
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        changeIt(n)


thread1 = threading.Thread(target=run_thread, args=(5,))
thread2 = threading.Thread(target=run_thread, args=(9,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("balance:", balance)


