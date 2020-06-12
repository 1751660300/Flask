# -*- coding:utf-8 -*-
"""
1.安装flask框架
    pip install flask
2.wsgi
    本质是使用的socket（网络套接字）
3.flask
    ps：对象() 执行的是对象的__call__方法
"""
from flask import Flask

# 实例化flask对象
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    # 监听用户请求
    # 如果用户请求到来。执行app的__call__方法
    app.run()
