#! /usr/bin/python


# # 类属性 和 实例属性

class Student:
    num = 0  # 这是类属性

    def __init__(self, name, age):
        self.name = name  # 这是实例属性
        self.age = age  # 这是实例属性


print(Student.num)
print(Student("tt", 30).name)
