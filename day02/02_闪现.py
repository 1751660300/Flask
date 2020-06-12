# -*- coding:utf-8 -*-
"""
闪照数据
1.使用flash()函数进行存储数据
    flash(message, category="message")
    可以使用category参数进行分类
2.使用get_flashed_messages()函数进行获取数据，获取完数据，则数据清除
    get_flashed_messages(with_categories=False, category_filter=())
    可以按照分类进行获取数据
3.应用：对临时数据进行操作，如错误信息
4.本质：是使用session存储数据，取出数据后在删除
"""
from flask import Flask, flash, get_flashed_messages

# 实例化flask对象
app = Flask(__name__)


@app.route('/set')
def sets():
    # 向某个地方设置值
    flash("钱良虎", category="name")
    return 'hello world!'


@app.route('/get')
def gets():
    # 从某个地方获取已设置的值，并删除，
    data = get_flashed_messages(category_filter="name")
    print(data)
    return 'hello world!'


if __name__ == '__main__':
    # 监听用户请求
    # 如果用户请求到来。执行app的__call__方法
    app.run()