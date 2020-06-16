# -*- coding:utf-8 -*-
"""
1.设置配置的方法
    app = Flask(__name__)
 a. app.secret_key = ''
 b. app.config['secret_key'] = ''
 c. app.config.from_pyfile("filename")
 d. app.config.from_object("filename.类名")
"""
from flask import Flask, session

app = Flask(__name__)
app.config.from_pyfile("templates/setting.py")
# app.config.from_object("templates.setting.config")


@app.route('/', methods=['post', 'get'])
def login():
    session["q"] = "123"
    return "hello world"


if __name__ == '__main__':
    app.run()
