# 线程
# https://liaoxuefeng.com/books/python/process-thread/thread/index.html
## 创建线程

import threading
import time


## 创建线程执行的函数

def loop():
    print('loop thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread name is >>> %s" % threading.current_thread().name)
        time.sleep(1)
    print("thread %s ended" % threading.current_thread().name)


print("main thread %s is running" % threading.current_thread().name)

## 执行线程
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("main thread %s ended" % threading.current_thread().name)
