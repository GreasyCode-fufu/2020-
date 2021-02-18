from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    TextAreaField,
    SubmitField,
    MultipleFileField,
)
from wtforms.fields import simple
from wtforms.validators import DataRequired, Length, ValidationError, Email, Optional
from wtforms import validators
from wtforms import widgets
from wtforms import Form


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "用户名"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "密码"},
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("登录")


class selectForm(FlaskForm):
    goodsid = StringField(
        "goodsid",
        validators=[DataRequired()],
        render_kw={"placeholder": "商品号"},
    )
    goodsname = StringField(
        "goodsname",
        validators=[DataRequired()],
        render_kw={"placeholder": "商品名"},
    )
    store = StringField(
        "store",
        validators=[DataRequired()],
        render_kw={"placeholder": "库存数"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "密码"},
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("查询")


class addgoodsForm(FlaskForm):
    goodsid = StringField(
        "商品号: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入商品号"},
    )

    predict = StringField(
        "运行内存大小: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入运行内存大小:"},
    )

    goodsname = StringField(
        "商品名: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "商品名"},
    )

    goodstatus = StringField(
        "商品状态: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "商品状态"},
    )

    store = StringField(
        "库存数: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "库存数"},
    )
    submit = SubmitField("确定")


class goodsForm(FlaskForm):
    goodsid = StringField(
        "商品号: ",
        validators=[DataRequired(), Length(3, 12)],
        render_kw={"placeholder": "请输入商品号", "class": "test"},
    )
    goodsname = StringField(
        "商品名: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "商品名"},
    )

    goodstype = StringField(
        "产品型号: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入型号名"},
    )

    body1 = TextAreaField('Body', validators=[DataRequired()])
    body2 = TextAreaField('Body', validators=[DataRequired()])
    body3 = TextAreaField('Body', validators=[DataRequired()])
    # body = StringField('Body', validators=[DataRequired()])

    goodsprice = StringField(
        "价格: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入价格"},
    )

    goodscolor = StringField(
        "颜色: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入商品颜色"},
    )

    goodsremarks = StringField(
        "备注: ",
        validators=[Optional(strip_whitespace=True)],
        render_kw={"placeholder": "请输入商品描述信息:"},
    )

    store = StringField(
        "库存数: ",
        validators=[DataRequired(message="库存数不能为空! ")],
        render_kw={"placeholder": "库存数"},
    )
    submit = SubmitField("确定")


class userForm(FlaskForm):
    username = StringField(
        "用户名: ",
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "请输入用户名"},
    )
    password = PasswordField(
        "密码: ",
        validators=[DataRequired()],
        render_kw={"placeholder": "请输入密码"},
    )

    submit = SubmitField("添加")


class UploadForm(FlaskForm):
    photo = FileField(
        "上传商品图片",
        validators=[FileRequired(), FileAllowed(["jpg", "jpeg", "png", "gif"])],
    )
    submit = SubmitField()


class MultiUploadForm(FlaskForm):
    photo = MultipleFileField("上传商品图片", validators=[DataRequired()])
    submit = SubmitField()
