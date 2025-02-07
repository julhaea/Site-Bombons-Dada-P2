from flask import render_template, request, redirect, url_for, session, flash
from appo import app, db, bcrypt
from appo.forms import LoginForm, CadastroForm
from appo.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('admprodutos'))  # Redireciona para a página de produtos
        else:
            flash('Usuário ou senha incorretos', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Você saiu da conta', 'info')
    return redirect(url_for('login'))

@app.route('/admprodutos')
def admprodutos():
    if 'user_id' not in session:
        flash('Faça login para acessar esta página', 'warning')
        return redirect(url_for('login'))
    return render_template('admprodutos.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        codigo = form.codigo.data
        username = form.username.data
        password = form.password.data

        # Validação do código de cadastro
        CODIGO_ESPERADO = "20122000"
        if codigo != CODIGO_ESPERADO:
            flash('Código de cadastro incorreto!', 'danger')
            return redirect(url_for('cadastro'))
        
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Nome de usuário já existe!', 'danger')
            return redirect(url_for('cadastro'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        novo_usuario = User(username=username, password=hashed_password)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)