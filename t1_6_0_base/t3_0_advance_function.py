#! /usr/bin/python3
from functools import reduce

# 高阶函数

# python 内置了强大的创建list的方式

# list函数
myList = list(range(1, 11))

for i in myList:
    print("元素: %s" % i)

list2 = [x * x for x in range(1, 11)]
for i in list2:
    print("%s" % i)


# map函数 第一个参数是函数，第二个参数是Iterable。对iterable的每个元素执行函数

def fun(x):
    return x * x


r = map(fun, list(range(1, 11)))
print("map: %s" % list(r))


# reduce函数 第一个参数是函数，第二个参数是序列或Iterable。对第二个参数的元素执行函数，把结果继续和序列的下一个元素做累计计算
def add(x, y):
    return x + y


myReduce = reduce(add, [1, 2, 3, 4, 5, 6])
print("reduce result %s" % myReduce)


# sorted函数

mySorted = sorted([2, 43, -11, -45, 3], key=abs)
print("mysorted %s" % mySorted)

# 偏函数 int(str, base=N) N:将str按N的进制进行转换
print(int('1000', 2))
print(int('100', 8))