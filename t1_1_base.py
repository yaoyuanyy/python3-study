a = 1

if a > 10:
    print("a is greater than 10 %s" % a)
else:
    print("a is less than 10 %s" % -a)

# r表示 '' 中的内容不转义;
print("hello \n world")
print(r"hello \n world")

# python 允许使用 "'''" 表示多行内容。
print(r'''hello,
a
b
c
\n world''')

# 逻辑运算符 and or not
name = "a"
age = 10

if age < 20 and name != "aa":
    print("a is greater than")

if not 10 < 5:
    print("a is less than bb")

