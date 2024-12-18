print('\u4e2d\u6587')

# 字符串函数
print('ABC'.encode("utf-8"))
print(len('abc'))

# 字符串格式化 - 方式一
print("name: {0} age: {1}".format("jundan", 20))

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 - s1) / s1
# 字符串格式化 - 方式二
print(f"提高了 {r:.1f}")

# 字符串格式化 - 方式三
print("hello, %s" % "world")
print("hello, %s, num:%d" % ("world", 10))
