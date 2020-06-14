# -*- coding:utf-8 -*-
"""
1.安装flask框架
    pip install flask
2.wsgi
    本质是使用的socket（网络套接字）
3.flask
    ps：对象() 执行的是对象的__call__方法
"""
from flask import Flask, request, render_template

# 实例化flask对象
app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def hello_world():
    msg = ""
    username = request.form.get("username")
    password = request.form.get("password")
    if username == 'jock' and password == '123':
        msg = "登录成功"
    elif username is None and password is None:
        msg = ""
    else:
        msg = "账户或密码错误"
    return render_template("login.html", message=msg)


if __name__ == '__main__':
    # 监听用户请求
    # 如果用户请求到来。执行app的__call__方法
    app.run()
