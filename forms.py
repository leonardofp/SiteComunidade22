from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmacao', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    botao_submit_login = SubmitField('Fazer Login')