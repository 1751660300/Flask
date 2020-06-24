# -*- coding:utf-8 -*-
"""
1.安装DBUtils
    pip install DBUtils
2.连接池的两种方式
    a.为每一个线程创建一个连接，线程即使调用了close方法，也不会关闭，知识重新放回了连接池，供自己的线程继续使用
        只有线程结束，连接才会自动关闭
    b.创建一些连接，线程共享使用
        因为pymysql等threadsafety值为1，所以连接池的连接会被所有的线程共享
"""
# 方式一
import pymysql
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB
POOL = PersistentDB(
    creator=pymysql,  # 使用连接数据库的模块
    maxusage=None,  # 一个连接最多可以重复使用的次数
    setsession=[],  # 开启会话执行的命令列表，如['set datestyle to ...', 'set time zone']
    ping=0,  # ping mysql 服务端，检查服务是否可用
    # ping=0 不检测，=1   请求时检测， =2  创建cursor时检测 ， =4  query时检测， =7  一直检测
    closeable=False,  # 如果为False时，连接的close方法实际上被忽略，如果为True，则关闭连接，再次连接的时候重新创建
    threadlocal=None,  # 就是threading.local()类，默认就好，也可以是之前写的支持线程的
    host='',
    port='',
    user='',
    password='',
    database='',
    charset=''
)


def fun():
    con = POOL.connection()
    cursor = con.cursor()
    sql = ""
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    con.close()
    return res


fun()

# 方式二
POOL2 = PooledDB(
    creator=pymysql,
    maxconnections=6,  # 连接池应许的最大连接数
    mincached=2,  # 初始化时创建的连接数
    maxcached=5,  # 连接池中最大的闲置连接
    maxshared=0,  # 共享的连接数，这里无用，pymysql默认为1
    blocking=True,  # 连接池中如果没有可用的连接，是否阻塞，True等待， flase报错
    maxusage=None,  # 一个连接最多可以重复使用的次数
    setsession=[],  # 开启会话执行的命令列表，如['set datestyle to ...', 'set time zone']
    ping=0,  # ping mysql 服务端，检查服务是否可用
    host='',
    port='',
    user='',
    password='',
    database='',
    charset=''
)


def fun1():
    con = POOL2.connection()
    cursor = con.cursor()
    sql = ""
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    con.close()
    return res


fun1()
