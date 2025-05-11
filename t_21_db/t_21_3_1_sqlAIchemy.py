# sql mapping db

import mysql.connector

from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建基类
Base = declarative_base()


class User(Base):
    # 映射的表名
    __tablename__ = 'user'

    # 映射到表的字段
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:Root_123@localhost:3306/test123')

# 创建session类型，即当前数据库连接
DBsession = sessionmaker(bind=engine)

# 创建session
session = DBsession()

# # 创建
# new_user1 = User(id=111, name='test111')
# new_user3 = User(id=333, name='test333')
#
# session.add(new_user1)
# session.add(new_user3)
# session.commit()
# session.close()

readSession = DBsession()
user = readSession.query(User).filter(User.id == '11').one()
print("name:%s user type:%s" % (user.name, type(user)))
readSession.close()
