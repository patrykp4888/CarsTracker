from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import DataRequired, Email, Length, EqualTo
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired(), Length(min=8)])
    confirm_pwd = StringField('confirm_pwd', validators=[DataRequired(), EqualTo('password', message='Passwords must match!')])