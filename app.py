import hashlib
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
from model.controler_usuario import Usuario


app = Flask(__name__)

# Criando para poder usar sessões
app.secret_key = "Godofredolindo"

lista_mensagem = [

]



# ROTAS DO COMENTÁRIO
@app.route("/")
@app.route("/comentario")
def pagina_inicial():
    if "usuario" in session:
        # Para escrever na página HTML
        # Recuperar as mensagens
        # Somente para recuperar alguma coisa 
        mensagens = Mensagem.recuperar_mensagens()
    
        # Enviar as mensagens para o template
         # return render_template ("pagina_inicial.html")
        return render_template("pagina_inicial.html", mensagens = mensagens)   
        
    else:
        return redirect("/login")

# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/mensagem" , methods = ["POST"])
def post_mensagem():

    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    
    # Cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrarmensagem(usuario, mensagem)
    
    
    # Redireiona para a pagina inicial
    return redirect("/comentario")

# Rota para excluir um comentário
@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):

    # Chamando a função para deletar
    Mensagem.deletar_mensagem(codigo)
    return redirect("/comentario")

# Rota para obter curtida
@app.route('/put/mensagem/adicionar/curtida/<codigo>')
def adicionar_curtida(codigo):

    # Chama a função para adicionar a curtida
    Mensagem.adicionar_curtida(codigo) 
    
    # Redireciona para a página inicial
    return redirect("/comentario") 

@app.route('/put/mensagem/delete/curtida/<codigo>')

def deletar_curtida(codigo):

    # Chama a função para adicionar a curtida
    Mensagem.deletar_curtida(codigo) 
    
    # Redireciona para a página inicial
    return redirect("/comentario") 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ROTAS DE CADASTRAR USUARIO

# Somente para pagina aparecer
@app.route("/usuario")
def pagina_usuario():
    # Para escrever na página HTML
    # Recuperar as mensagens
    
    # Enviar as mensagens para o template
    return render_template("cadastrar.html")


# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/usuario" , methods = ["POST"] )
def post_usuario():

    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    login = request.form.get("login")
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    
    # Cadastrando a mensagem usando a classe mensagem
    Usuario.cadastrarUsuario(login, usuario , senha )
    
    
    # Redireiona para a pagina inicial
    return redirect("/usuario")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ROTAS DE LOGIN

@app.route("/login")
def pagina_login():
    # Para escrever na página HTML
    
    # Enviar o usuario para o template
    return render_template("login.html")


# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/logar" , methods = ["POST"] )
def post_logar():
    
    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    usuario = request.form.get("login")

    senha = request.form.get("senha")
    
    # Cadastrando o usuario usando a classe Usuario
    esta_logado = Usuario.verificarLogin(usuario , senha )

    # Verificando se o builiano criado no controler_usuario for True ele direcina para página comentários, senão direciona para página login
    if esta_logado:
        return redirect('/comentario')
    else:
        return redirect('/login')

# ROTAS DE LOGOFF
@app.route("/logoff")
def post_deslogar():

    # Enviar as mensagens para o template
    return render_template("login.html")

@app.route("/api/get/mensagens")
def api_get_mensagens():
    mensagens =  Mensagem.recuperar_mensagens()
    return jsonify(mensagens)

@app.route("/api/get/ultimamensagem/<usuaio>")
def api_get_ultima_mensagens(usuario):
    mensagem = Mensagem.ultima_mensagem(usuario)
    return jsonify(mensagem)
    
# Para iniciar o app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)