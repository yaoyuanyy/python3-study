# 练习 mysql 的使用

import mysql.connector

# 创建一个连接
conn = mysql.connector.connect(user='root', password='Root_123', host='localhost', database='test123')

# 创建一个游标
# cursor = conn.cursor()

# create table
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
#
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Michael2'])

# 将连接的执行 sql 提交事务
# conn.commit();
# # 连接关闭
# conn.close()

cursor = conn.cursor()

# 查找指定id的数据
list_of_ids = [1, 2, 3]
print("list_of_ids", list_of_ids)

format_strings = ','.join(['%s'] * len(list_of_ids))
print("format_strings:", format_strings)

sql = 'select * from user where id in (%s)' % format_strings
print("sql:", sql)

values = tuple(list_of_ids)
print("values:", values)

try:
    cursor.execute(sql, values)

    # 查找全部数据
    # cursor.execute('select * from user')

    result = cursor.fetchall()
    for row in result:
        print(row)

except:
    pass

print("cursor statement:", cursor.statement)
conn.close()

# mysql 官网例子
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
