from enum import Enum


# 创建一个枚举
Month = Enum("month", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

print(Month.__name__)

for key, value in Month.__members__.items():
    print(key, "=>", value, "=>", value.value)

for key in Month.__members__.keys():
    print(key)

for value in Month.__members__.values():
    print(value, "=>", value.name, "=>", value.value)

# 自定义一个枚举类
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2

print(Weekday.Sun)
print(Weekday(1))
print(Weekday["Sun"])


for name, member in Weekday.__members__.items():
    print("Weekday enum=>", name, "=>", member);