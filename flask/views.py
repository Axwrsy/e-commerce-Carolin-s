from flask import Blueprint, render_template, session, redirect, url_for

routes = Blueprint('routes', __name__)

# página inicial
@routes.route("/")
def homepage():
    # define qual menu vai aparecer, dependendo do login
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

# simula login (teste rápido) — ex: /login/admin ou /login/user
@routes.route("/login/<user_type>")
def login(user_type):
    session['logged_in'] = True
    session['user_type'] = user_type
    return redirect(url_for('routes.homepage'))

# logout
@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('routes.homepage'))

# exemplo de página adicional
@routes.route("/contato")
def contato():
    return "contate-nos!"

@routes.route("/perfil")
def perfil():
    return "página do perfil do usuário."

@routes.route("/admin")
def admin():
    return "painel de administração"
