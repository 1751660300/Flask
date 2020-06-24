# -*- coding:utf-8 -*-
class foo(object):
    def __init__(self):
        object.__setattr__(self, 'list', {})

    def __getattr__(self, item):
        return self.list.get(item)

    def __setattr__(self, key, value):
        self.list[key] = value


f = foo()
f.__setattr__("add", lambda a, b:a+b)
print(f.add(1, 2))
print(foo.__dict__)
