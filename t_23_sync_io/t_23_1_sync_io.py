# 协程

# 协程的优点：1.没有线程切换开销；2.不存在锁，即没有锁竞争

# 协程讲解
# https://python3.info/advanced/generator/send.html
# https://peps.python.org/pep-0342/

def consumer():
    r = ''
    while True:
        print('consumer r value is %s' % r)
        n = yield r
        print('consumer r value is %s; n value is %s' % (r, n))
        if not n:
            return
        print('consumer ing %s' % n)
        r = '200 OK'


def producer(c):
    c.send(None)
    print('producer producing c.send None')
    n = 0
    while n < 3:
        n = n + 1
        print('producer producing %s' % n)
        r = c.send(n)
        print('producer c.send n:%s r:%s' % (n, r))
    c.close()


c = consumer()
producer(c)

