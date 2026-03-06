from flask import Flask, render_template  # Import correto

app = Flask(__name__)

# Rota raiz: mantém a mensagem de texto
@app.route('/inicio')
def inicio():
    return render_template ('inicio.html')

# Nova rota para index.html
@app.route('/index')  # ✅ precisa começar com barra
def show_index():
    return render_template('index.html')  # chama o HTML





@app.route('/codigos/<int:ano_nascimento>')
def exibe_codigos(ano_nascimento):
    ## ano_nascimento = 1988
    dados = {
        'nome': "Ze Bonitinho",
        'ano_nascimento': ano_nascimento,
        'idade': (2026 - ano_nascimento),
        'texto': "Vamos escrever um texto bem longo para que o truncate funcione",
        'ativo':True,
        'pessoas': ['joao', 'maria', 'jose']
    }
    return render_template('codigos.html', **dados)


@app.route('/home')
def home():
    return render_template('blocos/home.html')

@app.route('/produtos')
def produtos():
    return render_template('blocos/produtos.html')

@app.route('/perfil')
def perfil():
    return render_template('blocos/perfil.html')

if __name__ == "__main__":
    app.run(debug=True)