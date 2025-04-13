# 练习 sqlite 的使用

# 引入 sqlite
import sqlite3

# 创建新的连接
conn2 = sqlite3.connect("test.db")

# 创建新游标
cursor2 = conn2.cursor()

# result = cursor2.execute('select * from user where id>?', ('1',))
# for row in result:
#     print("row:", row)

c = cursor2.execute('select * from user where id = ? and name=?', ('3', 'ccc'))
data = c.fetchall()
for row in data:
    print("r:", row)
