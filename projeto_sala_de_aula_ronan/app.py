from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# ------------------------------
# Rota raiz
# ------------------------------
@app.route('/')
def raiz():
    return "Página inicial! Vá para /inicio ou /index."

# ------------------------------
# Rotas para HTML estático
# ------------------------------
# Rota para inicio.html
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# Rota para contato.html
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota para sobre.html
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/index')
def show_index():
    return render_template('index.html')

# ------------------------------
# Rota dinâmica /codigos/<ano_nascimento>
# ------------------------------
@app.route('/codigos/<int:ano_nascimento>')
def exibe_codigos(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    dados = {
        'nome': "Ze Bonitinho",
        'ano_nascimento': ano_nascimento,
        'idade': idade,
        'texto': "Vamos escrever um texto bem longo para que o truncate funcione",
        'ativo': True,
        'pessoas': ['joao', 'maria', 'jose']
    }
    return render_template('codigos.html', **dados)

# ------------------------------
# Rotas blocos
# ------------------------------
@app.route('/home')
def home():
    return render_template('blocos/home.html')

@app.route('/produtos')
def produtos():
    return render_template('blocos/produtos.html')

@app.route('/perfil')
def perfil():
    return render_template('blocos/perfil.html')

# ------------------------------
# Executa o app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)