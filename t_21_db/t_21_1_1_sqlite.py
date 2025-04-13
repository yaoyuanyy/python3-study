# 练习 sqlite 的使用

# 引入 sqlite
import sqlite3

# 创建连接 sqlite 数据库, 数据库文件不存在则创建一个
conn = sqlite3.connect("test.db")

# 使用连接 创建游标: cursor
cursor = conn.cursor()

# 使用游标 执行sql：创建一个表
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
print("Table created successfully")

# 使用游标 执行sql：insert 一条语句
cursor.execute("insert into user (id, name) values (\'1\', \'Michael2\')")
cursor.execute("insert into user (id, name) values (\'2\', \'b\')")
cursor.execute("insert into user (id, name) values (\'3\', \'ccc\')")
cursor.execute("insert into user (id, name) values (\'6\', \'小刘\')")
cursor.execute("insert into user (id, name) values (\'5\', \'小wang\')")
cursor.execute("insert into user (id, name) values (\'4\', \'xiao李\')")

# 使用游标 查看插入的行数
print("rowcount: %s lastrowid:%s" % (cursor.rowcount, cursor.lastrowid))

# 提交事务
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()







