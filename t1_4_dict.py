#! /usr/bin/python3

# dict 字典 同java中的map

dict2 = {"name":"jundan", "age":20, "action":"k u"}

print(dict2)

print(dict2["name"])
print(dict2.get("name"))

print(dict2.get("not exist"))
# print(dict2["not exist"]) 会报错
print("not exist" in dict2.keys())

