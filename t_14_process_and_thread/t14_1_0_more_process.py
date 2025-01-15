# 多进程
# https://liaoxuefeng.com/books/python/process-thread/process/index.html

from multiprocessing import Process
import os

# 创建进程
## 创建进程时需要传一个方法和一个参数

def create_proc(name):
    print("create process %s (%s pid:%s)..." % (name, os.getpid(), os.getppid()))

if(__name__ == "__main__"):
    print("parent process is %s:" % os.getpid())
    process = Process(target=create_proc, args=("child_test",))
    print("child process had created")
    process.start()
    process.join(1000)
    print("child process had terminated")



# 附录
## 学习时的疑问
# 1. Process这个class的声明中没有 target 和 args 两个入参，编写代码时为啥支持的，我自己随便写个ttt=111，程序就报错了呢，如下
# process = Process(target=create_proc, args=("child_test",), ttt=111)
# 进入源码发现 Process(process.BaseProcess)
#    class BaseProcess(object):
#        def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):

## 结论：所以，只要是class 中的 __init__方法中有入参，使用这个类时就可以传入这些个参数
