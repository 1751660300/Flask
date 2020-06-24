# -*- coding:utf-8 -*-
"""
1.创建表
    a.导包
        from sqlalchemy.ext.declarative import declarative_base
    b.实例化declarative_base
        Base = declarative_base()
    c.创建所要创建表的类
        # 1).首先要继承Base
        class Users(Base):

            # 2).设置表名
            __tablename__ = 'users'

            # 3).设置字段，Column(Integer, primary_key=True)中是表字段的属性
            id = Column(Integer, primary_key=True)
            name = Column(String(32), index=True, nullable=False)
            # email = Column(String(32), unique=True)
            # ctime = Column(DateTime, default=datetime.datetime.now)
            # extra = Column(Text, nullable=True)

            # 4).联合索引
            __table_args__ = (
                # UniqueConstraint('id', 'name', name='uix_id_name'),  # 唯一联合索引
                # Index('ix_id_name', 'name', 'email'),  # 普通联合索引
            )
            # 问题：如何设置表的编码格式；如何指定数据库的引擎
    d.创建表
        # 创建与数据库的连接
        engine = create_engine(
            "mysql+pymysql://root:123@127.0.0.1:3306/s6?charset=utf8",  # 连接数据库的信息
            max_overflow=0,  # 超过连接池大小外最多创建的连接
            pool_size=5,  # 连接池大小
            pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
            pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        )
        # 创建表
        Base.metadata.create_all(engine)

    删除表：
        Base.metadata.drop_all(engine)
    给字段添加外键：
        hobby_id = Column(Integer, ForeignKey("hobby.id"))
        参数是 表名.字段
        ForeignKey("hobby.id")
2.操作表
"""
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)

    # 时间函数不能加括号，否则就相当于与是具体的数值
    ctime = Column(DateTime, default=datetime.datetime.now)

    extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'email'),
    )


# 一对多的表结构
class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    hobby_id = Column(Integer, ForeignKey("hobby.id"))


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/s6?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)


# ##################### 多对多示例 #########################
class Server2Group(Base):
    __tablename__ = 'server2group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/s6?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
