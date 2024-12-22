#! /usr/bin/python
import types


class Student:
    pass


def fn():
    pass


# 使用 type() 方法获取实例的信息
s = Student()

print(type(s))
print(type(11))
print(type(fn))

# 使用 isInstance 判断实例的类型
print(isinstance(s, Student))
print(isinstance(fn, types.FunctionType))
print(isinstance(111, int))
