# -*- coding:utf-8 -*-
# 第一步 导包
from flask import Flask, render_template, request, redirect, url_for, session
import functools


# 装饰器：判断session是否有值
def p_session(sess):
    @functools.wraps(sess)  # 保留被装饰函数的原信息，如果不加并且不设置endpoint（默认是函数名），则会报错
    def func():
        user = session.get("info")
        if not user:
            print("user")
            # return redirect('login.html', error="用户名或密码错误")
            return redirect('login')
        else:
            print("jock")
            return sess()

    return func


# 第二步 实例化一个flask对象
app = Flask(__name__)
app.secret_key = "sdada"


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
@p_session
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
