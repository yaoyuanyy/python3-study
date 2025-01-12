#! /usr/bin/python3

# list 列表 用大括号表示 NOTE: 可变

list2 = ["a", 2, "list"]

for one in list2:
    print("元素是：%s" % one)


list2.insert(2, "二")

print(len(list2))


# set 列表 不能重复&无序

set2 = {"a", 1, "ddd"}
print(set2)
print(set2.add("aaa"))
print(set2)


# tuple 元组 NOTE: 不可变

tuple2 = (1, "2", '3')
for t in tuple2:
    print(f"元组的元素为 %s" % t)

for index, item in enumerate(tuple2):
    print("下标%s，元素%s" % (index, item))

# 对元组访问
print("通过大括号访问元组元素，第二个元素的值", tuple2[1])

# 元组中值为2的元素的个数
print("元组中值为2的元素的个数", tuple2.count(2))
