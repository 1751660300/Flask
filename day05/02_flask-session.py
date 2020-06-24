# -*- coding:utf-8 -*-
"""
1.flask-session 的处理机制（内置：是将session保存在加密的cookie中实现）
    a.请求到来时
        获取随机字符串，存在则去“数据库”中获取原来的个人数据，否则创建一个空容器，
    b.视图
        操作内存中的 对象（随机字符串，{放置数据的容器}）
    c.响应
        将数据保存到数据库中
        把随机字符串写在用户的cookie中
2.自定义flask-session
    a.请求到来时
        创建特殊的字典，并存在local中
        # 如果self.session为空
        if self.session is None:
            # 由于self.app.session_interface = SecureCookieSessionInterface()
            session_interface = self.app.session_interface
            # 所以session_interface.open_session(self.app, self.request)就相当于
            # SecureCookieSessionInterface().open_session(self.app, self.request)
            self.session = session_interface.open_session(self.app, self.request)

            if self.session is None:
                self.session = session_interface.make_null_session(self.app)
    b.调用时
        session -> LocalProxy -> 偏函数 -> LocalStack -> Local

    c. 请求终止时
        self.session_interface.save_session(self, session, response)

"""
from flask import Flask, session
from flask_session import RedisSessionInterface
app = Flask(__name__)
# 实例化RedisSessionInterface()需要传递参数如下：
"""
def __init__(self, redis, key_prefix, use_signer=False, permanent=True):
    if redis is None:
        from redis import Redis
        redis = Redis()
    self.redis = redis
    self.key_prefix = key_prefix
    self.use_signer = use_signer
    self.permanent = permanent
"""
app.session_interface = RedisSessionInterface()
# 调用RedisSessionInterface的open_session
"""
def open_session(self, app, request):
    # 获取cookie中的session
    sid = request.cookies.get(app.session_cookie_name)
    if not sid:
        # 创建一个随机字符串
        sid = self._generate_sid()
        # 创建一个特殊的字典并返回
        return self.session_class(sid=sid, permanent=self.permanent)
    if self.use_signer:
        signer = self._get_signer(app)
        if signer is None:
            return None
        try:
            sid_as_bytes = signer.unsign(sid)
            sid = sid_as_bytes.decode()
        except BadSignature:
            sid = self._generate_sid()
            return self.session_class(sid=sid, permanent=self.permanent)

    if not PY2 and not isinstance(sid, text_type):
        sid = sid.decode('utf-8', 'strict')
    # 如果sid不为空的话，就向redis中获取数据
    val = self.redis.get(self.key_prefix + sid)
    if val is not None:
        try:
            # 反序列化为session_class，并返回
            data = self.serializer.loads(val)
            return self.session_class(data, sid=sid)
        except:
            return self.session_class(sid=sid, permanent=self.permanent)
    return self.session_class(sid=sid, permanent=self.permanent)
"""
# 调用save_session
"""
# 序列化
val = self.serializer.dumps(dict(session))
# 像redis中设置值
self.redis.setex(name=self.key_prefix + session.sid, value=val,
                 time=total_seconds(app.permanent_session_lifetime))
if self.use_signer:
    session_id = self._get_signer(app).sign(want_bytes(session.sid))
else:
    session_id = session.sid
# 将session.sid（随机字符串）传递给用户cookie，将数据保存在redis中
response.set_cookie(app.session_cookie_name, session_id,
                    expires=expires, httponly=httponly,
                    domain=domain, path=path, secure=secure)

"""

'''
问题：如何设置关闭浏览器，cookie就失效
    response.set_cookie('', '', exipre=None)
'''