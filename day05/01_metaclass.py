# -*- coding:utf-8 -*-
"""
1.metaclass的作用
    用来指定当前类是由谁创建的，默认是由type创建的
2.使用metaclass
    python3中
    class m(metaclass=type):
        pass

    python2中
    class m():
        __metaclass__ = type
        pass
3.类是由type()创建的
    class m(object):
        pass
    创建类的方式等价与
    type('m', (object, ), {})
4.自己自定义type（使用MyType创建类本质上时由type创建的）
    a.继承type类
    class MyType(type):
        pass
    b.使用MyType创建类
    class foo(object, metaclass=MyType)
        pass
"""
class m(object, metaclass=type):
    pass