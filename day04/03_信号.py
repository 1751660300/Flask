# -*- coding:utf-8 -*-
"""
1.flask 框架的信号基于blinker
    使用信号需要手动安装blinker
    安装：pip install blinker
2.使用信号
    a.导入flask中signals模块
        from flask import signals
    b.写一个信号函数
        def s():
            print("信号")
    c.为信号函数注册
        signals.request_started.connect(s)
    d.触发信号，执行函数
        signals.request_started.send()
        不用我们去触发，flask中执行到相应的位置会自动触发
3.信号的类型
    request_started = _signals.signal("request-started")                # 请求到来前执行
    request_finished = _signals.signal("request-finished")              # 请求结束后执行

    template_rendered = _signals.signal("template-rendered")            # 模板渲染后执行
    before_render_template = _signals.signal("before-render-template")  # 模板渲染前执行

    request_tearing_down = _signals.signal("request-tearing-down")      # 请求完毕后自动执行，无论是否成功
    got_request_exception = _signals.signal("got-request-exception")    # 请求出现异常时自动执行
    appcontext_tearing_down = _signals.signal("appcontext-tearing-down") # 请求上下文完毕后自动执行，无论是否成功
    appcontext_pushed = _signals.signal("appcontext-pushed")            # 请求上下文pushed时自动执行
    appcontext_popped = _signals.signal("appcontext-popped")            # 请求上下文popped时自动执行
    message_flashed = _signals.signal("message-flashed")                # 调用flash在其中添加数据时触发
4.触发信号的流程
    a.before_first_request
    b.触发request_started 信号
    c.before_request
    d.模板渲染
        template_rendered  # 模板渲染后执行
        渲染
        before_render_template # 模板渲染前执行
    e.after_request
    f.session.save_session()
    g.触发request_finished信号
    h.触发request_tearing_down信号
"""
from flask import signals, Flask

app = Flask(__name__)


# 信号函数
def s(*args, **kwargs):
    print("信号", *args, **kwargs)


# 注册信号函数
signals.request_started.connect(s)


@app.route("/")
def fun():
    print("app")
    return "app"


@app.before_first_request
def first():
    print("first")


if __name__ == '__main__':
    app.__call__
    app.run()
