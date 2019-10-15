from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators

class FormLogin(FlaskForm):
    user = StringField('Usuário', [validators.DataRequired(message="Digite seu usuário!")])
    password = PasswordField('Senha', [validators.DataRequired(message="Digite sua senha!")])
    submit = SubmitField('Entrar')