from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, FloatField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class CadastroForm(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired()])
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class ProdutoForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[DataRequired()])
    price = FloatField('Preço (R$)', validators=[DataRequired()])
    image = FileField('Imagem do Produto', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Produto')