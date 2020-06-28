# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from wtforms import Form, validators
from wtforms.fields import *
from wtforms import widgets

app = Flask(__name__)


class LoginForm(Form):
    '''Form'''
    name = simple.StringField(
        label="用户名",
        widget=widgets.TextInput(),
        validators=[
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(max=8, min=3, message="用户名长度必须大于%(max)d且小于%(min)d")
        ],
        render_kw={"class": "form-control"}  # 设置属性生成的html属性
    )

    pwd = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空"),
            validators.Length(max=18, min=4, message="密码长度必须大于%(max)d且小于%(min)d"),
            validators.Regexp(regex="\d+", message="密码必须是数字"),
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "form-control"}
    )


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():  # 对用户提交数据进行校验，form.data是校验完成后的数据字典
            print("用户提交的数据用过格式验证，值为：%s" % form.data)
            return "登录成功"
        else:
            print(form.errors, "错误信息")
        return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
