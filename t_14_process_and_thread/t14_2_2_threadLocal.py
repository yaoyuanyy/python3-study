# 创建threadlocal，每个线程的变量放入threadlocal中，取的时候直接取当前线程的变量

import threading

threadLocal = threading.local()


def get_student():
    student = threadLocal.student
    print("cur thread:%s -> student:%s student.name:%s" % (threading.current_thread().name, student, student[0]))


def run_thread(args_student):
    # 存值到threadLocal
    threadLocal.student = args_student
    # 方法取值
    get_student()


thread1 = threading.Thread(target=run_thread, args=("aaa",), name="thread1")
thread2 = threading.Thread(target=run_thread, args=("bbb",), name="thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("cur thread -> %s" % threading.current_thread().name)


