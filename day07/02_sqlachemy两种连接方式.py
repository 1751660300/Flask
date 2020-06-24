# -*- coding:utf-8 -*-
"""
1.导包
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import Users
2.使用engine创建连接池
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
3.使用sessionmaker从连接池中获取连接
    Session = sessionmaker(bind=engine)
4.使用Session创建一个cursor（相当与）
    session = Session()
5.实例化需要添加进数据库中的类
    obj1 = Users(name="alex1")
6.对数据库中的表进行操作
    # 添加对象，向数据库中添加啊数据
    # 除了add还有很多其他的方法
    session.add(obj1)

    # 提交事务
    session.commit()
    # 关闭session连接（放回连接池）
    session.close()

"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
import Users  # 需要创建表的类

# 创建连接池
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)

# 获取连接
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
# session = Session()

# 第二种连接
session = scoped_session(Session)
# 自认为是这种方式实现的，不过scoped_session(Session)中是使用threading.local来代替字典的
'''
class foo(object):
    def __init__(self):
        object.__setattr__(self, 'list', {})

    def __getattr__(self, item):
        return self.list.get(item)

    def __setattr__(self, key, value):
        self.list[key] = value


f = foo()
f.__setattr__("add", lambda a, b:a+b)
print(f.add(1, 2))
'''

# ############# 执行ORM操作 #############
# 实例化对象
obj1 = Users(name="alex1")
# 添加对象，向数据库中添加啊数据
session.add(obj1)

# 提交事务
session.commit()
# 关闭session连接（放回连接池）
session.close()
