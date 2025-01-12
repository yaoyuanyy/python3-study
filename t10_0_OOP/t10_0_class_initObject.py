#! /usr/bin/python

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 80:
            return "good"
        elif self.score >= 60:
            return "ok"
        else:
            return "no good"


student1 = Student("jundan", 90)
student2 = Student("me", 30)

print("class", student1)
print("student1:", student1.name, student1.get_grade(), sep="_", end="\n\n")
print("student2:", student2.name, student2.get_grade())

# 和静态语言不同，python允许对实例变量绑定任何数据。即对于两个实例变量，虽然他们属于同一个类，但拥有的变量名称可以不同
student1.shenCai = 'i like'
print("student1 shenCai:", student1.name, student1.shenCai)

print("student2 shenCai:", student2.name, student2.shenCai)

