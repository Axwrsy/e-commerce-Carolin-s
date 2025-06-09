from flask import Blueprint, render_template, session, redirect, url_for, request

routes = Blueprint('routes', __name__)

@routes.route("/")
def homepage():
    if session.get('logged_in'):
        if session.get('user_type') == 'admin':
            menu = [
                {'name': 'Início', 'url': '#hero'},
                {'name': 'Admin', 'url': '/admin'},
                {'name': 'Sair', 'url': '/logout'},
            ]
        else:
            menu = [
                {'name': 'Início', 'url': '#hero'},
                {'name': 'Perfil', 'url': '/perfil'},
                {'name': 'Sair', 'url': '/logout'},
            ]
    else:
        menu = [
            {'name': 'Início', 'url': '#hero'},
            {'name': 'Sobre', 'url': '#about'},
            {'name': 'Serviços', 'url': '#services'},
            {'name': 'Login', 'url': '/login/user'},
        ]

    return render_template("homepage.html", menu=menu)

@routes.route("/login/<user_type>")
def login(user_type):
    session['logged_in'] = True
    session['user_type'] = user_type
    return redirect(url_for('routes.homepage'))

@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('routes.homepage'))

@routes.route("/cadastro", methods=["POST"])
def cadastro():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    # Salva os dados em um arquivo .txt
    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome} | Email: {email} | Senha: {senha}\n")

    return "Cadastro realizado com sucesso"

@routes.route("/perfil")
def perfil():
    return "Página de perfil"

@routes.route("/admin")
def admin():
    return "Painel de administração"

@routes.route("/contato")
def contato():
    return "Página de contato"
