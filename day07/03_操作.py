# -*- coding:utf-8 -*-
"""
1.对数据库中的表进行操作
    # 添加对象，向数据库中添加啊数据
    # 除了add还有很多其他的方法

    session.add(obj1)  # 添加一条数据
    session.add_all([obj1, obj2, ...])  # 添加多条数

    session.query(Uesr).all()  # 查询表中所有数据，返回一个对象列表
    session.query(Uesr).filter(User.id > 2)  # 根据条件查询表中数据，返回一个对象列表

    session.query(Uesr).filter(User.id > 2).delete()  # 根据条件查询表中数据，删除

    session.query(Uesr).filter(User.id = 2).update("id": "5")  # 根据条件查询表中数据，更新
    session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
    session.query(Users).filter(Users.id > 0).update({"age": Users.age + 1}, synchronize_session="evaluate")

    增删改都要commit

    r1 = session.query(Users).all()
    # 查询字段并重命名
    r2 = session.query(Users.name.label('xx'), Users.age).all()
    r3 = session.query(Users).filter(Users.name == "alex").all()
    r4 = session.query(Users).filter_by(name='alex').all()
    r5 = session.query(Users).filter_by(name='alex').first()
    r6 = session.query(Users).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(Users.id).all()
    r7 = session.query(Users).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
"""