# 多进程 - 进程池
# https://liaoxuefeng.com/books/python/process-thread/process/index.html
import posix
from multiprocessing import Pool
import os, time, random

# 创建进程
## 创建进程时需要传一个方法和一个参数

def create_proc(index):
    print("create process %s (%s pid:%s)..." % (index, os.getpid(), os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("subprocess %s exec %s seconds" % (index, (end - start)))

if __name__ == '__main__':
    print("parent process %s pid %s" % (os.getpid(), os.getppid()))
    # Pool(processes=4).map(create_proc)
    pool = Pool(processes=4)
    for i in range(5):
        pool.apply_async(create_proc, args=(i,))
    print("waiting all subprocesss done...")
    pool.close()
    pool.join()
    print("all subprocess done")


