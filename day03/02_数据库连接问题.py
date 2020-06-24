# -*- coding:utf-8 -*-
"""
1.数据库连接方式
    Django：使用ORM（框架）：本质是调用pymysql，MySQLdb
    flask/其它：
    使用原生sql，pymysql，MySQLdb（只支持python2）
    或者SQLAchemy（ORM框架，与Django不同）：本质是调用pymysql，MySQLdb
2.使用pymysql模块
3.多线程共用Connection对象实现
    a.加锁线程锁，threading.lock()
    b.使用连接池实现
"""
from pymysql import Connection
import threading
lock = threading.Lock()
con = Connection(host='127.0.0.1', user='root', password="123456",
                 database='test', port=3306,
                 charset='utf8')
cur = con.cursor()
lock.acquire()
print(cur)
lock.release()
cur.close()
con.close()
