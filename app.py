from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask(__name__)

lista_mensagem = [

]



# AQUI IRÁ TODAS AS MINHAS ROTAS
@app.route("/")
def pagina_inicial():
    # Para escrever na página HTML
    # Recuperar as mensagens
    mensagens = Mensagem.recuperar_mensagens()
    
    # Enviar as mensagens para o template
    return render_template("index.html", mensagens = mensagens)

    # return render_template ("pagina_inicial.html")

# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/mensagem" , methods = ["POST"])
def post_mensagem():

    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    
    # Cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    
    
    # Redireiona para a pagina inicial
    return redirect("/")


# Para iniciar o app
app.run(debug=True)