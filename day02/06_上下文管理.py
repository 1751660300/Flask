# -*- coding:utf-8 -*-
"""
1.使用 threading.local() 对象，会给每一个线程开辟一个独有的空间，可以避免加锁
2.request
    a.单进程单线程的情况下，一定不会出问题，基于全局变量
    b.单进程多线程的情况下，可以基于threading.local对象
    c.单进程单线程多协程的情况下，threading.local对象做不到，可以重写一个类似与threading.local的对象
3.自定义支持协程的threading.local
    要点：a.获取一个线程的唯一标识
        from _thread import get_ident
        b.获取一个协程的唯一标识
        from greenlet import getcurrent
        c.类中__setattr__方法
            执行 类的实例化对象.xxx = xxx 这句代码的时候会调用 __setattr__这个方法
        d.类中__getattr__方法
            执行 类的实例化对象.xxx 这句代码的时候会调用 __getattr__这个方法
        e.如果使用了c，d则创建self.lock_dict = {}时要改变创建方式为
            object.__setattr__(self, "local_dict", {})
            否则会引起递归循环
"""
try:
    from _thread import get_ident
except:
    from greenlet import getcurrent as get_ident
import threading


# class local(object):
#     def __init__(self):
#         self.lock_dict = {}
#         self.get_ident = get_ident
#
#     def set(self, key, value):
#         self.lock_dict[self.get_ident()] = {key: value}
#
#     def get(self, key):
#         try:
#             return self.lock_dict[get_ident()][key]
#         except:
#             return None
class local(object):
    def __init__(self):
        object.__setattr__(self, "local_dict", {})
        object.__setattr__(self, "get_ident", get_ident)

    def __setattr__(self, key, value):
        self.local_dict[self.get_ident()] = {key: value}

    def __getattr__(self, item):
        try:
            return self.local_dict[self.get_ident()][item]
        except:
            return None


local_data = local()


def task(num):
    local_data.__setattr__(num, get_ident())
    print(local_data.local_dict)


for i in range(10):
    td = threading.Thread(target=task, args=(i,), name="name {}".format(i))
    td.start()


