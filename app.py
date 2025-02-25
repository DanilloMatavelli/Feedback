from flask import Flask

app = Flask(__name__)

# AQUI IRÁ TODAS AS MINHAS ROTAS
@app.route("/")
def pagina_inicial():
    # Para escrever na página HTML
    return "SUPER PÁGINA PRINCIPAL"

# Para iniciar o app
app.run(debug=True)