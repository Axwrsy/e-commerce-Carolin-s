from flask import Flask
from views import routes  # importa o Blueprint de views.py
#blueprint  uma forma organizada de separar as rotas e funções do site.



app = Flask(__name__)
app.register_blueprint(routes)



if __name__ == "__main__":
    #sempre que você alterar o código e salvar, o flask reinicia o servidor automaticamente.
    app.run(port=8000, debug=True)

