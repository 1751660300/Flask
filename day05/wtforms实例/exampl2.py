# -*- coding:utf-8 -*-
from flask import Flask, render_template, redirect, request
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder="templates")
app.debug = True


# =======================simple===========================
class RegisterForm(Form):
    name = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "form-control"},
        default="wd"
    )
    pwd = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空")
        ]
    )
    pwd_confim = simple.PasswordField(
        label="重复密码",
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    # 　　========================html5============================
    email = html5.EmailField(  # 注意这里用的是html5.EmailField
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    # 　　===================以下是用core来调用的=======================
    gender = core.RadioField(
        label="性别",
        choices=(
            (1, "男"),
            (1, "女"),
        ),
        coerce=int  # 限制是int类型的
    )
    city = core.SelectField(
        label="城市",
        choices=(
            ("bj", "北京"),
            ("sh", "上海"),
        )
    )
    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )
    favor = core.SelectMultipleField(
        label="喜好",
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):  # 这里的self是一个RegisterForm对象
        '''重写__init__方法'''
        super(RegisterForm, self).__init__(*args, **kwargs)  # 继承父类的init方法
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))  # 把RegisterForm这个类里面的favor重新赋值，实现动态改变复选框中的选项

    def validate_pwd_confim(self, field, ):
        '''
        自定义pwd_config字段规则，例：与pwd字段是否一致
        :param field:
        :return:
        '''
        # 最开始初始化时，self.data中已经有所有的值
        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        form = RegisterForm(data={'gender': 1})  # 默认是1,
        return render_template("register.html", form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():  # 判断是否验证成功
            print('用户提交数据通过格式验证，提交的值为：', form.data)  # 所有的正确信息
        else:
            print(form.errors)  # 所有的错误信息
        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
