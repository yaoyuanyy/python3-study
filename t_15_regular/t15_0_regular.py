# 正则表达式
## refer to https://liaoxuefeng.com/books/python/reg-exp/index.html

## 要点：python 中正则表达式通过
# 1. import re 引用
# 2. 在字符串前加上 r 就不用考虑特殊字符转义的问题了
## 如 "ABC\\-010" -> r"ABC\-010"


import re

print(re.match(r"\d{3}\-\d{3,8}", "001-1111"))

print(re.match(r"^\d{3}\-\d{3,8}$", "001-1111-111"))
