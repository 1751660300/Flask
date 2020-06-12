# -*- coding:utf-8 -*-
"""
1.新建视图包，并在试图包的__init__.py中创建Flask对象
    from flask import Flask
    app = Flask(__name__)
2.创建的每一个视图模块中实例化Blueprint(),获取一个Flask对象
    from flask import Blueprint
    acc = Blueprint("acc", __name__)
    之后就可以对应的路由了
3.在视图包的__init__.py文件中注册视图模块中的Flask对象，使用app.register_blueprint(acc)
    from . import account
    app.register_blueprint(account.acc)
4.客户端的请求只能访问app，由app来分发请求
5.视图模块中的flask对象可以单独访问templates和static文件，先到最外层寻找资源文件，再到指定的资源文件
    acc = Blueprint("acc", __name__, template_folder='', static_folder='', url_prefix='/xxx')
    url_prefix='/xxx' : 为每一个视图模块的路由路径添加"/xx", 否则无法访问。
6.可以再每一个视图模板中添加单独的请求扩展，其他视图模板不执行
7.蓝图对象的名称，不能与方法名称相同
示例：见lantu_test项目
"""

