# -*- coding:utf-8 -*-
"""
SQLAlchmey详细：https://www.cnblogs.com/wupeiqi/articles/8259356.html
1.SQLAlchmey 是python中一种orm框架
    目标：将对类/对象的操作 -> sql语句（通过pymysql模块来执行sql语句） -> 对数据库的操作

"""
import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/t1?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)


def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from t1"
    )
    result = cursor.fetchall()
    cursor.close()
    conn.close()


for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()

