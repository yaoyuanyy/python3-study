from types import MethodType

# python动态绑定属性和方法，java等静态语言很难做到


class Person:
    pass


person1 = Person()
# 动态绑定一个属性给实例
person1.name = 'test'
print("给实例动态绑定一个属性name =>", person1.name)


def setName(self, name):
    self.name = name


# 动态绑定一个方法给实例
person1.set_name = MethodType(setName, person1)
person1.set_name("显示新的name值")
print(person1.name)


# 动态绑定一个方法给类
def getName(self):
    return self.name


person1.get_name = getName
print("通过动态绑定到类的方法，输出name值", person1.get_name)

