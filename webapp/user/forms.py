from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError

from webapp.user.models import User

# Создали класс для формы 
# DataRequired проверяет указаны ли даты без лишнего кода
# render_kw присваивает класс в html. Классы взяты из bootstrap.
# remember_me для запоминания текущего пользователя. render_kw - для отображения в разметке Bootstrap поле checkbox
#  default=True - по умолчанию чекбокс отмечен
class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-dark"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!',render_kw={"class": "btn btn-primary"})


    # проверка есть ли предлагаемое имя пользователя в базе
    def validate_username(self, username):
        # делаем поиск имени в базе. Если есть, то показываем сообщение с ошибкой
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')
    

    # проверка есть ли предлагаемая почта в базе
    def validate_email(self, email):
        # делаем поиск почты в базе. Если есть, то показываем сообщение с ошибкой
        email_count = User.query.filter_by(email=email.data).count()
        if email_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')