# -*- coding:utf-8 -*-
"""
1.
    app.route('/', methods=['post', 'get'])
        def route(self, rule, **options):
            def decorator(f):
                endpoint = options.pop("endpoint", None)
    本质        self.add_url_rule(rule, endpoint, f, **options)
                return f

        return decorator
2. 如果endpoint不写，则会默认为文件名
3.add_url_rule()和@app.route()参数
    rule : URL规则
    view_func : 视图函数的名称
    defaults=None : 默认没有参数，如果需要参数，defaults={'nid': 12}
    endpoint=None : 名称用于反向生成URL，即：url_for('名称')
    methods=None : 允许的请求方式
    strict_slashes=None : 对url最后的'/'是否严格要求，
                            如果为False：http://127.0.0.1:5000/index 和http://127.0.0.1:5000/index/ 均可访问
                            如果为True http://127.0.0.1:5000/index 可以访问
    redirect_to=None : 重定向到指定url
    subdomain
4.常用的路径
    @app.route('/user/<username>')  传递字符串
    @app.route('/user/<int:id>')  传递整数
    @app.route('/user/<float:id>')  传递浮点数
    @app.route('/user/<path:path>')  传递路径
5.自定义传递类型
    class BaseConverter(object):
    regex = "[^/]+"
    weight = 100

    def __init__(self, map):
        self.map = map

    def to_python(self, value):
        return value

    def to_url(self, value):
        if isinstance(value, (bytes, bytearray)):
            return _fast_url_quote(value)
        return _fast_url_quote(text_type(value).encode(self.map.charset))
    a.创建类并继承BaseConverter，实现to_python方法
    b.把自定义的类添加进app.url_map.converters字典中
    c.然后自己就可以使用自定义的路径
"""
from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, maps, regex):
        super(RegexConverter, self).__init__(maps)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传给视图函数中的参数
        :param value:
        :return:
        """
        return value

    def to_url(self, value):
        val = super(RegexConverter, self).to_url(value)
        return val


app = Flask(__name__)
app.url_map.converters['re'] = RegexConverter


@app.route("/<re('\d+'):nid>", methods=['post', 'get'])
def index(nid):
    return "regex"


if __name__ == '__main__':
    app.run()
