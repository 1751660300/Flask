# -*- coding:utf-8 -*-
"""
1.补充：
    a.偏函数
        导入包： from functools import partial
        使用partial()方法时，传递一个函数，和函数所需的若干个参数，返回一个新的函数，新函数所需参数个数
        是函数的参数个数 - 已经传递的参数个数
   b.实现面向对象的方法
   c.itertools 的 chain 方法 将两个可迭代对象串接起来, 返回chain对象, 也可以传递方法
2.上下文管理详细
    a.首先说明线程的 threading.local 有什么作用
    b.flask在内部自己定义了一个local类，与 threading.local功能一样，只是local类支持协程，
      而threading.local不支持协程
    c.request的请求流程
        -当请求到来时，flask将request和session封装成ctx对象，放入local对象中，源码如下：
        -视图执行时，导入request，调用_lookup_req_object函数，去local对象中获取ctx对象，再去ctx对象中获取
         获取request和session
        -请求结束时，就会调用ctx.auto_pop(),将ctx从local中移除
"""
from flask import Flask, request
from functools import partial
from itertools import chain


def fun(a, b, c):
    print(a, b, c)


new_fun = partial(fun, 123)
a = [1, 2, 3]
b = [1, 2, 3]
# 将两个列表连接起来
c = chain(a, b)
print(list(c))
app = Flask(__name__)
app.run()