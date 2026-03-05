from flask import Flask, render_template  # Import correto

app = Flask(__name__)

# Rota raiz: mantém a mensagem de texto
@app.route("/")
def home():
    return "Servidor funcionando 🚀"

# Nova rota para index.html
@app.route("/index")  # ✅ precisa começar com barra
def show_index():
    return render_template('index.html')  # chama o HTML

if __name__ == "__main__":
    app.run(debug=True)