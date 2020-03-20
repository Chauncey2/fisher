from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多十个字符')])

    def validate_email(self, field):
        """
        自定义校验email是否已经注册过
        :param field:form
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮件已经注册")

    def validate_nickname(self, field):
        """
        自定义校验nickname是否已经注册过
        :param field:form
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("昵称已经窜仔")


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])
