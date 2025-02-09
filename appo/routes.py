from flask import render_template, request, redirect, url_for, session, flash, send_from_directory
from appo import app, db, bcrypt
from appo.forms import LoginForm, CadastroForm, ProdutoForm
from appo.models import User, Produto
import os


# Caminho para a pasta de uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')




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
    form=ProdutoForm
    if 'user_id' not in session:
        flash('Faça login para acessar esta página', 'warning')
        return redirect(url_for('login'))
    
    dadosprodutos = Produto.query.all()  # Busca todos os produtos no banco de dados
    return render_template('admprodutos.html', form=form, dadosprodutos=dadosprodutos)
    

@app.route('/produtos')
def produtos():
    dadosprodutos = Produto.query.all()  # Busca todos os produtos no banco de dados
    return render_template('produtos.html', dadosprodutos=dadosprodutos)

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

# Rota para cadastrar um novo produto
@app.route('/cadastrar-produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'user_id' not in session:
        flash('Faça login para acessar esta página', 'warning')
        return redirect(url_for('login'))
    
    form = ProdutoForm()
    if form.validate_on_submit():
        if 'image' not in request.files:
            flash('Nenhum arquivo enviado', 'danger')
            return redirect(request.url)
        
        file = request.files['image']

        if file.filename == '':
            flash('Nenhum arquivo selecionado', 'danger')
            return redirect(request.url)
        
        if file and file.filename:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            
            file.save(file_path)

            new_product = Produto(
                name=form.name.data,
                price=form.price.data,
                image=filename
            )
            db.session.add(new_product)
            db.session.commit()

            flash('Produto cadastrado com sucesso!', 'success')
            return redirect(url_for('admprodutos'))
        else:
            flash('Extensão de arquivo não permitida', 'danger')
            return redirect(request.url)

    return render_template('cadastrar_produto.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
