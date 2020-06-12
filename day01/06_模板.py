# -*- coding:utf-8 -*-
"""
1.flask使用的模板是jinja2模板，所以其语法与Django无差别
2.页面传递参数可以传递函数
3.在前端可以使用管道safe防止xss攻击，在后端可以使用Markup函数防止xss攻击
"""
from flask import Flask, render_template, Markup

app = Flask(__name__)


def fun():
    return Markup("<h1>hahaha</h1>")


@app.route('/')
def index():
    return render_template('model.html', f=fun)  # 传递一个函数


if __name__ == '__main__':
    app.run()
