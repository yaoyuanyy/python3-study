# 定义函数

def my_abc(x):
    if x > 0:
        return x
    else:
        return -x

# 调用函数
print(my_abc(10))
print(my_abc(-10))



def moreParams(x, y):
    return x * x, y * y

# 返回的是一个元组，只是小括号省略了
a, b = moreParams(10, 5)
print(a, b)
