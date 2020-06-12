# -*- coding:utf-8 -*-
"""
1.使用 @app.before_request 装饰器装饰的函数，可以在每一次请求之前执行该函数（相当与检测）
2.如果有返回值，则表示被拦截了
3.如果没有返回值，则表示通过检测了
4.简单使用：用户认证
5.使用 @app.after_request  装饰器装饰的函数，可以在每一次请求之后执行，该函数必须要有response参数，必须要返回response
6.可以写多个这样的函数，@app.before_request 装饰的函数，顺序执行，@app.after_request 装饰的函数
    倒序执行
7.请求拦截后，所有的 @app.after_request 装饰的函数都会执行
8.定制错误信息 使用 @app.errorhandler([状态码]) 装饰器来定制错误信息
9.使用 @app.template_filter @app.template_global 装饰器装饰的函数，可以在页面中调用
"""

# 第一步 导包
from flask import Flask, render_template, request, redirect, url_for, session
import functools

# 第二步 实例化一个flask对象
app = Flask(__name__)
app.secret_key = "sdada"


# 装饰器：判断session是否有值
@app.before_request
def p_session():
    print(request.path)
    if request.path == "/login":
        return None
    user = session.get("info")
    if not user:
        # return redirect('login.html', error="用户名或密码错误")
        return redirect('login')


# 第三步 设置路由
@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'get':
        return render_template('login.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username == 'jock' and password == '123':
            url = url_for('detail')
            session["info"] = username
            return redirect(url)
        return render_template('login.html', error="用户名或密码错误")


USER = {
    'name': '张山',
    'age': '15',
    'detail': '123456'
}


@app.route('/index', methods=['get', 'post'], endpoint="detail")
def index():
    # user = session.get("info")
    # if not user:
    #     return render_template('login.html')
    return render_template('detail.html', user=USER)


if __name__ == '__main__':
    app.run()

# 问题： redirect()  参数是路径
# 使用session需要添加一个
# app.config['SECRET_KEY'] = ''
# app.secret_key = ''
