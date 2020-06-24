# -*- coding:utf-8 -*-
"""
1.组件：
    a.flask-script
        用于实现类似于django的运行命令的功能
        1).使用：
            导包：
            from flask_script import Manager

            将app加入管理
            manager = Manager(app)

            运行：
            manager.run()

            最后就可以向django一样启动服务，和使用其他的一些功能
    b.flask-migrate
"""