from flask import Flask
from views import routes  # importa o Blueprint de views.py

app = Flask(__name__)
app.secret_key = "123456"  # Pode ser qualquer string aleatória — troque depois por segurança

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
