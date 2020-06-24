# -*- coding:utf-8 -*-
"""
1.知道即可
2.如果是多app应用时，上下文管理是如何实现的
    flask的local与多app无关，他是根据线程划分的
"""
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
app1 = Flask("app1")
app2 = Flask("app2")


@app1.route("/index")
def fun1():
    return 'app1'


@app2.route("/index")
def fun2():
    return 'app2'


# 访问app1: http://localhost:5000/index
# 访问app2: http://localhost:5000/scr/index
dm = DispatcherMiddleware(app1, {"/scr": app2})

if __name__ == '__main__':
    run_simple("localhost", 5000, dm)
