#! /usr/bin/python3

# 类似java 中的 switch

age = 10

match age:
    case age if age > 15:
        print("< 10")
    case 10:
        print("is 10")
    case 11 | 12:
        print("is 11 or 12")
    case _:
        print("other is here")
