# -*- coding:utf-8 -*-
from flask import Flask

# 实例化flask对象
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


class md(object):  # 中间件
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, *args, **kwargs):
        print("开始之前")
        ret = self.old_wsgi_app(*args, **kwargs)
        print("结束之后")
        return ret


if __name__ == '__main__':
    # 监听用户请求
    # 如果用户请求到来。执行app的__call__方法
    app.wsgi_app = md(app.wsgi_app)
    app.run()
